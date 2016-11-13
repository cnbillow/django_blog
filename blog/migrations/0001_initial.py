# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 15:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=50, verbose_name='文章描述')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('click_count', models.IntegerField(default=0, verbose_name='点击次数')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['-date_publish'],
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='显示顺序(从小到大)')),
            ],
            options={
                'verbose_name_plural': '分类',
                'ordering': ['index', 'id'],
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签名称')),
                ('weight', models.IntegerField(default=10, verbose_name='标签大小')),
            ],
            options={
                'verbose_name_plural': '标签',
                'ordering': ['id'],
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]