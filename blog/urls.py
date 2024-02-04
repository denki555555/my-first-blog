from django.urls import path
from .import views

urlpatterns=[
    # Djangoがビューを見つけるとき、http://127.0.0.1:8000にアクセスがあったら、
    # views.post_list にリダイレクトさせるための設定
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]
