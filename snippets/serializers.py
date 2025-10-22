from django.contrib.auth import get_user_model

from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


User = get_user_model()


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "url", "id", "owner", "title", "code", "linenos", "language", "style", "highlight"
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        view_name='snippet-detail', read_only=True, many=True
    )

    class Meta:
        model = User
        fields = [
            'url', 'id', 'username', 'snippets'
        ]
