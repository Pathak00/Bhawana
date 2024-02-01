
from django.urls import path
from . import views
from .views import rang, webpage, contact

urlpatterns = [
    # path('',views.greet,name="home"),
    path('',views.webpage),
    path('contact.html',views.contact),
    path('webpage.html',views.webpage),
    # path('rang.html',views.rang),
    # path('aakash.html',views.aakash),
    path('poem/<int:pk>/', rang, name='rang'), 
    path('poem/<int:pk>/', webpage, name='webpage'), 
    path('webpage/', webpage, name='webpage'),
    path('contact/', contact, name='contact'),
    # path('poem/<int:pk>/', contact, name='contact'), 
    # path('random-poem/', random_poem_view, name='random_poem'),
    # path('poem/<int:pk>/webpage/', lambda request, pk: rang(request, pk, return_webpage=True), name='rang_to_webpage'),
    # path('poem/<int:pk>/webpage.html',views.webpage,name='webpage')
]