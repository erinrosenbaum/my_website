from django.urls import path

from . import views

urlpatterns = [
    path('', views.DiscussionListView.as_view(), name='discussion_list'),
    path('<int:pk>/edit/', views.DiscussionUpdateView.as_view(), name='discussion_edit'),
    path('<int:pk>/', views.DiscussionDetailView.as_view(), name='discussion_detail'),
    path('new/', views.DiscussionCreateView.as_view(), name='discussion_new'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_new'),
    path('<int:pk>/delete/', views.DiscussionDeleteView.as_view(), name='discussion_delete'),
    path('<int:pk>/comment/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
