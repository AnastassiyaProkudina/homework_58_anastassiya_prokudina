from django.views.generic import TemplateView, RedirectView

from issue_tracker.models import Issue


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issues"] = Issue.objects.exclude(is_deleted=True).order_by("-id")
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
