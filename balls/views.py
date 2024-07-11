import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Report

def display_ball(request):

    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        userId = data['userId']
        count = data['count']

        if Report.objects.filter(user=userId).exists():
            r = Report.objects.get(user=userId)
            r.count = count
            r.save()
        else:
            new_r = Report()
            new_r.user = userId
            new_r.color = data['color']
            new_r.count = count
            new_r.save()

    return render(request, 'balls.HTML', {})

def get_report(request):

    report_list = []

    for report in Report.objects.all():
        report_list.append([report.user, report.color, report.count])   

    return HttpResponse(json.dumps(report_list))
