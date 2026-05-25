from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'chatapp/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)           # auto login after register
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'chatapp/register.html', {'form': form})

@login_required
def room(request, room_name):
    return render(request, 'chatapp/room.html', {'room_name': room_name})