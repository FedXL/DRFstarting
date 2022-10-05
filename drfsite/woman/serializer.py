import io

from rest_framework import serializers
from .models import Women

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True, read_only=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("*"*50)
        print("instance:",type(instance),sep="\n")
        for i in instance.__dict__:
            print(i)
        print("validate:",type(validated_data))
        print("validate:",validated_data,sep="\n")
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('time_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance

class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


#-------------------------------------------------------------------------------------------
#---------------------------------------first try-------------------------------------------
#-------------------------------------------------------------------------------------------

# class WomenSerializer2(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
# def encode():
#     model = WomenModel("Zerohouse", "Content: Yep! Good content!")
#     model_s = WomenSerializer(model)
#     print(model_s.data, type(model_s), sep='\n')
#     json = JSONRenderer().render(model_s.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content": "Content: Angelina Super"}')
#     data = JSONParser().parse(stream)
#     serializers = WomenSerializer2(data=data)
#     serializers.is_valid()
#     print(type(serializers),serializers,serializers.validated_data,sep='\n')
#
