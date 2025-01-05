from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Users

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = Users
        fields = ['username', 'email', 'first_name', 'last_name', 'company_name', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 since it's not needed for creation
        user = Users.objects.create_user(**validated_data)  # Use `create_user` for hashed password
        return user
