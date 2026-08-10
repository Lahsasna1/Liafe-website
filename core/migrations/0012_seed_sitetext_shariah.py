from django.db import migrations

ITEMS = [
    ('shariah_eyebrow',                'Hero eyebrow / breadcrumb current segment', 'Shariah Advisory'),
    ('shariah_request_advisory_button','Hero button',                               'Request Advisory'),
    ('shariah_process_eyebrow',        'Process section eyebrow',                   'Our Process'),
    ('shariah_steps_heading',          'Process section heading',                   'Eight steps to compliant, confident outcomes.'),
    ('shariah_offer_eyebrow',          'Service cards eyebrow',                     'What We Offer'),
    ('shariah_dimensions_heading',     'Service cards heading',                     'Specialist advisory across all dimensions of Shariah compliance.'),
    ('shariah_back_to_home_button',    'CTA secondary button',                      'Back to Home'),
]


def seed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    for i, (key, label, default_value) in enumerate(ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'shariah', 'label': label, 'value': default_value, 'order': i,
        })


def unseed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    SiteText.objects.filter(key__in=[k for k, _, _ in ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_seed_sitetext_research'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
