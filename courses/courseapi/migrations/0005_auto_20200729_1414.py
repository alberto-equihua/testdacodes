# Generated by Django 2.2.7 on 2020-07-29 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapi', '0004_auto_20200729_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseresult',
            name='lesson_result_ids',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='question_ids',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response_ids',
        ),
        migrations.AddField(
            model_name='question',
            name='lesson_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='courseapi.Lesson'),
        ),
        migrations.AddField(
            model_name='responsequestion',
            name='question_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='courseapi.Question'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='lesson_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='courseapi.Lesson'),
        ),
        migrations.AlterField(
            model_name='lessonresult',
            name='lesson_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='courseapi.Lesson'),
        ),
    ]
