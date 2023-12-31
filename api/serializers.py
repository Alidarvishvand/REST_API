from rest_framework import serializers
from .models import question , answer
from .custom_relational_fields import UserEmailRelationalField
class personserializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class Questionserializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = UserEmailRelationalField(read_only=True)
    class Meta:
        model = question
        fields = '__all__'
    def get_answers(self,obj):
        result =obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = answer
        fields = '__all__'