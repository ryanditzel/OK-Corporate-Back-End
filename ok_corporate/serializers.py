from statistics import mode
from rest_framework import serializers
from .models import Company, User, Review


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'rating', 'reviews')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'username',
                  'email', 'password', 'reviews')


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
