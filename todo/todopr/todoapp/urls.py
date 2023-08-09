from . import views
from django.urls import path
app_name='todoapp'
urlpatterns=[
    path('',views.add,name='add'),
    path('delete/<int:todoid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('home/',views.tasklistiew.as_view(),name='home'),
    path('ldetail/<int:pk>/',views.taskdetailview.as_view(),name='ldetail'),
    path('lupdate/<int:pk>/', views.taskupdateview.as_view(),name='lupdate'),
    path('ldelete/<int:pk>/',views.taskdeleteview.as_view(),name='ldelete'),
]