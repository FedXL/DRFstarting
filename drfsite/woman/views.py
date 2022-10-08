from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import WomenSerializer


# class WomenApiViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     @action(methods=['get'], detail=True)
#     def category(self,request,pk=None):
#
#         try:
#             cats = Category.objects.get(pk=pk)
#             return Response({'cats': cats.name})
#         except:
#             return Response({'error': "Category does not exists"})

class WomenApiViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]
        else:
            return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self,request,pk=None):

        try:
            cats = Category.objects.get(pk=pk)
            return Response({'cats': cats.name})
        except:
            return Response({'error': "Category does not exists"})


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenApiUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class WomenApiDestroy(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


class WomenApiView(APIView):
    def get(self, request):
        lst = Women.objects.all()
        return Response({'post': WomenSerializer(lst, many=True, ).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'title': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT nt allowed"})
        try:
            print("get from base instance: ", "*"*50)
            print(pk)
            instance = Women.objects.get(pk=pk)
            print(type(instance))
            for i in instance.__dict__:
                print(i)
        except:
            return ({"error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def delete(self, *args, **kwargs):
        print("start delete"+"*"*20)
        pk = kwargs.get('pk', None)
        print(pk)
        if not pk:
            return Response({"error":"method DELETE not allowed"})
        try:
            print(f"start try with pk={pk}")
            new = Women.objects.filter(pk=pk)
            print(new)
            new.delete()
            return Response({"success": f"Object pk={pk} was DELETED"})
        except:
            return Response({"error": "Object does not exists"})

