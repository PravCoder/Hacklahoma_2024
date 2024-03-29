# Generated by Django 5.0.2 on 2024-02-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_largeproject_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='EssayDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('due_date', models.CharField(max_length=200, null=True)),
                ('doc_type', models.CharField(max_length=200, null=True)),
                ('prompt', models.CharField(max_length=500, null=True)),
                ('content', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
