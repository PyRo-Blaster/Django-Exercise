# Recruitment exercise

Set `DJANGO_SECRET_KEY` to a newly generated private value. Set `DJANGO_DEBUG=true` only for local development, and configure `DJANGO_ALLOWED_HOSTS` for your deployment.

Configure `LDAP_AUTH_URL`, `LDAP_AUTH_SEARCH_BASE`, `LDAP_AUTH_CONNECTION_USERNAME`, and `LDAP_AUTH_CONNECTION_PASSWORD` through the environment when using LDAP. LDAP TLS defaults to enabled.

Create a fresh local database using `python manage.py migrate`, then create your own administrator with `python manage.py createsuperuser`. Do not commit databases or credentials.
