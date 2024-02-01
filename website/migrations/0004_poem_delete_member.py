# Generated by Django 5.0.1 on 2024-01-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_members_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('poem_text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]