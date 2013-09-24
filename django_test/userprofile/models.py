from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    # one user will only have one user profile
    user = models.OneToOneField(User)
    likes_cheese = models.BooleanField()
    fav_name = models.CharField(max_length=50)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
