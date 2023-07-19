
from django.urls import path
from catapp.views import Allcat, SpecificProductDetail

urlpatterns = [
    path('catshop/', Allcat.as_view(), name = 'Catshop'),
    path('catshop/<int:pk>/', SpecificProductDetail.as_view(), name = 'catdetails'),
]
