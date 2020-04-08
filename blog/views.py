from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DeleteView,CreateView,UpdateView,DetailView)
from blog.models import Post,Comments
from django.utils import  timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import postForm,commentForm
from  django.urls import reverse_lazy,reverse



# Create your views here.
class aboutView(TemplateView):
    template_name = 'about.html'

class postListView(ListView):
    context_object_name = 'post_list'
    model = Post


#below method helps to recreate an sql like statement
#sql = select * from Postwhere published_Date<=sysdate order by published_date desc
#published_date__lte here __lte refers to less than equal to and '-' in ('-publised_date')refers to desc,
#if no '-' it will be asc

    #def get_queryset() will override ListViews get_queryset() method and will display filetered values:
    #https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/    dynamic filtering
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        # return  Post.objects.filter(title='Happy')

class postDetailView(DetailView):
    model = Post

#LoginRequiredMixin for login features
class createPostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = postForm
    model = Post


class postUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = postForm
    model = Post

class postDeleteView(LoginRequiredMixin , DeleteView):

    model = Post
    #reverse lazy wont erdirect to another page unless its actually deleted
    success_url = reverse_lazy('post_list')


class draftListView(LoginRequiredMixin,ListView):
    context_object_name = 'draft_posts'
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    template_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

class ThanksPage(TemplateView):
    template_name = 'blog/thanks.html'
#############################################################################
#############################################################################
@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if(request.method=='POST'):
        form = commentForm(request.POST)

        if(form.is_valid()):
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=commentForm()
        return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approved(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comments,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)




