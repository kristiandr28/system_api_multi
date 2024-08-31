from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()
UserProfile = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['user']
        
class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        UserModel = get_user_model()

        # Cek apakah username adalah email
        if '@' in username:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            user = UserModel.objects.filter(username=username).first()
            if user is None:
                raise serializers.ValidationError("Invalid username or password.")
        
        # Verifikasi password
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid username or password.")

        attrs['user'] = user
        return attrs