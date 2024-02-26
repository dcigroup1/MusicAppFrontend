from django.urls import path
from .views import HomePageView, BaseRecordView, DetailRecordView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('records/', BaseRecordView.as_view(), name='records'),
    path('records/<int:pk>/', DetailRecordView.as_view(), name='record_detail'),

]
