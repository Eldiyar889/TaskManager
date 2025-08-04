from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),
    path('projects/', include('projects.urls')),
]