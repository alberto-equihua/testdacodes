# Generated by Django 2.2.7 on 2020-07-29 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapi', '0006_auto_20200729_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='lesson_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapi.Lesson'),
        ),
        migrations.AlterField(
            model_name='lessonresult',
            name='lesson_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapi.Lesson'),
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapi.Lesson'),
        ),
    ]
