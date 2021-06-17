from django.contrib import admin
from django.urls import path

from tours.views import (
    custom_handler404,
    custom_handler500,
)
from tours.views import (
    main_view,
    departure_view,
    tour_view,
)

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('departure/<str:departure_code>/', departure_view, name='departure'),
    path('tour/<int:tour_id>/', tour_view, name='tour'),
]
