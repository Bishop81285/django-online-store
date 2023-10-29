from django.urls import path

from main.views import contacts, ProductListView, ProductDetailView, BlogPostListView, BlogPostCreateView, \
    BlogPostDetailView, BlogPostDeleteView, BlogPostUpdateView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionCreateView

app_name = 'main'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('blogpost/', BlogPostListView.as_view(), name='blogpost-list'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
    path('product/<int:pk>/add-version/', VersionCreateView.as_view(), name='version-create'),
]
