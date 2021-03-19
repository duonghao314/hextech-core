from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from hextech_core.blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


class BlogWagtailAdmin(ModelAdmin):
    model = Blog
    menu_label = "Blogs"
    menu_icon = "doc-empty"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author")


class BlogsAppWagtailAdmin(ModelAdminGroup):
    menu_label = "My Blog"
    menu_icon = "folder-open-inverse"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BlogWagtailAdmin,)


modeladmin_register(BlogsAppWagtailAdmin)
