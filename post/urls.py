#Library Import
from django.urls import path
#Local Import
from . import views


app_name='posts'
urlpatterns = [
    path('navbar/', views.Navbar.as_view(), name='navbar'),
    path('', views.HomeView.as_view(), name='home'),
    path("detail-post/<slug:slug>/", views.DetailPostView.as_view(), name="post_detail"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name="category_detail"),
    path('about-us/', views.AboutUsView.as_view(), name="about-us"),
    path('contact-us/', views.ContactUsView.as_view(), name="contact-us"),
]
