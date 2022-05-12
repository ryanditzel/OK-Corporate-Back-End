from rest_framework import serializers
from .models import Company, User, Review, CompanyReview
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class CompanySerializer(serializers.ModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='ReviewDetail',
        many=False
    )

    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'rating', 'review')


class ReviewSerializer(serializers.ModelSerializer):
    company = CompanySerializer(
        # view_name='company_detail',
        read_only=True
    )

    user = UserSerializer(
        # view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'company', 'user', 'title', 'jobtitle',
                  'body', 'helpful', 'unhelpful')


class CompanyReviewSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(read_only=True, source='company_id')
    review = ReviewSerializer(read_only=True, many=True, source='review_id')

    class Meta:
        model = CompanyReview
        fields = ('company', 'review')
