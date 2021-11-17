from django.urls import path

from .views import index, other_page, BBLogonView, profile, BBlogoutView, ChangeUserInfoView, BBPasswordChangeview, \
    RegisterUserView, RegisterDoneView, user_activate, DeleteUserView, BBPaswordResetView, BBPasswordResetCompleteView, \
    BBPasswordResetConfirmView, BBPasswordResetDoneView, by_rubric, detail, profile_bb_detail, profile_bb_add, \
    profile_bb_change, profile_bb_delete

app_name = 'main'
urlpatterns = [
    path('accounts/register/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/register/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBlogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPasswordChangeview.as_view(), name='password_change'),
    path('accounts/password/reset/', BBPaswordResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/done/', BBPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password/confirm/complete/', BBPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/password/confirm/<uidb64>/<token>/', BBPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('acoounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name= 'profile_bb_delete'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLogonView.as_view(), name='login'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
