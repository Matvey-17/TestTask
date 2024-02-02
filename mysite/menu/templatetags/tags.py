from django import template
from menu.models import Menu

register = template.Library()


def get_all_menu(menu_items):
    all_menu = [menu_items]
    if menu_items.children.all():
        menu_items.children.all().update(is_active=True)
    while menu_items.parent:
        menu_items = menu_items.parent
        all_menu.insert(0, menu_items)
    return all_menu


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    Menu.objects.all().update(is_active=False)
    menu_item = Menu.objects.filter(name=menu_name).select_related('parent').first()
    current_url = context['request'].path
    if menu_item:
        get_menu = get_all_menu(menu_item)
        Menu.objects.filter(id__in=[item.id for item in get_menu]).update(is_active=True)
        return {'menu_items': get_menu[0], 'current_url': current_url}
    return {'menu_items': [], 'current_url': current_url}


@register.inclusion_tag('menu/menu_item.html')
def draw_menu_recursive(menu):
    return {'menu': menu}
