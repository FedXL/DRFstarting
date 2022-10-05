from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women
from .serializer import WomenSerializer


# class WomenApiView (generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

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
        print(pk)
        if not pk:
            return Response({"error": "Method PUT nt allowed"})
        try:
            print("get from base instance: ","*"*50)
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

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({"error":"method DELETE not allowed"})
        try:
            new = Women.objects.filter(pk=pk)
            new.delete()
            return Response({"success": f"Object pk={pk} was DELETED"})
        except:
            return Response({"error": "Object does not exists"})
        #;l;ekw;eokf;sakfe;skf
