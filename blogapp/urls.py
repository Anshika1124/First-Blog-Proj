from django.urls import path,include
from . import views
from django.shortcuts import redirect


urlpatterns = [
	path('signup/', views.signup, name='signup'),
    path('loginn/', views.loginn, name='loginn'),
    path('base/', views.base, name='base'),
    path('newpost/', views.newPost, name='new-post'),
    path('mypost/', views.myPost, name='my-post'),
    path('logout/', views.signout, name='signout'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('mypost/<int:pk>/', views.my_post, name='mypost_detail'),
    path('my-post/<int:pk>/', views.my_post, name='mypost'),
	path('', lambda request: redirect('/base/'), name='redirect-to-base'),  
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('', views.home, name='home'),
	path('authors/',views.author_list,name='author_list'),
	path('author/new/',views.author_create,name='author_create'),
	path('author/<int:pk>/',views.author_detail,name='author_detail'),
	path('author/<int:pk>/edit/',views.author_update,name='author_update'),
	path('author/<int:pk>/delete/',views.author_delete,name='author_delete'),
]



