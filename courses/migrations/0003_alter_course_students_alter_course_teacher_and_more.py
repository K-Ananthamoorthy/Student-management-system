# Generated by Django 5.1.1 on 2024-10-23 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_initial"),
        ("users", "0003_alter_student_date_of_birth_alter_teacher_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                blank=True, related_name="courses", to="users.student"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="courses",
                to="users.teacher",
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="results",
                to="courses.course",
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="results",
                to="users.student",
            ),
        ),
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_announcements",
                        to="courses.course",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teacher_announcements",
                        to="users.teacher",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Note",
        ),
    ]
