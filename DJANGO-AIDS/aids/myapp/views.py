from django.shortcuts import render
from .forms import ContactForm


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register_view(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():

            user  = form.save()
            login(request, user)
            return redirect('contact')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def contact_view(request):

    if request. method =='POST':

        form = ContactForm(request.POST)
        if form. is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'myapp/thanks.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {'form': form})