from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('values', views.values, name='values'),
    path('values/add', views.addValue, name='add-value'),
    path('values/<int:id>/update', views.updateValue, name='update-value'),
    path('values/<int:id>/delete', views.deleteValue, name='delete-value'),
]
