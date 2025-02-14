from django.db import models
from accounts.models import CustomUser

SCORE_CHOICES = (
    (1, '★1'),
    (2, '★2'),
    (3, '★3'),
    (4, '★4'),
    (5, '★5'),
)

CATEGORY_CHOICES = (
    ('イラスト', 'イラスト'),
    ('風景画', '風景画'),
    ('写真', '写真'),
    ('その他', 'その他'),
)

# # カテゴリー
# class Category(models.Model):
#     name = models.CharField(max_length=64,choices=CATEGORY_CHOICES,verbose_name="カテゴリ名")
#     def __str__(self):
#         return self.name

# 投稿
class Publish(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    category = models.CharField(max_length=64,choices=CATEGORY_CHOICES,verbose_name='カテゴリー')
    title = models.CharField(max_length=64,verbose_name="タイトル")
    detail = models.TextField(max_length=1024,verbose_name="作品詳細")
    image = models.ImageField(upload_to="images/")
    at_post = models.DateTimeField("date published")
    def __str__(self):
        return self.title

# 返信
class Reply(models.Model):
    publish_id = models.ForeignKey(Publish,on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    rating = models.IntegerField('評価値',choices=SCORE_CHOICES,default=1)
    comment = models.TextField(max_length=1024,verbose_name="コメント")
    at_reply = models.DateTimeField("date published")

# ブックマーク
class Bookmark(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    publish_id = models.ForeignKey(Publish,on_delete=models.CASCADE)
    at_bookmark = models.DateTimeField("date published")