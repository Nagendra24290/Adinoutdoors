from django.db import models

class OutdoorMedium(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    outdoor_medium = models.ForeignKey(OutdoorMedium, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    size = models.CharField(max_length=20)  # e.g., "24 x 30"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ad_images/')  # Upload folder
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name}"
    

class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return self.title
