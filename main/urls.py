from django.urls import path
from main.views import IndexView, AddNewJobView,ListAllJobs

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new/', AddNewJobView.as_view(), name='new'),
    path('jobs/', ListAllJobs.as_view(), name='jobs')
]