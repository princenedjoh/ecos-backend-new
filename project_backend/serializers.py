from rest_framework import serializers
from .models.users_model import Users
from .models.article_model import Article
from .models.article_category_model import Article_category
from .models.article_like_model import Article_like
from .models.comment_model import Comment
from .models.comment_like_model import Comment_like
from .models.reply_model import Reply
from .models.reply_likes_model import Reply_like
from .models.mission_model import Missions
from .models.alert_model import Alert
from rest_framework.validators import UniqueValidator
from project_backend.models.users_model import Users
from project_backend.models.settings_model import Settings

class Users_serializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field in self.Meta.fields:
                setattr(instance, field, value)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class Article_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class Settings_serializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class Article_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article_category
        fields = '__all__'

class Article_like_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article_like
        fields = '__all__'

class Reply_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class Reply_like_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reply_like
        fields = '__all__'

class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class Comment_like_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_like
        fields = '__all__'

class Missions_serializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = '__all__'

class Alert_serializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'