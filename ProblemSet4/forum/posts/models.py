from django.db import models

class Post(models.Model):
    '''
    A post is a message that a user can post to the forum
    '''

    #the name of the author of the post must be less than 20 characters
    author = models.CharField(max_length=20)

    #the body of the post must contain a maximum of 120 characters 
    body = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.body}"



    
