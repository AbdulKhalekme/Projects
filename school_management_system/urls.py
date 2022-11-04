"""student_management_system URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from school_management_app import views, HoDviews, StaffViews, StudentViews
from school_management_system import settings

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',HoDviews.admin_home,name="admin_home"),
    path('add_staff',HoDviews.add_staff,name="add_staff"),
    path('add_staff_save',HoDviews.add_staff_save,name="add_staff_save"),
    path('add_course', HoDviews.add_course,name="add_course"),
    path('add_course_save',HoDviews.add_course_save,name="add_course_save"),
    path('add_student', HoDviews.add_student,name="add_student"),
    path('add_student_save', HoDviews.add_student_save,name="add_student_save"),
    path('add_subject', HoDviews.add_subject,name="add_subject"),
    path('add_subject_save', HoDviews.add_subject_save,name="add_subject_save"),
    path('manage_staff', HoDviews.manage_staff,name="manage_staff"),
    path('manage_student', HoDviews.manage_student,name="manage_student"),
    path('manage_course', HoDviews.manage_course,name="manage_course"),
    path('manage_subject', HoDviews.manage_subject,name="manage_subject"),
    path('edit_staff/<str:staff_id>', HoDviews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HoDviews.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', HoDviews.edit_student,name="edit_student"),
    path('edit_student_save', HoDviews.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', HoDviews.edit_subject,name="edit_subject"),
    path('edit_subject_save', HoDviews.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>', HoDviews.edit_course,name="edit_course"),
    path('edit_course_save', HoDviews.edit_course_save,name="edit_course_save"),
#     Staff URL Path
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('student_home', StudentViews.student_home, name="student_home"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)