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
    path('post/<int:pk>/', views.my_post, name='mypost_detail'),
    path('my-post/<int:pk>/', views.my_post, name='mypost'),
	path('', lambda request: redirect('/loginn/'), name='redirect-to-login'),  
    path('auth/', include('django.contrib.auth.urls')), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]



