from django.db import models

class Books(models.Model):
    GANRE_CHOICE = (
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
        ('Приключения', 'Приключения')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Введите название книги')
    description = models.TextField(verbose_name='Введите описание книги')
    price = models.FloatField(verbose_name='Введите цену книги')
    published_data = models.DateField(verbose_name='Дата публикации')
    genre = models.CharField(max_length=100, choices=GANRE_CHOICE, verbose_name='Жанр книги')
    mail = models.EmailField(verbose_name='Введите почту автора')
    author = models.CharField(max_length=100, verbose_name='Введите автора книги')
    audio_book = models.URLField(verbose_name='Введите ссылку на аудиокн')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'
