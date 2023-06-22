from django.shortcuts import redirect, render
from .forms import StoryForm
from .models import Story
from django.http import HttpResponseRedirect
from django.views.generic import DetailView,UpdateView,DeleteView

# Create your views here.



def add_stories(request):
    form = StoryForm
    if request.method == "POST":
        if form.is_valid:
            title = request.POST.get('title')
            category = request.POST.get('category')
            content = request.POST.get('content')
            story_obj = Story(title = title, category =category,content =content)
            story_obj.author = request.user
            story_obj.save()
            return redirect('/stories')

    return render(request, 'stories.html',{ "form" :form})


def stories(request):
    # 从数据库获取当前登录用户的所有文章
    posts = Story.objects.filter(author =request.user)
    return render(request, 'story_list.html',{ "posts" :posts})

def about(request):
    return render(request, 'about.html')


class StoryUpdateView(UpdateView):
     model = Story
     fields =['category','title','content']
     template_name = 'story_update.html'
     success_url = "/stories"

class StoryDetailView(DetailView):
     model = Story
     fields =['title','content']
     template_name = 'story_detail.html'
     success_url = "/stories"

class StoryDeleteView(DeleteView):
        model = Story
        template_name= 'delete.html'
        success_url = "/stories"