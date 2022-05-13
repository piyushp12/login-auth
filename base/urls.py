from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='home'),
    path('Doctor/',views.Doctor,name='Doctor'),
    path('Patient/',views.Patient,name='Patient')
    
]
