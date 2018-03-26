from django.urls import path
from blog.api import views


urlpatterns = [
	# path('category/create/', views.CategoryCreateAPIView().as_view(), name='category_create_list'),
	# path('category/update/<uuid:uuid>/', views.CategoryUpdateAPIView().as_view(), name='category_update'),
	# path('category/detail/<uuid:uuid>/', views.CategoryRetrieveAPIView().as_view(), name='category_detail'),
	path('category/', views.CategoryCreateListAPIView().as_view(), name='category'),
    path('post/create/', views.PostCreateAPIView().as_view(), name='post_create'),
    path('post/update/<uuid:uuid>/', views.PostUpdateAPIView().as_view(), name='post_update'),
    path('post/', views.PostListAPIView().as_view(), name='post'),
	path('tag/create/', views.TagCreateAPIView().as_view(), name='tag_create'),
    path('tag/update/<uuid:uuid>/', views.TagUpdateAPIView().as_view(), name='tag_update'),
    path('tag/', views.TagListAPIView().as_view(), name='tag'),
]
