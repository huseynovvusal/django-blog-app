from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class LimitOffsetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'limit': self.page_size,
            'count': self.page.paginator.count,
            'current': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
