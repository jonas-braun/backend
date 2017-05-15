from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Tag(models.Model):
    text = models.CharField(max_length=64)

    def __str__(self):
        return "TAG[id: %s, tag: %s]" % (self.pk, self.text)



class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return "USERPROFILE:[id: %s, username: %s]" % (self.pk, self.user.username)


class Question(models.Model):
    text = models.TextField(max_length=500)
    tags = models.ManyToManyField(Tag, related_name="questions")
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(Userprofile, through="VoteQuestion", related_name='votes')
    creator = models.ForeignKey(User)

    def __str__(self):
        return "[ id: %s, creator: %s ]" % ( self.pk, self.creator.username )


class VoteQuestion(models.Model):
    class Meta:
        unique_together = ['question', 'user']
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    text = models.TextField(max_length=5000)
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class VoteAnswer(models.Model):
    class Meta:
        unique_together = ['question', 'user']
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    up = models.BooleanField()