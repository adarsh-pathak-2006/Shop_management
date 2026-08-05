from rest_framework.throttling import UserRateThrottle

class CoreThrottle(UserRateThrottle):
    rate="30/minute"