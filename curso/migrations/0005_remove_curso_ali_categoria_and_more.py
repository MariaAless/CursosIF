# Generated by Django 4.2.2 on 2023-06-18 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("curso", "0004_rename_cursos_curso_ali_curso_info_curso_api"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="curso_ali",
            name="categoria",
        ),
        migrations.RemoveField(
            model_name="curso_api",
            name="categoria",
        ),
        migrations.RemoveField(
            model_name="curso_info",
            name="categoria",
        ),
        migrations.DeleteModel(
            name="Categoria",
        ),
    ]
