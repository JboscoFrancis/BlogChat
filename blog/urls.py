from django.urls import path
from . import views

#urls for blog app
urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register' ),
    path('profile/', views.profile, name = 'profile' ),
    path('update_profile/', views.update_profile, name = 'update_profile' ),
    path('login/', views.userlogin, name = 'login' ),
    path('logout/', views.userlogout, name = 'logout'),
    path('create/', views.createpost, name = 'create'),
    path('detail/<str:pk>', views.postdetail, name = 'detail'),
    path('update/<str:pk>', views.updatepost, name = 'update'),
    path('delete_post/<str:pk>', views.delete_post, name = 'delete_post'),
    path('delete_comment/<str:pk>', views.delete_reply, name = 'delete_reply'),
]
