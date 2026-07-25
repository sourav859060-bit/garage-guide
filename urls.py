"""garageguide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('loginn', views.loginn),
    path('loginn_buttonsumit', views.loginn_buttonsumit),
    path('admin_home', views.admin_home),
    path('Add_service', views.Add_service),
    path('Add_service_buttonsumit', views.Add_service_buttonsumit),
    path('view_serviceadmin', views.view_serviceadmin),
    path('edit_service/<id>',views.edit_service),
    path('edit_service_post/<id>',views.edit_service_post),
    path('delete_service/<id>',views.delete_service),
    path('complaints', views.complaints),
    path('reply_complaint/<id>', views.reply_complaint),
    path('reply_complaint_post/<id>', views.reply_complaint_post),
    path('varify_worker', views.varify_worker),
    path('approved_admin_worker/<id>', views.approved_admin_worker),
    path('reject_admin_worker/<id>', views.reject_admin_worker),
    path('approved_worker', views.approved_worker),
    path('Rating', views.Rating),
    path('change_password', views.change_password),
    path('change_password_post', views.change_password_post),
    path('Approved_booking',views.Approved_booking),
    path('blocked_worker/<id>',views.blocked_worker),
    path('unblocked_worker/<id>',views.unblocked_worker),
    path('view_user', views.view_user),




#################### worker


    path('worker_home', views.worker_home),
    path('Register', views.Register),
    path('Register_post', views.Register_post),
    path('change_passwordworker', views.change_passwordworker),
    path('change_passwordworker_post', views.change_passwordworker_post),
    path('view_profile', views.view_profile),
    path('Edit_profile/<id>', views.Edit_profile),
    path('Edit_profile_post/<id>', views.Edit_profile_post),
    path('view_serviceworker', views.view_serviceworker),
    path('Own_service_manage', views.Own_service_manage),
    path('Add_own_service/<id>', views.Add_own_service),
    path('ADD_own_service_post/<id>', views.ADD_own_service_post),
    path('Edit_own_service/<id>', views.Edit_own_service),
    path('Edit_own_service_post/<id>', views.Edit_own_service_post),
    path('manage_schedule',views.manage_schedule),
    path('Add_schedule', views.Add_schedule),
    path('add_schedule_post', views.add_schedule_post),
    path('Edit_schedule/<id>', views.Edit_schedule),
    path('Edit_schedule_post/<id>', views.Edit_schedule_post),
    path('varify_booking', views.varify_booking),
    path('approved_booking/<id>',views.approved_booking),
    path('reject/<id>',views.reject),
    path('view_booking', views.view_booking),
    path('Update_worke_status/<id>',views.Update_worke_status),
    path('view_payments',views.view_payments),
    path('View_Rating',views.View_Rating),
    path('Own_service/<id>',views.Own_service),
    path('Own_service_post/<id>',views.Own_service_post),



   ################user

    path('Uesr_home', views.Uesr_home),
    path('UserReeister',views.UserReeister),
    path('UserRegister_post', views.UserRegister_post),
    path('Change_passworduser',views.Change_passworduser),
    path('change_passworduser_post', views.change_passworduser_post),
    path('View_worker',views.View_worker),
    path('View_schedule',views.View_schedule),
    path('View_service/<id>',views.View_service),
    path('add_booking/<id>', views.add_booking),
    path('Add_rating/<id>',views.Add_rating),
    path('View_ratinguser',views.View_ratinguser),
    path('Make_payment/<id>/<price>',views.Make_payment),
    path('make_payment_post/<id>',views.make_payment_post),
    path("payment_success",views.payment_success),
    path('default',views.default),
    path('View_payment_history',views.View_payment_history),
    path('view_replycomplain',views.view_replycomplain),
    path('send_complaint',views.send_complaint),
    path('send_complaint_post',views.send_complaint_post),
    path('View_service_status',views.View_service_status),
    path('add_rating_post/<id>',views.add_rating_post),
    path('Booking_status',views.Booking_status),
    path('',views.abc),


]
#