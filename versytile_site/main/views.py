from django.shortcuts import render
from django.http import HttpResponse
from .models import Forum, Discussion


# Create your views here.
def homepage(request):

    matching_Forum = Forum.objects.all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_Forum}
    )


def a_forum(request, a_forum: str):

    matching_Forum = Discussion.objects.filter(a_forum__slug=a_forum).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_Forum}
    )

def discuss(request, a_forum: str, discuss:str):

    matching_discuss = Discussion.objects.filter(a_forum__slug=a_forum, Discussion_slug=discuss ).first()
    
    return render(
        request=request,
        template_name='main/discuss.html',
        context={"object": matching_discuss}
    )