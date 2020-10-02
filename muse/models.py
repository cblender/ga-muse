from django.db import models

class Gallery(models.Model):

    # Set the length of a gallery title to the length of a tweet
    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title

class Image(models.Model):
    name = models.CharField(max_length=140)
    img_url = models.URLField(max_length=280) # this will allow for longer image urls to be entered
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.name