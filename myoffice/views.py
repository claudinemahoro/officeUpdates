from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Department,Profile,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
  departments = Department.get_all_departments()
  return render(request, 'index.html',{"departments":departments})

def profile(request, username):
  return render(request, 'profile.html')

def my_office(request, id):
  title = "My office"
  department = Department.objects.get(id=id)

  return render(request, 'office.html', {'title':title,'department':department})

def join(request, id):
  current_user = request.user
  department = Department.objects.get(id=id)
  department.employees_count.add(current_user)
  department.save()
  return redirect("office")

@login_required(login_url='/accounts/login/')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewPostForm(request.POST, request.FILES)
    if form.is_valid():
       post = form.save(commit=False)
       post.profile = current_user
       post.save()
    return redirect('index')
  else:
    form = NewPostForm()
  return render(request, 'new_post.html', {"form": form})
