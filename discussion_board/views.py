from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from . import models

class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = models.Discussion
    template_name = 'discussion_board/discussion_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DiscussionListView(LoginRequiredMixin, ListView):
    model = models.Discussion
    template_name = 'discussion_board/discussion_list.html'
    login_url = 'login'

class DiscussionDetailView(LoginRequiredMixin, DetailView):
    model = models.Discussion
    template_name = 'discussion_board/discussion_detail.html'
    login_url = 'login'

class DiscussionUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Discussion
    fields = ['title', 'body']
    template_name = 'discussion_board/discussion_edit.html'
    login_url = 'login'

class DiscussionDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Discussion
    template_name = 'discussion_board/discussion_delete.html'
    success_url = reverse_lazy('discussion_list')
    login_url = 'login'

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Comment
    template_name = 'discussion_board/comment_delete.html'
    success_url = reverse_lazy('discussion_list')
    login_url = 'login'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = 'discussion_board/comment_new.html'
    fields = ['comment']
    #success_url = reverse_lazy('article_detail')
    login_url = 'login'

    def form_valid(self, form):
        # print(self)
        # print(self.request)
        # print(form)
        form.instance.author = self.request.user
        form.instance.discussion_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          discussion_id=self.kwargs['pk']
          return reverse_lazy('discussion_detail', kwargs={'pk': discussion_id})
