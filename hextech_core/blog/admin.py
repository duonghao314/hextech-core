from django.contrib import admin
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.core.fields import RichTextField

from hextech_core.blog.models import Blog, BlogCategory


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


class BlogCategoryWagtail(ModelAdmin):
    model = BlogCategory
    menu_label = "Blog Categories"
    menu_icon = "list-ul"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "parent")
    search_fields = ("name",)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name", classname="name"),
                FieldPanel("parent", classname="parent"),
                FieldPanel("slug", classname="slug"),
            ],
            heading="Category Info",
        ),
        FieldPanel("metadata"),
    ]


class BlogWagtail(ModelAdmin):
    model = Blog
    menu_label = "Blogs"
    menu_icon = "doc-empty"
    menu_order = 120
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "author", "category", "created_at")
    search_fields = ("title", "author")
    content = RichTextField()
    # edit_template_name = "wagtail/blog/blog_post_page.html"

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title", classname="title"),
                FieldPanel("author", classname="author"),
                FieldPanel("category", classname="category"),
                # RichTextFieldPanel('content', classname='content'),
                FieldPanel("content", classname="content"),
                FieldPanel("slug", classname="slug"),
                FieldRowPanel(
                    [
                        FieldPanel("published", classname="published"),
                        FieldPanel("published_at", classname="published_at"),
                    ]
                ),
            ],
            heading="Blog content",
        ),
        FieldPanel("metadata"),
    ]


class BlogsAppWagtailAdmin(ModelAdminGroup):
    menu_label = "My Blog"
    menu_icon = "thumbtack"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        BlogCategoryWagtail,
        BlogWagtail,
    )


modeladmin_register(BlogsAppWagtailAdmin)
