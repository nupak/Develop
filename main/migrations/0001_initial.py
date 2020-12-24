# Generated by Django 3.0.8 on 2020-11-29 17:35

from django.db import migrations, models
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scientist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='images/scientistPhoto/default.png', max_length=255, null=True, upload_to='images/scientistPhoto', verbose_name='Фотография пользователя')),
                ('hide_email', models.BooleanField(default=True)),
                ('hide_phone', models.BooleanField(default=True)),
                ('name', models.CharField(default='Имя пользователя', max_length=60, verbose_name='Имя')),
                ('surname', models.CharField(default='Фамилия', max_length=60, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, default='Отчество', max_length=60, verbose_name='Отчество')),
                ('Bigregion', models.CharField(choices=[('cfo', 'Центральный Федеральный Округ'), ('szfo', 'Северо-Западный Федеральный Округ'), ('yfo', 'Южный Федеральный Округ'), ('skfo', 'Северо-Кавказский Федеральный Округ'), ('pfo', 'Приволжский Федеральный Округ'), ('urfo', 'Уральский Федеральный Округ'), ('sfo', 'Сибирский Федеральный Округ'), ('dfo', 'Дальневосточный Федеральный Округ')], default='', max_length=60, verbose_name='Федеральный округ')),
                ('region', models.CharField(blank=True, default='Регион', max_length=60, verbose_name='Cубъект')),
                ('job_place', models.CharField(blank=True, default='Место работы', max_length=60, verbose_name='Место работы')),
                ('position', models.CharField(blank=True, default='Должность', max_length=60, verbose_name='Должность')),
                ('academicDegree', models.CharField(choices=[('kandNauk', 'Кандидат наук'), ('drNauk', 'Доктор наук')], default='', max_length=60, verbose_name='Ученая степень')),
                ('codeSpeciality', models.CharField(choices=[('Коррекционная психология', 'Коррекционная психология'), ('Коррекционная педагогика', 'Коррекционная педагогика')], default='', max_length=60, verbose_name='Специальность')),
                ('academicTitle', models.CharField(choices=[('prof', 'Профессор'), ('docs', 'Доцент')], default='', max_length=60, verbose_name='Ученое звание')),
                ('mainResults', models.TextField(blank=True, default='Основные результаты', verbose_name='Основные результаты исследовательской деятельности')),
                ('keyWords', models.TextField(blank=True, max_length=200, verbose_name='Ключевые слова')),
                ('keyWordsString', models.CharField(blank=True, default='', max_length=200, verbose_name='Строка ключевых слов')),
                ('phone_numer', models.CharField(blank=True, default='', max_length=12, verbose_name='Номер Телефона')),
                ('ymapshortcut', models.TextField(blank=True, default='', verbose_name='Точка на яндекс карте')),
                ('publication', models.TextField(blank=True, default='', max_length=4096)),
                ('elibID', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код Elibriary')),
                ('elib_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на cтраницу в Elibriary')),
                ('h_Scopus', models.IntegerField(blank=True, null=True, verbose_name='H - индекс  Scopus')),
                ('scopusLink', models.URLField(blank=True, null=True, verbose_name='Ссылка на cтраницу в Scopus')),
                ('h_WebOfScience', models.IntegerField(blank=True, null=True, verbose_name='H - индекс  Web of Science')),
                ('WoSLink', models.URLField(blank=True, null=True, verbose_name='Ссылка на cтраницу в Web of Science')),
            ],
            options={
                'verbose_name': 'Ученый',
                'verbose_name_plural': 'Ученые',
            },
            managers=[
                ('objects', main.models.MyAccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('headLine', models.CharField(max_length=128, verbose_name='Название новости')),
                ('announce_text', models.TextField(blank=True, max_length=512, verbose_name='Текст для анонса')),
                ('text', models.TextField(max_length=4096, verbose_name='Текст новости')),
                ('image', models.ImageField(default='images/news/default.png', upload_to='images/news/')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='newsSer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
    ]
