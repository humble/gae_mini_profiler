import json

from django.template import Library, loader, Context

from gae_mini_profiler import profiler

register = Library()


@register.simple_tag
def profiler_includes_request_id(request_id, show_immediately=False):
    if not request_id:
        return ''

    template = loader.get_template('../templates/includes.html')
    return template.render(Context({
        'request_id': request_id,
        'js_path': '/gae_mini_profiler/static/js/profiler.js',
        'css_path': '/gae_mini_profiler/static/css/profiler.css',
        'show_immediately_js': json.dumps(show_immediately),
    }))


@register.simple_tag
def profiler_includes():
    return profiler_includes_request_id(profiler.request_id)
