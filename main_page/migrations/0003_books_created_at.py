# Generated by Django 4.2.16 on 2024-11-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_books_options_reviewbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
