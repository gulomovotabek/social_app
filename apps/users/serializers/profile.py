from rest_framework import serializers

from users.models import User


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'avatar',
        )

    def create(self, validated_data):
        passport = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(passport)
        user.save()
        return user


class RetrieveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'avatar',
        )


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'avatar',
        )
