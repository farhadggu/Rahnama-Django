from contextlib import suppress

from django.conf import settings


def inject_accept_language(get_response):
    """
    Ignore Accept-Language HTTP headers.

    This will force the I18N machinery to always choose

      - Ukrainian for the main site
      - ADMIN_LANGUAGE_CODE for the admin site

    as the default initial language unless another one is set via
    sessions or cookies.

    Should be installed *before* any middleware that checks
    request.META['HTTP_ACCEPT_LANGUAGE'], namely
    `django.middleware.locale.LocaleMiddleware`.
    """
    admin_lang = getattr(settings, 'ADMIN_LANGUAGE_CODE',
                         settings.LANGUAGE_CODE)

    def middleware(request):
        # Force Ukrainian locale for the main site
        lang = admin_lang if request.path.startswith('/admin') else 'uk'
        accept = request.META.get('HTTP_ACCEPT_LANGUAGE', []).split(',')

        with suppress(ValueError):
            # Remove `lang` from the HTTP_ACCEPT_LANGUAGE to avoid duplicates
            accept.remove(lang)

        accept = [lang] + accept
        request.META['HTTP_ACCEPT_LANGUAGE'] = f"""{','.join(accept)}"""
        return get_response(request)

    return middleware