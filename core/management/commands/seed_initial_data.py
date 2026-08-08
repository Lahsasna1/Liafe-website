import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Seed initial site data and create superuser if missing'

    def handle(self, *args, **options):
        self._seed_superuser()
        self._seed_site_settings()
        self._seed_hero_slides()
        self._seed_homepage_sections()
        self._seed_value_pillars()
        self._seed_about_stats()
        self._seed_services()
        self._seed_service_features()
        self.stdout.write(self.style.SUCCESS('Seed complete.'))

    # ── Superuser ──────────────────────────────────────────────────────────────
    def _seed_superuser(self):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email    = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
        if not password:
            self.stdout.write('DJANGO_SUPERUSER_PASSWORD not set — skipping superuser creation.')
            return
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(f'Superuser "{username}" created.')
        else:
            self.stdout.write(f'Superuser "{username}" already exists.')

    # ── Core: SiteSetting ─────────────────────────────────────────────────────
    def _seed_site_settings(self):
        from core.models import SiteSetting
        obj, created = SiteSetting.objects.get_or_create(pk=1)
        if created:
            obj.company_name   = 'London International Academy for Excellence'
            obj.short_name     = 'LIAFE'
            obj.tagline        = 'Empowering growth through knowledge, innovation and integrity.'
            obj.phone          = '+44 207 354 33 55'
            obj.email          = 'info@ukliafe.com'
            obj.address        = 'London, N4 2DN'
            obj.working_hours  = '9 AM – 5 PM'
            obj.footer_text    = 'A consultancy dedicated to empowering growth through Shariah advisory, education, research, and publication.'
            obj.copyright_text = '© 2026 London International Academy for Excellence. All rights reserved.'
            obj.save()
            self.stdout.write('SiteSetting created.')

    # ── Core: HeroSlide ───────────────────────────────────────────────────────
    def _seed_hero_slides(self):
        from core.models import HeroSlide
        if HeroSlide.objects.exists():
            return
        HeroSlide.objects.create(
            title       = 'London International Academy for Excellence',
            subtitle    = 'Shariah Advisory · Academy · Research & Development · Publications',
            description = 'A consultancy dedicated to empowering growth through professional training, impactful publications, strategic research, and expert Shariah advisory.',
            button_1_text = 'Consult Us',
            button_1_link = '/contact/',
            button_2_text = 'Explore Services',
            button_2_link = '#services',
            order = 0,
        )
        self.stdout.write('HeroSlide created.')

    # ── Core: HomepageSection ─────────────────────────────────────────────────
    def _seed_homepage_sections(self):
        from core.models import HomepageSection
        if HomepageSection.objects.exists():
            return
        sections = [
            dict(section_name='hero', order=0,
                 title='London International Academy for Excellence',
                 subtitle='Shariah Advisory – Academy – Research & Development – Publications',
                 description='The London International Academy for Excellence is a consultancy dedicated to empowering growth through professional training, impactful publications, strategic research, and expert Shariah advisory.',
                 button_text='Consult Us', button_link='/contact/'),
            dict(section_name='about', order=1,
                 title='A consultancy where knowledge, innovation and integrity meet.',
                 description='The London International Academy for Excellence (LIAFE) is a consultancy dedicated to empowering growth through four core services: professional training through the Academy, impactful publications, strategic research, and expert Shariah advisory. We blend knowledge, innovation, and integrity to deliver solutions that matter.'),
            dict(section_name='core_services', order=2,
                 title='Four practices, one standard of excellence.',
                 subtitle='Every engagement draws on the full strength of LIAFE — advisory, education, research, and publication working in concert.'),
            dict(section_name='why_choose_us', order=3,
                 title='Six principles that govern everything we deliver.',
                 description='From Shariah advisory to executive education, our work is shaped by a single set of principles. They are how we hire, how we engage, and how we measure ourselves.'),
            dict(section_name='approach', order=4,
                 title='Faith. Finance. Evidence. Working together.',
                 description="We sit at the intersection of classical scholarship and modern finance. Our engagements start with the client's commercial and regulatory reality and end with structures that are defensible, transparent, and durable.",
                 button_text='Start a conversation', button_link='/contact/'),
            dict(section_name='cta', order=5,
                 title='Ready to work with LIAFE?',
                 button_text='Contact Us', button_link='/contact/'),
        ]
        for s in sections:
            HomepageSection.objects.get_or_create(section_name=s.pop('section_name'), defaults=s)
        self.stdout.write('HomepageSections created.')

    # ── Core: ValuePillar ─────────────────────────────────────────────────────
    def _seed_value_pillars(self):
        from core.models import ValuePillar
        if ValuePillar.objects.exists():
            return
        pillars = [
            ('Knowledge',       'A foundation of rigorous scholarship and applied expertise in finance, law, and ethics.',           'Knowledge',  0),
            ('Innovation',      'Modern frameworks for emerging fintech, digital finance, and inclusive economic systems.',          'Innovation', 1),
            ('Integrity',       'Independent counsel and uncompromising standards across every engagement.',                         'Integrity',  2),
            ('Excellence',      'Delivery measured against the highest professional and academic benchmarks.',                       'Excellence', 3),
            ('Ethical Solutions','Outcomes designed to be transparent, defensible, and aligned with Shariah principles.',            'Ethical',    4),
            ('Global Impact',   'A London base, a worldwide reach — partnerships across the UK, MENA, and Asia.',                   'Global',     5),
        ]
        for title, desc, icon, order in pillars:
            ValuePillar.objects.create(title=title, description=desc, icon_class=icon, order=order)
        self.stdout.write('ValuePillars created.')

    # ── Core: AboutStat ───────────────────────────────────────────────────────
    def _seed_about_stats(self):
        from core.models import AboutStat
        if AboutStat.objects.exists():
            return
        stats = [
            ('4',    '',  'Core Practices',        0),
            ('3',    '',  'Global Regions',        1),
            ('2025', '',  'Founded',               2),
            ('100',  '%', 'Independent Advisory',  3),
        ]
        for value, suffix, label, order in stats:
            AboutStat.objects.create(value=value, suffix=suffix, label=label, order=order)
        self.stdout.write('AboutStats created.')

    # ── Services ──────────────────────────────────────────────────────────────
    def _seed_services(self):
        from services.models import Service
        if Service.objects.exists():
            return
        services = [
            dict(slug='shariah-advisory', title='Shariah Advisory', menu_title='Shariah Advisory',
                 icon_class='Shariah', order=0,
                 short_description='Independent Shariah advisory, structuring, and audit for ethical, compliant finance.',
                 hero_title='Ensuring Compliance, Building Trust',
                 hero_description='LIAFE provides expert Shariah advisory services to help businesses grow ethically, transparently, and in harmony with Shariah principles.',
                 cta_title='Ready to learn more about Shariah Advisory?',
                 cta_button_text='Get in Touch', cta_button_link='/contact/'),
            dict(slug='academy', title='Academy', menu_title='Academy',
                 icon_class='Academy', order=1,
                 short_description='Executive education, structured training, and online learning for finance professionals.',
                 hero_title='Professional Training for the Modern Finance Practitioner',
                 hero_description='The Academy is LIAFE\'s education wing, offering executive and structured professional training both in-person and online.',
                 cta_title='Ready to learn more about Academy?',
                 cta_button_text='Get in Touch', cta_button_link='/contact/'),
            dict(slug='research-house', title='Research House', menu_title='Research House',
                 icon_class='Research', order=2,
                 short_description='Dedicated R&D in Islamic finance, social sciences, and fintech.',
                 hero_title='Dedicated R&D in Islamic Finance, Social Sciences, and Fintech',
                 hero_description='LIAFE Research Centre specialises in research and development for social sciences, fintech, Islamic finance, and Shariah studies.',
                 cta_title='Ready to learn more about Research House?',
                 cta_button_text='Get in Touch', cta_button_link='/contact/'),
            dict(slug='publication', title='Publication', menu_title='Publication',
                 icon_class='Publication', order=3,
                 short_description='Books, articles, journal papers, and thought leadership that turn insight into impact.',
                 hero_title='Research, Insights, and Global Perspectives',
                 hero_description='LIAFE publications turn insight into impact. Our books and articles bring knowledge to life, offering ideas that inspire growth, ethics, and innovation.',
                 cta_title='Ready to learn more about Publication?',
                 cta_button_text='Get in Touch', cta_button_link='/contact/'),
        ]
        for s in services:
            Service.objects.create(**s)
        self.stdout.write('Services created.')

    # ── ServiceFeatures ───────────────────────────────────────────────────────
    def _seed_service_features(self):
        from services.models import Service, ServiceFeature
        if ServiceFeature.objects.exists():
            return
        try:
            shariah = Service.objects.get(slug='shariah-advisory')
            academy = Service.objects.get(slug='academy')
            research = Service.objects.get(slug='research-house')
        except Service.DoesNotExist:
            return

        features = [
            # Shariah process steps
            (shariah, 'process', 'Client Consultation',      'Understanding business model, jurisdictional context, and Shariah objectives.',         0),
            (shariah, 'process', 'Shariah Review',           'Detailed review of contracts, products, and operational flows against Shariah standards.', 1),
            (shariah, 'process', 'Structuring',              'Designing or restructuring products and instruments to achieve Shariah compliance.',      2),
            (shariah, 'process', 'Shariah Endorsement',      'Formal endorsement from qualified scholars supported by reasoned legal opinion.',         3),
            (shariah, 'process', 'Documentation Review',     'Legal documentation audited for consistency with the endorsed Shariah structure.',        4),
            (shariah, 'process', 'Implementation Monitoring','Continuous oversight during launch to ensure operational fidelity to the approved design.',5),
            (shariah, 'process', 'Shariah Audit',            'Periodic independent audit covering products, transactions, and operational practices.',   6),
            (shariah, 'process', 'Reporting & Disclosure',   'Board-ready Shariah reports and public disclosures aligned with regulatory expectations.', 7),
            # Shariah cards
            (shariah, 'card', 'Shariah Structuring',   'End-to-end product and transaction structuring grounded in classical and contemporary fiqh.',   0),
            (shariah, 'card', 'Product Development',   'Designing Sukuk, takaful, Murabaha, Ijarah, and bespoke compliant financial solutions.',        1),
            (shariah, 'card', 'Shariah Review',        'Independent review of documents, contracts, and processes for institutional and retail clients.',2),
            (shariah, 'card', 'Compliance Screening',  'Equity, asset, and portfolio screening using leading methodologies and scholar-approved criteria.',3),
            (shariah, 'card', 'Fatwa Issuance',        'Reasoned legal opinions delivered by qualified Shariah scholars for new and complex matters.',    4),
            (shariah, 'card', 'Documentation',         'Drafting and reviewing Shariah governance, policies, and procedural frameworks.',                5),
            (shariah, 'card', 'Shariah Audit',         'Risk-based audit programmes covering products, transactions, and operational practices.',         6),
            (shariah, 'card', 'Ongoing Compliance',    'Continuous monitoring and advisory relationships for sustained Shariah governance.',              7),
            # Academy delivery modes
            (academy, 'delivery', 'Online Courses',          'Self-paced and cohort-based programmes via our learning platform.',                       0),
            (academy, 'delivery', 'Face-to-face Training',   'Executive masterclasses and structured cohorts delivered in-person.',                     1),
            (academy, 'delivery', 'Webinars',                'Live and recorded webinars with practitioners and visiting scholars.',                    2),
            (academy, 'delivery', 'Professional Workshops',  'Short-form intensive sessions on focused practitioner topics.',                           3),
            # Research values
            (research, 'value', 'Insightful Research',   'Rigorous, evidence-led work that addresses the questions practitioners and policymakers face.',0),
            (research, 'value', 'Innovative Solutions',  'Frameworks and prototypes that translate research into deployable tools and methodologies.',   1),
            (research, 'value', 'Global Impact',         'Industry partnerships and policy briefs that shape outcomes at institutional and national level.',2),
        ]
        for svc, itype, title, desc, order in features:
            ServiceFeature.objects.create(service=svc, item_type=itype, title=title, description=desc, order=order)
        self.stdout.write('ServiceFeatures created.')
