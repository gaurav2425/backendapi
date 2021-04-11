from django.db import models
import datetime
from django.utils.timezone import utc
from django.utils import timezone
from datetime import datetime
import time
# Create your models here.
Day = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

Month = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)


class Trending(models.Model):

    name = models.CharField(max_length=120, default='trending')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='null',)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Hot(models.Model):
    name = models.CharField(max_length=120, default='hot')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class New(models.Model):
    name = models.CharField(max_length=120, default='new')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.CharField(max_length=120, default='')

    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='March'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Amazon(models.Model):
    name = models.CharField(max_length=120, default='amazon')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='null', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Google(models.Model):
    name = models.CharField(max_length=120, default='google')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='', blank=True)
    para2 = models.CharField(max_length=3000, default='', blank=True)
    para3 = models.CharField(max_length=3000, default='', blank=True)
    para4 = models.CharField(max_length=3000, default='', blank=True)
    para5 = models.CharField(max_length=3000, default='', blank=True)
    para6 = models.CharField(max_length=3000, default='', blank=True)
    para7 = models.CharField(max_length=3000, default='', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Microsoft(models.Model):
    name = models.CharField(max_length=120, default='microsoft')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Tesla(models.Model):
    name = models.CharField(max_length=120, default='tesla')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Apple(models.Model):
    name = models.CharField(max_length=120, default='apple')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Facebook(models.Model):
    name = models.CharField(max_length=120, default='facebook')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Privacy(models.Model):
    name = models.CharField(max_length=120, default='privacy')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Cybersecurity(models.Model):
    name = models.CharField(max_length=120, default='cybersecurity')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Netflix(models.Model):
    name = models.CharField(max_length=120, default='netflix')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Sports(models.Model):
    name = models.CharField(max_length=120, default='sports')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Television(models.Model):
    name = models.CharField(max_length=120, default='television')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Films(models.Model):
    name = models.CharField(max_length=120, default='films')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Gaming(models.Model):
    name = models.CharField(max_length=120, default='gaming')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Phones(models.Model):
    name = models.CharField(max_length=120, default='phones')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Laptops(models.Model):
    name = models.CharField(max_length=120, default='laptops')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Cameras(models.Model):
    name = models.CharField(max_length=120, default='cameras')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Headphones(models.Model):
    name = models.CharField(max_length=120, default='headphones')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Speakers(models.Model):
    name = models.CharField(max_length=120, default='speakers')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Youtube(models.Model):
    name = models.CharField(max_length=120, default='youtube')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Instagram(models.Model):
    name = models.CharField(max_length=120, default='instagram')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Linkedin(models.Model):
    name = models.CharField(max_length=120, default='linkedin')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Twitter(models.Model):
    name = models.CharField(max_length=120, default='twitter')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Nasa(models.Model):
    name = models.CharField(max_length=120, default='nasa')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Spacex(models.Model):
    name = models.CharField(max_length=120, default='spacex')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Health(models.Model):
    name = models.CharField(max_length=120, default='health')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Energy(models.Model):
    name = models.CharField(max_length=120, default='energy')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Environment(models.Model):
    name = models.CharField(max_length=120, default='environment')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=120, default='')
    subtitle = models.CharField(max_length=120, default='')
    para1 = models.CharField(max_length=3000, default='')
    para2 = models.CharField(max_length=3000, default='')
    para3 = models.CharField(max_length=3000, default='')
    para4 = models.CharField(max_length=3000, default='')
    para5 = models.CharField(max_length=3000, default='')
    para6 = models.CharField(max_length=3000, default='')
    para7 = models.CharField(max_length=3000, default='')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    videosrc = models.CharField(
        default='https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/UD7CEz6/videoblocks-editorial-amazon-logo-on-glass-building_hwejn98w_b__e76572479d6e0eef1ed47aedc20ca538__P360.mp4', max_length=300)
    youtubevideo = models.CharField(
        default='', max_length=300)
    day = models.CharField(
        max_length=20,
        choices=Day,
        default='Monday'
    )
    month = models.CharField(
        max_length=20,
        choices=Month,
        default='January'
    )
    dateint = models.CharField(max_length=2, default='')
    date = models.DateField(default=timezone.now)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    now = models.TimeField(default=curr_clock)

    def __str__(self):
        return self.title


class Contact(models.Model):
    fullname = models.CharField(max_length=120, default='')
    email = models.CharField(max_length=120, default='')
    message = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.email
