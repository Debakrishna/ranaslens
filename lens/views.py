from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from .models import QueryForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def portfolio(request):
    query_set = Image.objects.all()
    return render(request, "portfolio.html", {'query_set': query_set})

def contact(request):

    service_choice  = QueryForm.SERVICE_CHOICES
    reference_choice  = QueryForm.REFERENCE_CHOICE

    # getting the user inputs
    
    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email_id = request.POST["email_id"]
        phone_no = request.POST["phone_no"]
        service = request.POST.get('services')
        reference = request.POST.get('found_us')
        message = request.POST["message"] 

        query = QueryForm(first_name=first_name, last_name=last_name,email_id=email_id, phone_no=phone_no, service=service, reference=reference, message=message)
        query.save()
        messages.success(request, 'Your message sent successfully ! 🚀')
        messages.add_message(request, messages.INFO,
                                 'Thanks for reaching out! We will be in contact soon!',
                                 extra_tags='ex-tag')
        return HttpResponseRedirect("/contact/")
    return render(request, "contact.html", {"service_choice" : service_choice, "reference_choice": reference_choice})


def handling404(request, exception):
    return render(request, "404.html", {})