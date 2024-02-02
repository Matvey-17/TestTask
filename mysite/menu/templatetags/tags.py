from django import template
from menu.models import Menu

register = template.Library()


def get_all_menu(menu_items):
    menu_items.is_active = True
    menu_items.save()
    all_menu = [menu_items]
    if menu_items.children.all():
        for item in menu_items.children.all():
            item.is_active = True
            item.save()
    while menu_items.parent:
        menu_items = menu_items.parent
        menu_items.is_active = True
        menu_items.save()
        all_menu.insert(0, menu_items)
    return all_menu


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    default_state = Menu.objects.all()
    for state in default_state:
        state.is_active = False
        state.save()
    menu_item = Menu.objects.filter(name=menu_name).select_related('parent').first()
    current_url = context['request'].path
    print(current_url)
    if menu_item:
        get_menu = get_all_menu(menu_item)
        return {'menu_items': get_menu[0], 'current_url': current_url}
    return {'menu_items': [], 'current_url': current_url}


@register.inclusion_tag('menu/menu_item.html')
def draw_menu_recursive(menu):
    return {'menu': menu}
