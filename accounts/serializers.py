from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "phone_number",
            "password",
        ]

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            username=validated_data.get("username"),
            phone_number=validated_data.get("phone_number"),
            password=validated_data["password"]
        )