from rest_framework import pagination


class PostViewSetPagination(pagination.PageNumberPagination):
    page_size = 4
