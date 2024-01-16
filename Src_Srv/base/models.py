from django.db import models

# Create your models here.
class QueryLog(models.Model):
    query_id = models.AutoField(primary_key=True)
    query_text = models.TextField(default="Q")
    answer_text = models.TextField(default="A")
    timestamp = models.DateTimeField(auto_now_add=True)
    imageResponse = models.BooleanField(default=False)

    def __str__(self):
        return self.query_text

