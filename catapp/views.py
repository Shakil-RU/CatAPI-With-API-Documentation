
from rest_framework import generics
from catapp.models import catshop
from catapp.serializer import ProductSerializer


class Allcat(generics.ListCreateAPIView):
    queryset = catshop.objects.all()
    serializer_class = ProductSerializer


class SpecificProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = catshop.objects.all()
    serializer_class = ProductSerializer

