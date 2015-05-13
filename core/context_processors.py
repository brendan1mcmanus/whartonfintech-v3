from django.conf import settings

def third_party_integrations(request):
  return {
    'render_analytics': settings.ANALYTICS_ENABLED and not request.user.is_staff,
    'google_analytics_tracking_id': settings.GOOGLE_ANALYTICS_TRACKING_ID,
  }
