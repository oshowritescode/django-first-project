from django.shortcuts import render
from .forms import studentRegistration 

def showdataforms(request):
        if request.method == 'POST':
            fm = studentRegistration(request.POST)
            print("validated")
            print("name" . cleaned_data["name"])
        else:
            fm = studentRegistration()
        return render(request, "enroll/studentdetails.html" , {'form' :fm })


 