from .models import Post
from django.shortcuts import render
from django.utils import timezone

def post_list(request):
	Post.objects.all().order_by('-published_date')
	return render(request, 'blog/post_list.html', {})
