from django.urls import path
from memory import views

app_name = 'memory'

urlpatterns = [
    path('',views.MemoryListView.as_view(),name='home'),
    path('create/',views.MemoryCreateView.as_view(),name='create'),
    path('delete/<int:pk>/',views.MemoryDeleteView.as_view(),name='delete'),
    path('edit/<int:pk>/',views.MemoryEditView.as_view(),name='edit'),
]
