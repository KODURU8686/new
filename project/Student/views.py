from django.shortcuts import render,redirect
from Student.forms import UsrReg,ChpwdForm,Medform,ServiceForm,RequestForm,PrfUpd,RolerqForm,GvForm,OrgForm
from django.contrib import messages
from Student.models import MedicineInfo,User,DonationInfo,Rolrq,Orgdetails
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from Project import settings
from datetime import date
from django.http import HttpResponseRedirect

# Create your views here.
def management(request):
	return render(request,'htfiles/management.html')

def HomePage(rt):
	return render(rt,'htfiles/HomePage.html')


def about(request):
	return render(request,'htfiles/about.html')

def mainpage(request):
	return render(request,'htfiles/mainpage.html')	

def registration1(fh):
	if fh.method=="POST":
		k=UsrReg(fh.POST)
		if k.is_valid():
			e=k.save(commit=False)
			sb="Testing email for Donation"
			mg="Hi welcome {}. You have successfully registered for Donation portal.".format(e.username)
			sd=settings.EMAIL_HOST_USER
			snt=send_mail(sb,mg,sd,[e.email])
			if snt == 1:
				e.save()
				return redirect('/login')
			else:
				return redirect('/')
			# messages.success(fh,"You have registered successfully")
			#return redirect('/login')
	k=UsrReg()
	return render(fh,'htfiles/register.html',{'t':k})


@login_required
def cgf(request):
	if request.method=="POST":
		print("Yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/login')
	c=ChpwdForm(user=request)
	return render(request,'htfiles/passwordchange.html',{'g':c})

def role(request):
	return render(request,'htfiles/role.html')

def rolereq(request):
	if request.method == "POST":
		m = RolerqForm(request.POST,request.FILES)
		if m.is_valid():
			z=m.save(commit=False)
			z.ud_id = request.user.id
			z.save()
			return redirect('/main')
	m = RolerqForm()
	return render(request,'htfiles/rolereq.html',{'n':m})

def userpage(request):
	if request.method=="POST":
		p=Medform(request.POST)
		if p.is_valid():
			k = p.save(commit=False)
			k.uid_id = request.user.id
			k.save()
			return redirect('/tb')
	p=Medform()
	return render(request,'htfiles/userpage.html',{'h':p})

def profile(request):
	return render(request,'htfiles/profile.html')

def updpfle(request):
	f = User.objects.get(id=request.user.id)
	v = Orgdetails.objects.get(us_id=request.user.id)
	if request.method == "POST":
		z = PrfUpd(request.POST,request.FILES,instance=f)
		s = OrgForm(request.POST,instance=v)
		if z.is_valid() or s.is_valid():
			z.save()
			s.save()
			return redirect('/pfe')
	z = PrfUpd(instance=f)
	s = OrgForm(instance=v)
	return render(request,'htfiles/updpfle.html',{'x':z,'k':s})

def dnrpfle(request):
	f = User.objects.get(id=request.user.id)
	if request.method == "POST":
		z = PrfUpd(request.POST,request.FILES,instance=f)
		if z.is_valid():
			z.save()
			return redirect('/pfe')
	z = PrfUpd(instance=f)
	return render(request,'htfiles/dnrpfle.html',{'x':z})

def orgform(request):
	if request.method == "POST":
		k = OrgForm(request.POST)
		if k.is_valid():
			n = k.save(commit=False)
			n.us_id = request.user.id
			n.save()
			return redirect('/pfe')
	k = OrgForm()
	return render(request,'htfiles/orgentry.html',{'g':k})

def crud(request):
	if request.method=="POST":
		un=request.POST['name']
		pas=request.POST['pwd']
		em=request.POST['eml']
		Age=request.POST['age']
		#data2=UsrRg.objects.all()
		if len(un)!=0:
			data=MedicineInfo.objects.create(Username=un,password=pas,email=em,age=Age)
		#return render(request,'html/actions.html',{'info':data2})
	data2=MedicineInfo.objects.all()
	return render(request,'htfiles/crud.html',{'info':data2})

def deletedata(req,id):
	print("1")
	data=MedicineInfo.objects.get(id=id)
	data.delete()
	print("2")
	return redirect('/cr')

def tab(hj):
	data=MedicineInfo.objects.filter(uid_id=hj.user.id)
	return render(hj,'htfiles/table.html',{'info':data})

def delete(red,id):
	data=MedicineInfo.objects.get(id=id)
	if red.method=="POST":
		data.delete()
		return redirect('/tb')
	return render(red,'htfiles/userdelete.html',{'sd':data})

def userupdate(up,si):
	a=MedicineInfo.objects.get(id=si)
	#y=NewData.objects.get(pid_id=si)
	if up.method=="POST":
		d=Medform(up.POST,instance=a)
		#k=NewUsrForm(up.POST,instance=y)
		if d.is_valid():
			d.save()
			#k.save()
			return redirect('/tb')
	d=Medform(instance=a)
	#k=NewUsrForm(instance=y)
	return render(up,'htfiles/updateuser.html',{'us':d})

def view(request):
	return render(request,'htfiles/view.html')


def gvper(request):
	m = User.objects.all()
	n = Rolrq.objects.all()
	p,s = [],{}
	for i in m:
		p.append(i.id)
	for j in m:
		if j.id not in p or j.is_superuser:
			continue
		else:
			q = Rolrq.objects.get(ud_id=j.id)
			s[j.id] = j.username,q.roltype,q.prf,j.role,j.id
	return render(request,'htfiles/giveperm.html',{'v':s.values()})

def aprvrl(request,t):
	s = User.objects.get(id=t)
	h = Rolrq.objects.get(ud_id=t)
	if request.method == "POST":
		y = GvForm(request.POST,instance=s)
		if y.is_valid():
			h.is_checked = 1
			h.save()
			y.save()
			return redirect('/gvperm')
	y = GvForm(instance=s)
	return render(request,'htfiles/aprorl.html',{'a':y})


def peruser(request):
	ty=User.objects.all()
	return render(request,'htfiles/peruser.html',{'q':ty})

def index1(request):
	i = MedicineInfo.objects.filter(uid_id=request.user.id)
	g = MedicineInfo.objects.all()
	#l=DonationInfo.objects.all()
	k = {}
	for m in g:
		days_count=m.expiry_date-m.created_date

		print(days_count,m.expiry_date,m.created_date)
		#s = User.objects.get(id=m.uid_id)
		k[m.id] = m.id,m.pharmacy_name,m.medicine_name,m.quantity,m.batch_no,m.category,m.production_date,m.entry_date,m.expiry_date,days_count
	print(k)

	# for i in l:
	# 			remaining_tablets=l.quantity - l.donated_tablets
	# 			print(remaining_tablets)
	# 			k[l.id] = l.id,l.remaining_tablets
	# b=l.values()
	f = k.values()
	return render(request,'htfiles/index.html',{'it':i,'d':f})


def requ(request):
	#l=DonationInfo.objects.all()
	if request.method=="POST":
		g=RequestForm(request.POST)
		if g.is_valid():
			g.save()
	g=RequestForm()
	return render(request,'htfiles/request.html',{'r':g})		

def search(request):
	if request.method=="POST":
		searched=request.POST['searched']
		ven=MedicineInfo.objects.filter(medicine_name__contains=searched)
		
		return render(request,'htfiles/searchbar.html',{'searched':searched,'Med':ven})

	else:
		return render('htfiles/searchbar.html')


