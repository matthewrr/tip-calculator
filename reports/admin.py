from django.contrib import admin
from .models import *

class ReportAdmin(admin.ModelAdmin):
    pass
    # fields = ["start_date"]
    # list_display = ["start_date"]
                    # "start_date","end_date","is_active","timestamp","submitter",
                    # "rev_total","rev_hourly","rev_method","cash_tips","cc_tips",
                    # "total_tips","tips_paid","tips_pull_amount","tips_pull_time",
                    # "worked_minutes","bartender_rate","barback_rate","security_rate"
                    # )
    # notes = models.TextField(default="")
    # list_filter = ("email", "is_staff", "is_active",)
    # search_fields = ("start_date",)
    # ordering = ("start_date",)
class TimecardAdmin(admin.ModelAdmin):
    # fields = ["start_date"]
    list_display = ("employee", "report")


admin.site.register(Report, ReportAdmin)
admin.site.register(Timecard, TimecardAdmin)
