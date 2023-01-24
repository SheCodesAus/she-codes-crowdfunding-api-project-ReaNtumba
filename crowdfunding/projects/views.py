from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer,ProjectDetailsSerializer, PledgeSerializer
from django.http import Http404
from rest_framework import status, generics, permissions
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView): #project list is where you get all the projects
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        projects = Project.objects.all() #we are using the GET requests as REST verb
        serializer = ProjectSerializer(projects, many=True) #we say many=true because it is a list of projects, many
        return Response(serializer.data) #serializer.data woyld be an end point
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data) #take the data from serializer and use that data for your request
        if serializer.is_valid():
            serializer.save(owner=request.user) #is this data valid?, if yes SAVE
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED
            ) #return response from the end point

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:#catches errors as they occur in your code
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project #Try return project
        except Project.DoesNotExist: #if the are exceptions
            raise Http404 #raise this http error
            #logic is the person allowed access? do they have permssions

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailsSerializer(
            instance=project,
            data=data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

        #you need to come in and update the code here for when it is NOT valid like the views above
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailsSerializer(project) #project serializer turns the project into json
        return Response(serializer.data)

class PledgeList(generics.ListCreateAPIView): #this is a generic get and post, you let the system know the
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)
    # def get(self, request): #If you want pledges only for specific projects you can modify here and include the pk to go to specific projects not all
    #     pledges = Pledge.objects.all()
    #     serializer = PledgeSerializer(pledges, many=True)
    #     return Response(serializer.data)
        
    # def post(self, request):
    #     serializer = PledgeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_201_CREATED
    #         )

    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )
