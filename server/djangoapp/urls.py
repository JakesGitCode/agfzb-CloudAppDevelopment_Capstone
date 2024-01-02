from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contact/', views.contact, name='contact'),

    # path for registration
    path('registration/', views.registration_request, name='registration'),

    # path for login
    path('login/', views.login_request, name='login'),

    # path for logout
    path('logout/', views.logout_request, name='logout'),

    # path for the index view
    path('', views.get_dealerships, name='index'),

    # path for dealer details view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # path for add a review view
    path('add_review/<int:dealer_id>/', views.add_review, name='add_review'),

    # path for the home view (can be updated based on your actual home page)
    path('home/', views.get_dealerships, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
