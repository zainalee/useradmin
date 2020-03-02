from products.models import Product, Categories
from rest_framework import viewsets
from .serializers import ProductSerializers, CategoriesSerializers
from rest_framework.generics import ListAPIView
#  {ListAPIView,
# RetrieveAPIView,
# CreateAPIView,
# DestroyAPIView,
# UpdateAPIView}


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    # permission_classes = []

    # def get (self,request, *args, **kwargs):
    #     if request.method =='GET':
    #         snippets = Product.objects.all()
    #         serializer = ProductSerializers(snippets, many=True)
    #         return Response(serializer.data)
        
    #     if request.method == 'POST':
    #         serializer = ProductSerializers(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response (
    #             {
    #             "message":"Success",
    #             "status" : 200,
                # "result": ax.data,
                # "result_count" : qs.count()

                # })
        # elif:
        #     return Response(
        #     {
        #         'message':fail,
        #         "status" : 400,
        #     }
        # )
            


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializers
    queryset = Categories.objects.all() 
