# Generated by Django 4.0 on 2022-01-19 17:11

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=sqlalchemy.sql.expression.true, serialize=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('comment', models.TextField()),
                ('date_posted', models.DateField(default='2022-01-19')),
                ('due_date', models.DateField(default='2022-01-19')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
