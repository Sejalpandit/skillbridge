from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Internship, Application
from django.contrib.auth.models import User

def internship_list(request):
    query = request.GET.get('q')

    if query:
        internships = Internship.objects.filter(title__icontains=query)
    else:
        internships = Internship.objects.all()

    applied_ids = []

    if request.user.is_authenticated:
        applied_ids = Application.objects.filter(
            user=request.user
        ).values_list('internship_id', flat=True)

    return render(request, 'internships.html', {
        'internships': internships,
        'applied_ids': applied_ids
    })

@login_required
def apply_internship(request, id):
    user = request.user
    internship = Internship.objects.get(id=id)

    already_applied = Application.objects.filter(
        user=user,
        internship=internship
    ).exists()

    if not already_applied:
        Application.objects.create(user=user, internship=internship)

    return redirect('/')

@login_required
def my_applications(request):
    user = request.user
    applications = Application.objects.filter(user=user)

    return render(request, 'my_applications.html', {'applications': applications})