from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("simple-graph/", views.simple_rdf_graph, name="simple_rdf_graph"),
]
