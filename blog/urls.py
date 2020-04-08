from django.urls import  path
from blog import views


urlpatterns=[
    path('',views.postListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.postDetailView.as_view(),name='post_detail'),
    path('about/',views.aboutView.as_view(),name='about'),
    path('post/new',views.createPostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',views.postUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove',views.postDeleteView.as_view(),name='post_remove'),
    path('drafts',views.draftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.comment_approved,name='comment_approve'),
    path('comment/<int:pk>/remove',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish',views.post_publish,name='post_publish'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
]