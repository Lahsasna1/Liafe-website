from django.db import migrations

ITEMS = [
    ('home_hero_eyebrow',             'Hero eyebrow label',                 'London Consultancy'),
    ('home_about_eyebrow',            'About section eyebrow',              'About LIAFE'),
    ('home_core_services_eyebrow',    'Core Services eyebrow',              'Core Services'),
    ('home_know_more_button',         'Service card "Know More" button',    'Know More'),
    ('home_why_choose_eyebrow',       'Why Choose Us eyebrow',              'Why Choose LIAFE'),
    ('home_approach_eyebrow',         'Approach section eyebrow',           'Our Approach'),
    ('home_start_conversation_button','Approach section button',            'Start a conversation'),
    ('home_explore_services_button',  'Hero fallback secondary button',     'Explore Services'),
    ('home_our_services_button',      'CTA band secondary button',          'Our Services'),
]


def seed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    for i, (key, label, default_value) in enumerate(ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'home', 'label': label, 'value': default_value, 'order': i,
        })


def unseed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    SiteText.objects.filter(key__in=[k for k, _, _ in ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_sitetext'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
