from django.shortcuts import render
from django.views.generic import TemplateView

def post_list(request):
    return render(request, 'blog/post_list.html', {})