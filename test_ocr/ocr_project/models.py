from django.db import models

# # Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# class UploadImage(models.Model):
#     caption = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images')

#     def __str__(self):
#         return self.caption 

# class UploadedImage(models.Model):
#     image = models.ImageField(upload_to='images/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

class ImageUploadedForm(models.Model):
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"image uploaded"