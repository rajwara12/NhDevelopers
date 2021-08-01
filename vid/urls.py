from django.urls import path

from . import views

urlpatterns = [
    # <-----Authentication Urls---->
    path('', views.index, name="index"),

    path('handleSignup', views.handleSignup, name="handleSignup"),
    path('handleLogin', views.handleLogin, name="handleLogin"),
    path('handleLogout', views.handleLogout, name="handleLogout"),
    path('<auth_token>', views.verify, name="verify"),
    path('forget_pass/', views.forget_pass, name="forget_pass"),
    path('change_pass/<auth_token>/', views.change_pass, name="change_pass"),
    path('blog/postcomment', views.postcomment, name="postcomment"),
    path('blog/', views.blog, name="blog"),
    path('blog/search', views.search, name="search"),
    path('blog/<int:id>', views.blogpost, name="blogpost"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/det/<int:id>', views.det, name="det"),
    path('dashboard/det/dele/<int:id>', views.dele, name="dele"),
    path('dashboard/det/upd/<int:id>', views.upd, name="upd"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),

]
