#Library Import
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.translation import gettext as _

from django.utils import translation

from django.core.paginator import Paginator
#Local Import
from .models import Post, Category
from management.models import Settings


class Navbar(View):
    def get(self, request):
        categories = Category.objects.filter(is_sub=False)
        return render(request, 'inc/navbar.html', {'categories':categories})


class HomeView(View):
    def get(self, request):
        posts = Post.objects.filter(status='p').order_by('-created')[:5]
        settings = Settings.objects.first()
        post_services = Post.objects.filter(vip=True)

        context = {'posts':posts, 'settings':settings, 'post_services':post_services}
        return render(request, 'home.html', context)


class DetailPostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'post/post_detail.html', {'post':post})


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post/post-list.html', {'posts':page_obj})


class CategoryDetailView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        return render(request, 'post/category_detail.html', {'category':category})


class AboutUsView(View):
    def get(self, request):
        settings = Settings.objects.first()
        return render(request, 'about_us.html', {'settings':settings})


class ContactUsView(View):
    def get(self, request):
        settings = Settings.objects.first()
        return render(request, 'contact_us.html', {'settings':settings})


# class ChangeLanguage(View):
#     def get(self, request):
#         activate(request.GET.get('lang'))
#         return redirect(request.GET.get('next'))


# def selectlanguage(request):
#     cur_language = translation.get_language()
#     lasturl= request.META.get('HTTP_REFERER')
#     lang = request.POST['language']
#     translation.activate(lang)
#     request.session[translation.LANGUAGE_SESSION_KEY]=lang
#     #return HttpResponse(lang)
#     return HttpResponseRedirect("/"+lang)


def change_lang(request):
    activate(request.GET.get('lang'))
    return redirect(request.GET.get('next'))