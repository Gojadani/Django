from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="index"),
    path("Brian", views.Brian, name="Brian"),
    path("<str:name>", views.greet, name="greet")
=======
    path('', views.testIndex, name="index")
>>>>>>> b6cb05acf92063acf4224d3369f4d40577b907bd
]