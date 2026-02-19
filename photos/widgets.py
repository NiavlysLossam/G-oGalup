from django.contrib.gis.forms.widgets import OSMWidget

class AzimuthMapWidget(OSMWidget):
    template_name = 'photos/admin/azimuth_map.html'
    
    class Media:
        js = (
            'photos/js/admin_azimuth.js',
        )
