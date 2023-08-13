from django.urls import path

from .import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('contact/', views.ContactView.as_view(), name='contact'),
	path('learning-journey/', views.learning_journey, name='learning-journey'),
	path('leadership/', views.leadership, name='leadership'),
	path('news/', views.NewsListView.as_view(), name='news'),
	path('initiatives/', views.initiatives, name='initiatives'),
	path('donate/', views.donate, name='donate'),
	path('films/', views.films, name='films')
]