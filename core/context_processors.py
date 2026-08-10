from .models import SiteSetting


def site_settings(request):
    from pages.models import NavigationMenuItem
    from services.models import Service
    nav_items = NavigationMenuItem.objects.filter(is_active=True).select_related('page')
    nav_services = Service.objects.filter(is_active=True).order_by('order')
    return {
        'site':         SiteSetting.load(),
        'nav_items':    nav_items,
        'nav_services': nav_services,
    }
