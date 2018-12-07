from django.shortcuts import render, get_list_or_404
from .lib.data_process import process_resume_data
from home.models import User
from django.shortcuts import HttpResponse

def home_view(request):
    return render(request, 'home/index.html')

def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            new_user.save()
            return render(request, 'home/index.html')
        else:
            return HttpResponse("<h1>Please same enter the same password for password and confirm password</h1>")

def login_view(request):
    if request.method == "POST":
        user_name = request.POST.get('login_email')
        password = request.POST.get('login_password')
        user = get_list_or_404(User, email=user_name)
        return render(request, 'home/resume.html')

def result_view(request):
    if request.method == "POST":
        resume = {
            "education": request.POST.get("education"),
            "work_experience": request.POST.get("work_experience"),
            "areas_of_interest": request.POST.get("areas_of_interest"),
            "projects": request.POST.get("projects"),
            "technical_skills": request.POST.get("technical_skills"),
            "publications": request.POST.get("publications"),
            "technical_events": request.POST.get("technical_events"),
            "extra_curricular_activities": request.POST.get("extra_curricular_activities"),
            "personal_info": request.POST.get("personal_info")
        }
        result = process_resume_data(resume)
        return render(request, 'home/result.html', 
                        {"result_1": result[0], "result_2": result[1], "result_3": result[2]})
    