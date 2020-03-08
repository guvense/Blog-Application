from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["created_at"]

    def __str__(self):
        return self.username