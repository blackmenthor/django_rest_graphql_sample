from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from sample_api import settings
from sample_api.views import CustomGraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backoffice/', admin.site.urls),
    path('animal/', include('animal.urls')),
    path('animal_keeper/', include('keeper.urls')),
    path('gallery/', include('gallery.urls')),
    path(
        'graphql/',
        csrf_exempt(
            CustomGraphQLView.as_view(
                graphiql=settings.DEBUG,
                pretty=True,
            )
        ),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
