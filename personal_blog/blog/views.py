from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.core.mail  import send_mail
class BaseView(TemplateView):
    template_name = "base.html"

def sendmail(request):
    send_mail('Liked Site',
    'Someone liked your blog.It is an auto-generated mail',
    'liked@blog.com',
    ["mussalmittu@gmail.com"],
    fail_silently = False,
    )
    return render(request,'mail.html')
def backpage(request):
    return render(request,'base.html')