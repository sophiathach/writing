from django.shortcuts import render
#import the time
from django.utils import timezone
#import the Post class 
from .models import Post

# Create your views here.
def post_list(request):
	#order the list by date
	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

