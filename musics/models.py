from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=50) # 제목
    artist = models.CharField(max_length=50) # 아티스트
    album = models.CharField(max_length=50) # 앨범
    genre = models.CharField(max_length=30) #장르
    year = models.IntegerField() # 출시년도

    def __str__(self):
        return self.title