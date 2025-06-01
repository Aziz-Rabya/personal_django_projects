from django.urls import path
from .views import Home, ProfileList, ProfileCreate, watch, ShowMovieDetail, ShowMovie

app_name = 'core'
urlpatterns = [
    path('', Home.as_view()),
    path('profiles/', ProfileList.as_view(), name='profile_list'),
    path('profiles/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/', watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name='show_detail'),
    path('movie/play/<str:movie_id>/', ShowMovie.as_view(), name='play'),

]
