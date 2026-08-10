from django.db import migrations

GLOBAL_ITEMS = [
    ('breadcrumb_home_label',     'Breadcrumb "Home" segment (shared across all service pages)',     'Home'),
    ('breadcrumb_services_label', 'Breadcrumb "Services" segment (shared across all service pages)', 'Services'),
]

ACADEMY_ITEMS = [
    ('academy_eyebrow',                 'Hero eyebrow label',           'Academy'),
    ('academy_explore_programmes_button','Hero primary button',         'Explore Programmes'),
    ('academy_enquire_now_button',      'Hero secondary button',        'Enquire Now'),
    ('academy_delivery_empty_title',    'Delivery modes empty state',   'Delivery modes coming soon'),
    ('academy_catalogue_eyebrow',       'Course Catalogue eyebrow',     'Course Catalogue'),
    ('academy_disciplines_heading',     'Course Catalogue heading',     'Four disciplines. Every level.'),
    ('academy_disciplines_subtitle',    'Course Catalogue subtitle',    'From foundations to executive practice — structured learning designed around real-world finance.'),
    ('academy_courses_empty_title',     'No courses empty-state title', 'Courses coming soon'),
    ('academy_courses_empty_body',      'No courses empty-state text',  'Our programme catalogue is being finalised. Contact us to register your interest.'),
    ('academy_courses_empty_button',    'No courses empty-state button','Get in touch'),
    ('academy_back_to_home_button',     'CTA secondary button',         'Back to Home'),
]


def seed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    for i, (key, label, default_value) in enumerate(GLOBAL_ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'global', 'label': label, 'value': default_value, 'order': i,
        })
    for i, (key, label, default_value) in enumerate(ACADEMY_ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'academy', 'label': label, 'value': default_value, 'order': i,
        })


def unseed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    keys = [k for k, _, _ in GLOBAL_ITEMS] + [k for k, _, _ in ACADEMY_ITEMS]
    SiteText.objects.filter(key__in=keys).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_seed_sitetext_home'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
