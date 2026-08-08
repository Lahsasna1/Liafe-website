from django.db import migrations

OLD_STATS = [
    ('12',   '+',  'Markets Served',       0),
    ('40',   '+',  'Programmes Delivered', 1),
    ('25',   '',   'Senior Associates',    2),
    ('£3.2', 'bn', 'Reviewed AUM',         3),
]

NEW_STATS = [
    ('4',    '',  'Core Practices',        0),
    ('3',    '',  'Global Regions',        1),
    ('2025', '',  'Founded',               2),
    ('100',  '%', 'Independent Advisory',  3),
]


def update_stats(apps, schema_editor):
    AboutStat = apps.get_model('core', 'AboutStat')
    AboutStat.objects.all().delete()
    for value, suffix, label, order in NEW_STATS:
        AboutStat.objects.create(value=value, suffix=suffix, label=label, order=order)


def revert_stats(apps, schema_editor):
    AboutStat = apps.get_model('core', 'AboutStat')
    AboutStat.objects.all().delete()
    for value, suffix, label, order in OLD_STATS:
        AboutStat.objects.create(value=value, suffix=suffix, label=label, order=order)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_about_stat'),
    ]

    operations = [
        migrations.RunPython(update_stats, revert_stats),
    ]
