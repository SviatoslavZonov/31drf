from django.urls import path

from measurement.views import SensorsView, AddMeasurement, SensorUpdate


urlpatterns = [
    path("sensors/", SensorsView.as_view()),
    path("sensors/<pk>/", SensorUpdate.as_view()),
    path("measurements/<pk>/", AddMeasurement.as_view()),
]
