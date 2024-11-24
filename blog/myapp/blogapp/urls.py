from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.login_view,name='login'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_views,name='logout'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('user/<str:username>/', views.post_list_by_user, name='posts_by_user'),

]