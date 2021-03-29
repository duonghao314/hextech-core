# Generated by Django 3.1.7 on 2021-03-29 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20210325_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
        migrations.CreateModel(
            name='BlogLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_like', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('blog', 'user')},
            },
        ),
    ]