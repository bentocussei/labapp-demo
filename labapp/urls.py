from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from escolas import views

schema_view = get_schema_view(
   openapi.Info(
      title="LABAPP",
      default_version='v1',
      description="LABAPP é uma API aberta desenvolvida em Django que gerencia informações sobre escolas, permitindo a criação, atualização, exclusão e importação de dados a partir de um arquivo Excel. LABAPP também permite filtrar as escolas com base nas províncias fornecidas no JSON no corpo da requisição.",
      terms_of_service="https://www.linkedin.com/in/bentocussei/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('escolas', views.EscolaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escolas/upload-excel/', views.UploadExcelView.as_view(), name='upload_excel'),
    
    path('', include(router.urls)),
]

# Swagger routes
urlpatterns += [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
