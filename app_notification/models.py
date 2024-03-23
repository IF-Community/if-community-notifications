from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):

    TYPE_MESSAGES = (
        ("AV","aviso"),
        ("MA","marcou"),
        ("RE", "espondeu"),
        ("DM","deletado pela moderação"),
    )

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sender')
    message = models.TextField()
    type_message = models.CharField(max_length=2, choices=TYPE_MESSAGES)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.recipient} - {self.message}'

    class Meta:
        verbose_name_plural = "Notificações"