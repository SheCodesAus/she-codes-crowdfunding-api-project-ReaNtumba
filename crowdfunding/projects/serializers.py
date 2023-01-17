from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous','project', 'supporter']
        read_only_fields = ['id', 'supporter']


    def create(self, validated_data):
            return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer): #list of all the fields on our model
    id = serializers.ReadOnlyField() #should be read-only. Django assists the ID, so no one can change it
    title = serializers.CharField(max_length=200) 
    description = serializers.CharField(max_length=None) #charfield for short text and text field for long text. we need both in this model
    goal = serializers.IntegerField() 
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data) #double asterix unpacking . Hands each key value pair, it changes the format of the list'


class ProjectDetailsSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
