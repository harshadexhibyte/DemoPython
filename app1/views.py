from django.shortcuts import render,redirect
from django.conf import settings
import datetime
from .models import adminUser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from django.http import HttpResponse


def index(request):
	return render(request,'index.html')
def Dashboard(request):
	if request.method=="POST":
		admin_email=request.POST['admin_email']
		admin_password=request.POST['admin_password']
		print(admin_email,admin_password)
		try:
			admin_user=adminUser.objects.get(email='harshad05.exhibyte@gmail.com',password='123')
			request.session['admin_email']=admin_user.email
			return render(request,'Dashboard.html')
		except Exception as e:
			print(e)
			FailedMsg="Encorect Email or Password"
			return render(request,'index.html',{'FailedMsg':FailedMsg})
	else:
		return redirect('index')

def fileUploded(request):
	if request.method=="POST":
		file = request.FILES['uplodedFile']
		data = pd.read_excel(file)
		print(data.columns);
		data.plot(x="COL1", y=["COL2","COL3"])
		plt.show()
		return render(request,'Dashboard.html')
	else:
		return render(request,'Dashboard.html')
	