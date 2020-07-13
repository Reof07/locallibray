from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.book_detail_view, name='book-detail'),
    url(r'^authors/$', views.Authorlist.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.author_detail_view, name='author-detail'),
    ]

urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]