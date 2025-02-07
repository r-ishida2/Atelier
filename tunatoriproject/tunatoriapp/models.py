from django.db import models

# 投稿
class Publish(models.Model):
    user_id = models.ForeignKey()

# カテゴリー
class Category(models.Model):
    category_name = models.CharField()

# 返信
class Reply(models.Model):
    user_id = models.ForeignKey()

# ブックマーク
class Bookmark(models.Model):
    user_id = models.ForeignKey()