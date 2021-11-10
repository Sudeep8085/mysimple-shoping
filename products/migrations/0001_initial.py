# Generated by Django 3.1.3 on 2021-11-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_image', models.ImageField(default='p.png', upload_to='products')),
                ('pro_name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]