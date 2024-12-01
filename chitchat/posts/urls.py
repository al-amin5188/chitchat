from django.urls import path
from . import views

urlpatterns = [
    
    # URL to create a post
    path('post/create/', views.create_post, name='create_post'),  

    # URL to update a post
    path('post/<int:post_id>/update/', views.update_post, name='update_post'),  

    # URL to delete a post
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  


    # Like a post
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),

    # Save a post
    path('post/<int:post_id>/save/', views.save_post, name='save_post'),

    # Like a comment
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),

    # Add a comment to a post
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
