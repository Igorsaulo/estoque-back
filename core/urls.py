from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.urls import users_urls
from products.urls import product_urls

api_doc = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_urls)),
    path('api/doc/', include(api_doc)),
    path('products/', include(product_urls)),
]
