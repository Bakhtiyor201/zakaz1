# Generated by Django 4.1 on 2022-08-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('course', models.CharField(choices=[('Course1', 'Course1'), ('Course2', 'Course2'), ('Course3', 'Course3')], max_length=30)),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
            },
        ),
    ]
