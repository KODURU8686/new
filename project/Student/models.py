from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractUser):
	img= models.ImageField(upload_to='Profiles/',default="profile.png")
	dob=models.DateField(null=True,blank=True)
	organization_name=models.CharField(max_length=120,blank=True,null=True)
	hospital_name=models.CharField(max_length=120,blank=True,null=True)
	g=[('Male','Male'),('Female','Female')]
	gender=models.CharField(max_length=10,choices=g,null=True,blank=True)
	ph_no=models.CharField(max_length=10)
	pan_no=models.CharField(max_length=10,null=True,blank=True)
	address=models.CharField(max_length=100)
	postal_code=models.CharField(max_length=7)
	city=models.CharField(max_length=20)
	state=models.CharField(max_length=20,default='Andra Pradesh')
	country=models.CharField(max_length=20,default='India')
	p=[(1,'Medicinist'),(2,'Organisation'),(3,'Guest')]
	role=models.IntegerField(choices=p,default=3)

class Rolrq(models.Model):
	r = [(1,'Medicinist'),(2,'Organisation')]
	uname = models.CharField(max_length=50)
	roltype = models.IntegerField(choices=r,default=0)
	prf = models.ImageField(upload_to='RolesRequested/')
	is_checked = models.BooleanField(default=0)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)

class Orgdetails(models.Model):
	org_name=models.CharField(max_length=50,default="Organisation Name")
	found_name=models.CharField(max_length=50,default="Founder Name")
	est_date=models.DateField(null=True)
	us=models.OneToOneField(User,on_delete=models.CASCADE)

class MedicineInfo(models.Model):
	#organization_name=models.CharField(max_length=120,default="ngo")
	pharmacy_name=models.CharField(max_length=500)
	medicine_name=models.CharField(max_length=120)
	quantity=models.CharField(max_length=30)
	batch_no=models.IntegerField(unique=True,null=True)
	category=models.CharField(max_length=120)
	production_date=models.DateField(null=True)
	entry_date=models.DateField(null=True)
	expiry_date=models.DateField(null=True)
	created_date=models.DateField(auto_now=True)
	uid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	impf=models.ImageField(upload_to='Medicines/',default="ngo1.jpg")

class DonationInfo(models.Model):
	username=models.CharField(max_length=120)
	quantity=models.CharField(max_length=30)
	medicine_name=models.CharField(max_length=120)
	pharmacy_name=models.CharField(max_length=500)
	org_name=models.CharField(max_length=120)
	total_tablets=models.IntegerField(blank=True,null=True)
	donated_tablets=models.IntegerField(blank=True,null=True)
	remaining_tablets=models.IntegerField(null=True)
	days_count=models.DateField(blank=True,null=True)
	created_date=models.DateField(auto_now=True)
	required_tablets=models.IntegerField(blank=True,null=True)
	donated_date=models.DateField(blank=True,null=True)
	pid=models.ForeignKey(MedicineInfo,on_delete=models.CASCADE,null=True)

class ServiceBox(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	change_role=models.CharField(max_length=1000)
	impf=models.ImageField(upload_to='Medicines/',default="ngo1.jpg")

class Export(models.Model):
	is_medicinist = models.BooleanField(default=False)
	#age = models.IntegerField(default=10)
	u = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		Export.objects.create(u=instance)
