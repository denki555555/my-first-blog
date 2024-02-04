from django.urls import path
from .import views

urlpatterns=[
    # Djangoがビューを見つけるとき、http://127.0.0.1:8000にアクセスがあったら、
    # views.post_list にリダイレクトさせるための設定
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail')
]
