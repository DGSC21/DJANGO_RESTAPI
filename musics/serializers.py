from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music # 모델을 뮤직으로 설정한다.
        fields = ('id', 'title', 'artist', 'album', 'genre', 'year') # 필드를 설정한다.