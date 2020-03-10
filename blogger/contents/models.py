from django.db import models

# Create your models here.


class Content(models.Model):

    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"
        ordering = ["created_at"]

    def __str__(self):
        return self.title
