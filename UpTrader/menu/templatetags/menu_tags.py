# menu/templatetags/menu_tags.py
from django import template
from django.urls import NoReverseMatch, resolve, reverse
from menu.models import Menu, MenuItem
from collections import defaultdict

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {"menu_items": []}

    items = menu.items.select_related("parent").all()

    tree = defaultdict(list)
    item_dict = {}

    active_item = None

    for item in items:
        item_dict[item.id] = item
        tree[item.parent_id].append(item)

        # Получаем URL пункта
        try:
            item_url = reverse(item.named_url) if item.named_url else item.url
        except NoReverseMatch:
            item_url = item.url

        # Проверка точного совпадения с текущим URL
        if item_url == request.path and active_item is None:
            active_item = item

    def get_open_ids(item):
        ids = set()
        while item:
            ids.add(item.id)
            item = item.parent
        return ids

    open_ids = get_open_ids(active_item) if active_item else set()

    def build_menu(items, level=0):
        result = []
        for item in items:
            children = tree.get(item.id, [])
            result.append(
                {
                    "item": item,
                    "children": build_menu(children, level + 1),
                    "is_active": item == active_item,
                    "is_open": item.id in open_ids,
                }
            )
        return result

    structured_menu = build_menu(tree[None])
    return {"menu_items": structured_menu}
