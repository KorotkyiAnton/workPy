from django.urls import path
from . import views

urlpatterns = [
    path('bp_crm/', views.get_all_users_data, name='bp_crm'),
]
