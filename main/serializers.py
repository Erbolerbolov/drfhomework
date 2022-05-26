from rest_framework import serializers
# from .serializers import CategoryProductSerializer


from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    # category = CategoryProductSerializer

    class Meta:
        model = Product
        fields = "__all__"

    
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep["category"] = instance.category.title
    #     return rep
