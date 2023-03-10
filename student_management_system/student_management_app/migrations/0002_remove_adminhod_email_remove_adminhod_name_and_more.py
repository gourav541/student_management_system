# Generated by Django 4.1.7 on 2023-03-01 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminhod',
            name='email',
        ),
        migrations.RemoveField(
            model_name='adminhod',
            name='name',
        ),
        migrations.RemoveField(
            model_name='adminhod',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='password',
        ),
        migrations.RemoveField(
            model_name='students',
            name='email',
        ),
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='password',
        ),
        migrations.AddField(
            model_name='staffs',
            name='address',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(verbose_name=255),
        ),
    ]
