from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image = models.URLField() #images through a URL field
    is_open = models.BooleanField() #know if project is running
    date_created = models.DateTimeField(auto_now_add=True) #when project as first created,tells Django ehenever model is created set model to the current time when its created immediatly. like auto record
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, #if user deletes a model all their projects will be deleted
        related_name='owner_projects' #user.owner projects we get all the projects they created
    ) #this model should be linked to the user, one you create a user, we will have to change this to a foreginkey(owner in another table I want to reference) to link to the user

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE, #If project that gets cancelled, the owner and everything linked to the project should get cancelled
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )