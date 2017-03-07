DjDT Sites panel
================

``DjDT Sites`` adds a ``Sites`` panel that lists all registered sites and allows
to easily switch from one to another during development.

.. image:: https://raw.githubusercontent.com/Nicals/djdt-sites/master/screenshot.png
   :width: 934
   :height: 341

Install
-------

Install using ``pip``:

  pip install djdt-sites

Add ``djdt_sites`` to ``INSTALLED_APPS`` so that we can find the panel templates.
Obviously, you must have ``django.contrib.sites`` in the ``INSTALLED_APPS`` too.

Add ``djdt_sites.SitesPanel`` to ``DEBUG_TOOLBAR_PANELS``.

Add ``djdt_sites.switch_site_middleware`` to ``MIDDLEWARE`` after any other site
selection middleware.
``switch_site_middleware`` is responsible to override the current site on demand.

This uses a ``site`` attribute of the request object to manage the current site.
The ``django.contrib.sites.middleware.CurrentSiteMiddleware`` provides this
functionnality and must be enabled before the ``djdt_sites`` middleware.

The ``SitesPanel`` uses the ``request.sites`` attribute to display
the current sites. Therefore, the ``djdt_sites`` middleware must be set 
before the debug toolbar one.

.. code:: python

    MIDDLEWARE = [
      # ...
      'django.contrib.sites.middleware.CurrentSiteMiddleware',
      'djdt_sites.middleware.switch_site_middleware',
      'debug_toolbar.middleware.DebugToolbarMiddleware',
      # ...
    ]
