from rest_framework import serializers
from .models import Company, User, Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'rating', 'reviews')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'username', 'password')
        extra_kwargs = {'write_only': True}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    companies = serializers.HyperlinkedRelatedField(
        view_name='company_detail',
        read_only=True
    )

    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'company', 'user', 'title', 'jobtitle',
                  'body', 'helpful', 'unhelpful', 'companies')
