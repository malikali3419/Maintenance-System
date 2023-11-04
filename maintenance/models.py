from django.db import models

class Andrede(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    andrede_name = models.CharField(max_length=155, default=None, blank=True, null=True)
    def __str__(self) -> str:
        return self.andrede_name

class Stadt(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    stadt_name = models.CharField(max_length=155, blank=True, null=True)
    def __str__(self) -> str:
        return self.stadt_name

class Land(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    land_name = models.CharField(max_length=155, blank=True, null=True)
    def __str__(self) -> str:
        return self.land_name
class Company(models.Model):
    company_name = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='images', blank=True, null=True)
    def __str__(self) -> str:
        return self.company_name
    

class Records(models.Model):
    andrede_name = models.ForeignKey(Andrede, on_delete=models.CASCADE, related_name="record_andrede_name", null=True, blank=True)
    first_name = models.CharField(max_length=155, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=155, default=None, blank=True, null=True)
    company_name = models.CharField(max_length=155, default=None, blank=True, null=True)
    email = models.EmailField(null=True, blank=True, default=None)
    news_accept = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20, default=None, blank=True, null=True)
    starBe = models.TextField(default=None, blank=True, null=True)
    nr = models.CharField(max_length=155, blank=True, default=None)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    stadt_name = models.ForeignKey(Stadt, on_delete=models.CASCADE, related_name='record_stadt_name', null=True, blank=True)
    land_name = models.ForeignKey(Land, on_delete=models.CASCADE, related_name="record_land_name", null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True, default=None)
    uid_number = models.CharField(max_length=55, null=True, blank=True)
    ammerkung = models.TextField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.id)
