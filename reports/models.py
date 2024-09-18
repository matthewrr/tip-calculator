from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

class Report(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField()
    submitter_name = models.CharField(max_length=30, default="")
    submitter_pk = models.IntegerField(default=0)

    rev_total = models.DecimalField(max_digits=6, decimal_places=2)
    rev_hourly = models.JSONField() #GO FOR 24 HOURS
    rev_method = models.CharField(max_length=30)
    cash_tips = models.DecimalField(max_digits=6, decimal_places=2)
    cc_tips = models.DecimalField(max_digits=6, decimal_places=2)
    total_tips = models.DecimalField(max_digits=6, decimal_places=2)
    tips_paid = models.DecimalField(max_digits=6, decimal_places=2)
    tips_diff = models.DecimalField(max_digits=6, decimal_places=2)
    tips_pull_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    tips_pull_time = models.DateTimeField(blank=True, null=True)

    worked_minutes = models.IntegerField(default=0)

    bartender_rate = models.DecimalField(max_digits=6, decimal_places=2)
    barback_rate = models.DecimalField(max_digits=6, decimal_places=2)
    security_rate = models.DecimalField(max_digits=6, decimal_places=2)

    notes = models.TextField(default="")

    def __str__(self):
        return self.start_date.strftime('%Y-%m-%d')
    
    def date(self):
        pass
        # return self.start_date..strftime('%Y-%m-%d')
        
    def cc_rate(self):
        return self.cc_tips / self.total_tips

    def total_employees(self):
        return #the count of timecards

    # functions for explaining fields?

class Timecard(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=30) # make it possible to add multiple in a day
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    minutes_total = models.IntegerField(default=0)
    minutes_hourly = models.JSONField()
    earned_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    earned_hourly = models.JSONField()
    earned_tips = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    tips_to_report = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # wage (somehow tie hourly from employee model to this since change over time)

    def __str__(self):
        return str(self.employee)

    @property
    def date(self):
        return self.report.start_date

