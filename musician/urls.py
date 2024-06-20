
from django.urls import path
from .import views
urlpatterns = [
    
    path('add/',views.add_musician,name='musicianpage'),
    path('edit/<int:id>',views.musician_edit,name='musician_edit')
    
]
