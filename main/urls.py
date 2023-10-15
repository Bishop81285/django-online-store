from django.urls import path

from main.views import contacts, ProductListView, ProductDetailView, BlogPostListView, BlogPostCreateView, \
    BlogPostDetailView, BlogPostDeleteView, BlogPostUpdateView

app_name = 'main'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blogpost/', BlogPostListView.as_view(), name='blogpost-list'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
]
