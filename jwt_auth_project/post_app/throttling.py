from rest_framework import throttling

class PostUserRateThrottle(throttling.UserRateThrottle):
    scope = "post_throttle"
