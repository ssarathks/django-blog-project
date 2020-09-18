from django.conf.urls import url
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name="post_list"),
    url(r'^post_create/$',views.PostCreateView.as_view(),name="post_create"),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name="post_detail"),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name="post_update"),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name="post_delete"),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name="post_publish"),
    url(r'^drafts/$',views.DraftListView.as_view(),name="drafts"),
    url(r'^post/(?P<pk>\d+)/add_comment$',views.add_comment_to_post,name="add_comment"),
    url(r'^comment/(?P<pk>\d+)/approve$',views.comment_approve,name="comment_approve"),
    url(r'^comment/(?P<pk>\d+)/delete$',views.comment_delete,name="comment_delete"),  
    url(r'^counter/',views.counter,name="counter"),
    url(r'^change_counter/(?P<action>[-\w]+)/$',views.change_counter,name="change_counter"),
    url(r'^search/$',views.search,name="search"),

    # url(r'^increase_counter/(?P<action>[-\w]+)/$',views.increase_counter,name="increase_counter"),
    # url(r'^decrease_counter/$',views.decrease_counter,name="decrease_counter"),


    
]
