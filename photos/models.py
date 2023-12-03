from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Gallery(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()
    created_data=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title}"
