from django.urls import path
from.import views

urlpatterns = [
	path('',views.index,name='index'),
	path('hr',views.hr,name='hr'),
	path('candidate',views.candidate,name='candidate'),

]