from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from . import models

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    template_name = 'articles/article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'articles/article_edit.html'
    login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Comment
    template_name = 'articles/comment_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'articles/comment_new.html'
    fields = ['comment']
    #success_url = reverse_lazy('article_detail')
    login_url = 'login'

    def form_valid(self, form):
        # print(self)
        # print(self.request)
        # print(form)
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          article_id=self.kwargs['pk']
          return reverse_lazy('article_detail', kwargs={'pk': article_id})
