from django.shortcuts import render
from django.http import JsonResponse
from accounts.models import CustomUser
from reports.models import *

from datetime import datetime, timedelta
import json
import pytz


def find_item(request):
    employees = CustomUser.objects.filter(is_active=True).order_by('first_name')
    hours_reg = {
        "2:00PM": "14", "3:00PM": "15", "4:00PM": "16", "5:00PM": "17",
        "6:00PM": "18", "7:00PM": "19", "8:00PM": "20", "9:00PM": "21",
        "10:00PM": "22", "11:00PM": "23", "12:00AM": "00", "1:00AM": "01",
        "2:00AM": "02", "3:00AM": "03",
    }
    context = {'employees': employees,
               'hours_reg': hours_reg,
               'title': "Home"
               }
    return render(request, 'getdata/body.html', context)

def support(request):
    context = {"title": "Support"}
    return render(request, 'getdata/support.html', context)

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def create_timecards(report_pk, start_date, end_date, timecards={}):
    report = Report.objects.get(id=report_pk)
    for pk, value in timecards.items():
        employee = CustomUser.objects.get(id=pk)

        start_hour = int(value['hours']['start']['hour'])
        start_min = int(value['hours']['start']['minute'])
        end_hour = int(value['hours']['end']['hour'])
        end_min = int(value['hours']['end']['minute'])

        if not (start_hour in range(5, 24) and end_hour in range(0, 4)):
            end_date = start_date + timedelta(days=0) #better way for shallow copy?

        start_time = start_date.replace(hour=start_hour, minute=start_min)
        end_time = end_date.replace(hour=end_hour, minute=end_min)

        t = Timecard(
            report = report,
            employee = employee,
            role = value['role'],
            start_time = str(start_time),
            end_time = str(end_time),
            # wage = 0,
            minutes_total = value['hours']['minsWorked'],
            minutes_hourly = json.dumps(value['hours']['workedByHour']),
            earned_total = 0, #value['earnings']['totalEarnings'],
            earned_hourly = json.dumps(value['earnings']['earningsByHour']),
            earned_tips = value['earnings']['tipEarnings'],
            tips_to_report = value['earnings']['tipsToReport']
        )
        t.save()

def create_report(data={}):
    #COMBINE START TIME WITH START DATE??
    # print(my_obj.timecard_set.all())

    #DONT ENTER UNTIL VALIDATED
    #ACTIVE = TRUE... not always. Same initial submissions.
    start_date = datetime.fromtimestamp(data['start-date']/1000.0, tz=pytz.UTC)
    end_date = datetime.fromtimestamp(data['end-date']/1000.0, tz=pytz.UTC)
    submitted = datetime.fromtimestamp(data['submitted']/1000.0, tz=pytz.UTC)
    submitter_pk = data['submitter-pk']
    submitter_name = CustomUser.objects.get(id=submitter_pk)
    total_tips = float(data['tips-cc']) + float(data['tips-cash'])


    print("----------------------------------------")
    print(data['rev-total'])
    print(type(data['rev-total']))

    #should I use id or pk? both work. #if statements for pull
    #rounding tips put onto frontend. tacking roundings.


    #2024 Sept 14
    rev_total = data['rev-total'].split(',')
    print(rev_total)
    "".join(rev_total)
    print(rev_total)
    mynew = rev_total[0] + rev_total[1]
    print(mynew)
    print(type(mynew))
    mynew = float(mynew)
    print(mynew)
    rev_total = mynew
    

    t = Report(
        start_date = start_date,
        end_date = end_date,
        timestamp = submitted,
        is_active = True, #hard coded
        submitter_pk = submitter_pk, #update
        submitter_name = submitter_name,
        rev_total = rev_total,
        rev_hourly = json.dumps(data['rev-hourly']),
        rev_method = data['rev-method'],
        cash_tips = data['tips-cash'],
        cc_tips = data['tips-cc'],
        total_tips = total_tips,
        tips_paid = data['tips-paid'], #determined by summing all "tips to report"
        tips_diff = total_tips - data['tips-paid'], #total_tips - tips paid (account for pos and neg)
        tips_pull_amount = 0, 
        worked_minutes = 120,
        bartender_rate = float(data['bartender-rate'])/100,
        barback_rate = float(data['barback-rate'])/100,
        security_rate = float(data['security-rate'])/100
        #different in tips earned v paid
        # tips_pull_time = data['pull-time'],

    )
    t.save()
    create_timecards(t.pk, start_date, end_date, data['timecards'])


def security_rates(timecards):
    # security_hourly = {"14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "00":0, "01":0, "02":0, "03":0}
    # time_order = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2]
    security_hourly = [["14",0], ["15",0], ["16",0], ["17",0], ["18",0], ["19",0], ["20",0], ["21",0], ["22",0], ["23",0], ["00",0], ["01",0], ["02",0]]
    time_order = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "00", "01", "02"]

    start_time = {
        'index': len(time_order) - 1,
        'hour': time_order[-1],
        'minute': 59
    }

    for values in timecards.values():
        if values['role'] == "SECURITY":
            start_hour = values['hours']['start']['hour']
            start_minute = int(values['hours']['start']['minute'])
            start_index = time_order.index(start_hour)

            if start_index <= start_time['index']:
                start_time['index'] = start_index
                start_time['hour'] = start_hour
            
            if start_index == start_time['index']:
                if start_minute < start_time['minute']:
                    start_time['minute'] = start_minute
            else:
                start_time['minute'] = start_minute
    

    for i in range(start_time['index'], len(time_order)-1):
        print("i is...")
        print(i)
        if i == start_time['index']:
            hourly_portion = (60-start_time['minute'])/60
            security_hourly[start_time['index']][1] = hourly_portion
        else:
            security_hourly[i][1] = 1.0

    print('IM PRINTING THEM FOR YOU BBY')

    sec_rates = {}
    for i in security_hourly:
        k = i[0]
        v = i[1]
        sec_rates[k] = v

    return sec_rates

def validate_data(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('formData'))
        start_date = datetime.fromtimestamp(data['start-date']/1000.0)
        timecards = data['timecards']
        
        barback_rate =float(data['barback-rate'])/100
        security_rate = float(data['security-rate'])/100

        #Uuuupppppppdddaaaattteeeee
        bartender_rate = (float(data['bartender-rate'])/100)#+ security_rate

        print('Printing Timecards')
        pretty(timecards)

        print("Printing Hourly Security Rate")
        sec_rate = security_rates(timecards)
        print(sec_rate)

        for values in timecards.values():

            start_hour = values['hours']['start']['hour']
            start_minute = int(values['hours']['start']['minute'])
            end_hour = values['hours']['end']['hour']
            end_minute = int(values['hours']['end']['minute'])
            role = values['role']

            x = True

            mins = 60-start_minute
            values['hours']['workedByHour'][start_hour] = mins;
            while x == True:
                #mess up if hour worked is before rev listed hour (or something different?)
                # do this way before... set bartender rate to combined and security at 0 for each hour auto
                data['hours'][start_hour]['role']['SECURITY']['tipRate'] = security_rate


                # print([type(start_hour), start_hour])
                # NEW STUFF

                data['hours'][start_hour]['role']['SECURITY']['tipRate'] = security_rate * sec_rate[start_hour]
                # data['hours'][start_hour]['role']['BARTENDER']['tipRate'] = bartender_rate
                data['hours'][start_hour]['role']['BARTENDER']['tipRate'] = (bartender_rate + security_rate) - (security_rate * sec_rate[start_hour])

                print(["Security Rate:", security_rate * sec_rate[start_hour]])
                print(["Bartender Rate:", (bartender_rate + security_rate) - (security_rate * sec_rate[start_hour])])
                       
                    #    (security_rate * sec_rate[start_hour])])





                

                if start_hour == end_hour:
                    mins = end_minute
                    x = False
                    values['hours']['workedByHour'][start_hour] = mins
                    data['hours'][start_hour]['role'][role]['minutesWorked'] += mins

                    if values['role'] == "SECURITY":
                        
                        logged_min = data['hours'][start_hour]["securityMinutes"]
                        if logged_min < end_minute:
                            data['hours'][start_hour]["securityMinEnd"] = end_minute
                            percent_hour = end_minute/60

                            security_rate_hour = security_rate*percent_hour
                            bartender_rate_hour = bartender_rate-security_rate_hour

                        data['hours'][start_hour]['role']['SECURITY']['tipRate'] = security_rate_hour
                        data['hours'][start_hour]['role']['BARTENDER']['tipRate'] = bartender_rate_hour
                
                    break

                values['hours']['workedByHour'][start_hour] = mins;
                data['hours'][start_hour]['role'][role]['minutesWorked'] += mins
    
                if values['role'] == "SECURITY":

                    logged_min = data['hours'][start_hour]["securityMinutes"]
                    if logged_min < end_minute:
                        data['hours'][start_hour]["securityMinEnd"] = end_minute
                    start_min = mins*1;
                    percent_hour = start_min/60

                    security_rate_hour = security_rate*percent_hour
                    bartender_rate_hour = bartender_rate-security_rate_hour

                    data['hours'][start_hour]['role']['SECURITY']['tipRate'] = security_rate_hour
                    data['hours'][start_hour]['role']['BARTENDER']['tipRate'] = bartender_rate_hour
                    #WHAT IF MORE NSECURITY? CHOOSE GREATER OF VALUES
                    
                mins = 60

                if start_hour != "23":
                    start_hour = str(int(start_hour) + 1)
                    if len(start_hour) == 1:
                        start_hour = "0" + start_hour
                else:
                    start_hour = "00"

        for value in data['hours'].values():
            for role,v in value['role'].items():
                value['role'][role]['tipsEarned'] = value["tips"] * value["role"][role]["tipRate"]
        
        tips_paid = 0 
        tips_total_report = 0
        
        for values in timecards.values():
            total_tips = 0
            role = values['role']

            for hour, v in values['earnings']['earningsByHour'].items():
                hourly_tips = 0
                employeeWorkedMins = values['hours']['workedByHour'][hour]
                minsByRole = data['hours'][hour]['role'][role]['minutesWorked']
                tipsByRole = data['hours'][hour]['role'][role]['tipsEarned']
                
                if minsByRole:
                    hourly_tips = (employeeWorkedMins/minsByRole) * tipsByRole

                total_tips += hourly_tips
                values['earnings']['earningsByHour'][hour] = hourly_tips
            
            total_tips = round(total_tips, 2)
            values['earnings']['tipEarnings'] = total_tips


            tips_to_report = round(total_tips * (float(data['tips-cc-rate'])/100), 2)
            values['earnings']['tipsToReport'] = tips_to_report
            tips_paid += total_tips
            tips_total_report += tips_to_report
            # better naming for tip rates by role
            
        data['tips-paid'] = tips_paid
        data['tips-total-report'] = tips_total_report #ADD TO MODEL
        # sum to tips paid after rounding
        # pretty(data)
        # print(data['hours']['17']['role']['BARTENDER'].keys())
        # print(data['timecards'].keys())
        # print('-----------')
        # print(data['hours'])
        # print('-----------')
        # print(data['hours']['18']['role']['BARTENDER'])
        # print(data['hours']['role']['BARTENDER'])
        create_report(data)
        return JsonResponse(data)
    return JsonResponse({'status': 'error'})