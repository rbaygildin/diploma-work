"""neurdicom URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from neurdicom import settings

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  # path('api-auth/', include('rest_framework.urls')),
                  # path('api/', include('apps.dicom_ws.urls'))
                  # path('', IndexView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       url(r'^dev/debug', include(debug_toolbar.urls)),
#                   ] + urlpatterns

PATIENT_LIST_URL = r'/api/patients'
PATIENT_DETAIL_URL = r'/api/patients/(\d+)'
PATIENT_STUDIES_URL = r'/api/patients/(\d+)/studies'

STUDY_LIST_URL = r'/api/studies'
STUDY_DETAIL_URL = r'/api/studies/(\d+)'
STUDY_SERIES_URL = r'/api/studies/(\d+)/series'

SERIES_LIST_URL = r'/api/series'
SERIES_DETAIL_URL = r'/api/series/(\d+)'
SERIES_INSTANCES_URL = r'/api/series/(\d+)/instances'

INSTANCE_LIST_URL = r'/api/instances'
INSTANCE_UPLOAD_URL = r'/api/instances/upload'
INSTANCE_DETAIL_URL = r'/api/instances/(\d+)'
INSTANCE_IMAGE_URL = r'/api/instances/(\d+)/image'
INSTANCE_RAW_URL = r'/api/instances/(\d+)/raw'
INSTANCE_TAGS_URL = r'/api/instances/(\d+)/tags'
INSTANCE_PROCESS_URL = r'/api/instances/(\d+)/process/by_plugin/(\d+)'

DICOM_NODE_LIST_URL = r'/api/dicom_nodes'
DICOM_NODE_DETAIL_URL = r'/api/dicom_nodes/(\d+)'
DICOM_NODE_ECHO_URL = r'/api/dicom_nodes/(\d+)/echo'

PLUGIN_LIST_URL = r'/api/plugins'
PLUGIN_DETAIL_URL = r'/api/plugins/(\d+)'
PLUGIN_INSTALL_URL = r'/api/plugins/(\d+)/install'

MEDIA_URL = r'/media/(.*)'

