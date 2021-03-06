from rest_framework import viewsets

from wp_news.models import NewsEntry
from wp_news.serializers import NewsEntrySerializer
from wp_news.permissions import ReadOnlyAccess
# Create your views here.


class NewsEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyAccess]
    queryset = NewsEntry.objects.filter(published=True)
    serializer_class = NewsEntrySerializer
