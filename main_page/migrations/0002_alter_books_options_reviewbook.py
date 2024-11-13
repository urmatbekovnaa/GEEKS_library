# Generated by Django 4.2.16 on 2024-11-12 17:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Оставьте отзыв о книге')),
                ('mark', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Укажите оценку от 1 до 5')),
                ('review_books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main_page.books')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]