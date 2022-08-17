from weather_data.models import search_results
from datetime import datetime

def upload_search(data, year, code):
    """Thsi function is to upload Search results."""
    val = search_results.objects.create(area_searched= code, year= year, data= data)

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)