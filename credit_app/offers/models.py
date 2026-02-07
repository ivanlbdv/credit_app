from django.db import models


class CreditOffer(models.Model):
    logo = models.ImageField(
        upload_to='logos/',
        verbose_name='Логотип'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    amount = models.CharField(
        max_length=50,
        verbose_name='Сумма займа'
    )
    term = models.CharField(
        max_length=50,
        verbose_name='Срок'
    )
    grace_period = models.CharField(
        max_length=50,
        verbose_name='Период без %'
    )
    apply_url = models.URLField(
        verbose_name='Ссылка на оформление'
    )
    details_text = models.TextField(
        verbose_name='Подробная информация',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Оффер компании {self.name}'

    class Meta:
        verbose_name = 'Кредитный оффер'
        verbose_name_plural = 'Кредитные офферы'
