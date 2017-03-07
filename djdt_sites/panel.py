from debug_toolbar.panels import Panel


class SitesPanel(Panel):
    """This panel shows a list of all existing sites and allows the user to
    switch between them.
    """
    title = "Sites"
    has_content = True
    template = 'ddt_sites/panel.html'

    @property
    def nav_subtitle(self):
        try:
            return self.get_stats().get('current').domain
        except AttributeError:
            return ''

    def generate_stats(self, request, response):
        from django.contrib.sites.models import Site
        self.record_stats({
            'current': request.site,
            'sites': [
                {
                    'site': site,
                    'is_current': site == request.site,
                }
                for site in Site.objects.all().order_by('pk')
            ],
        })
