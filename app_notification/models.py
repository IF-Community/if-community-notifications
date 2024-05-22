from django.db import models

class Users(models.Model):

    user = models.IntegerField()
    profile_name = models.CharField("Nome do Perfil", max_length=100)
    email = models.EmailField("E-mail")

    def __str__(self) -> str:
        return f'{self.profile_name}'

    class Meta:
        verbose_name_plural = "Usuários"

class Notification(models.Model):

    TYPE_MESSAGES = (
        ("AV","aviso"),
        ("MA","marcou"),
        ("RE", "respondeu"),
        ("DM","deletado pela moderação"),
    )

    recipient = models.ForeignKey(Users, related_name='received_notifications', on_delete=models.CASCADE)
    sender = models.ForeignKey(Users, related_name='sent_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    type_message = models.CharField(max_length=2, choices=TYPE_MESSAGES)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.recipient.profile_name} - {self.message}'

    class Meta:
        verbose_name_plural = "Notificações"

