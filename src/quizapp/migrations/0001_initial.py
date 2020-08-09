from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_userID', models.TextField(default='', max_length=15)),
                ('_points', models.IntegerField(default=0)),
                ('_previousPoints', models.IntegerField(default=0)),
                ('_previousCorrect', models.BooleanField(default=False)),
                ('_userChannelName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_text', models.CharField(max_length=50)),
                ('_correct', models.BooleanField()),
                ('_pointValue', models.IntegerField(default=0)),
                ('_votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_questionText', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_quizName', models.CharField(max_length=60)),
                ('_quizDescription', models.TextField(default=None, null=True)),
                ('_dateCreated', models.DateTimeField(auto_now_add=True)),
                ('_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_owner', models.IntegerField(default=-1)),
                ('_sessionID', models.CharField(default='', max_length=6)),
                ('_hostChannelName', models.CharField(max_length=255)),
                ('_questionCounter', models.IntegerField(default=-1)),
                ('_currentVotes', models.IntegerField(default=0)),
                ('_sessionState', models.TextField(default='start', max_length=20)),
                ('_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='_quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='_voters',
            field=models.ManyToManyField(to='quizapp.AnonymousUser'),
        ),
        migrations.AddField(
            model_name='anonymoususer',
            name='_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Session'),
        ),
    ]
