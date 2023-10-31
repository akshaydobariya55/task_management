from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('developer_home/',views.developer_home,name='developer_home'),
    path('manager_home/',views.manager_home,name='manager_home'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('add_project/',views.add_project,name='add_project'),
    path('add_task/',views.add_task,name='add_task'),
    path('delete/<int:id>/',views.projectdeleteview.as_view(),name="deletedata"),
    path('delete_task/<int:id>/',views.taskdeleteview.as_view(),name="deletetask"),
]
