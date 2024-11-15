from django.core.validators import MinValueValidator, MaxValueValidator
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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    stock_count = models.PositiveIntegerField(default=0, verbose_name="Количество в наличии", null=True)

    def reduce_stock(self):
        if self.stock_count > 0:
            self.stock_count -= 1
            self.save()

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'

class ReviewBook(models.Model):
    review_books = models.ForeignKey(Books, on_delete=models.CASCADE,
                                    related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзыв о книге')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_books} - {self.created_at}'
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
