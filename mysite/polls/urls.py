from django.urls import include, path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', include([
        # ex: /polls/5/
        path('', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('vote/', views.vote, name='vote'),
    ])),
]
