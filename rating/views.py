# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.template import Context,loader
from rating.models import Images
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponse("Hello World")

def transaction(request):
    latest_image_list = Images.objects.get(id=1)
    t=loader.get_template('rating/transaction.html')
#    c=Context({'image_path':latest_image_list})
    c=Context({})
    return HttpResponse(t.render(c))

def content(request):
    latest_image_list=Images.objects.get(id=1)
    t=loader.get_template('rating/transaction_files/content.html')
    c=Context({'image_path':latest_image_list})
    return HttpResponse(t.render(c))

def menu(request):
    t=loader.get_template('rating/transaction_files/menu_1.html') 
    c=Context({})
    return HttpResponse(t.render(c))

@csrf_exempt
def rating(request):
    #p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice=request.POST['rating']
    except(KeyError, selected.DoesNotExist):    
        print("Not good")
    else:  
        image=Images.objects.get(id=1) 
        image.rating=(image.rating+float(selected_choice))/2
        image.save()
        return HttpResponseRedirect(reverse('rating.views.content'))    

#it should be fine ...its just access to his os
#yes
