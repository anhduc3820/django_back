from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Staffs
from .models import Courses
from .models import Subjects
from .models import Students
from .models import Attendance
from .models import AttendanceReport
from .models import LeaveReportStudent
from .models import LeaveReportStaff
from .models import FeedBackStudent
from .models import FeedBackStaffs
from .models import NotificationStudent
from .models import NotificationStaffs
from .models import AdminHOD


# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
