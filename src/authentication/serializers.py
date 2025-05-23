from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    phone_number = PhoneNumberField(required=False, allow_blank=True, allow_null=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(
            username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError('Username already exists')
        
        phone_number_exists = not attrs['phone_number']=="" and User.objects.filter(
            phone_number=attrs['phone_number']).exists()
        if phone_number_exists:
            raise serializers.ValidationError('Phone number already exists')

        return super().validate(attrs)
