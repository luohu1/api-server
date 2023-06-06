# Generated by Django 4.1.9 on 2023-06-06 11:28

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='group name')),
                ('desc', models.CharField(blank=True, max_length=128, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update time')),
            ],
            options={
                'db_table': 'sys_group',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='role name')),
                ('desc', models.CharField(blank=True, max_length=128, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update time')),
            ],
            options={
                'db_table': 'sys_role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, verbose_name='nickname')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='mobile')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'sys_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
