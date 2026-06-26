from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def index(request):
    return HttpResponse(
        """
        <h1>Магазин запущен</h1>
        <p>Django-проект магазина успешно работает через Docker Compose.</p>
        <ul>
            <li><a href="/shop/">Магазин</a></li>
            <li><a href="/admin/">Админ-панель</a></li>
        </ul>
        """,
        content_type="text/html; charset=utf-8",
    )


urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("shop/", include("shopapp.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )