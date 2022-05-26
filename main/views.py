from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Q


from .serializers import ProductSerializer
from .models import Product



class ProductAPiView(APIView):


    def get(self, request):
        search = request.query_params.get("search")
        if search:
            products = Product.objects.filter(Q (title__icontains=search) | Q(price__icontains=search), published = True)
        else:
            products = Product.objects.filter(published =True).order_by('title')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class RetrieveProductView(generics.ListAPIView):
    queryset = Product.objects.all() # Ленивый запрос
    serializer_class = ProductSerializer


class DestroyProductView(generics.DestroyAPIView):
    queryset = Product.objects.all() # Ленивый запрос
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all() # Ленивый запрос
    serializer_class = ProductSerializer


class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all() # Ленивый запрос
    serializer_class = ProductSerializer          