from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Avg, Max, Min, Count
from django.http import HttpResponse
from .models import *
import datetime,time
from django.utils import timezone
from calendar import monthrange #获取月份的天数

# Create your views here.

def index(request):
    content = select()
    return render(request, 'index.html',{'content':content})

def rofth_data(request):
    content = select()
    return render(request, 'game_data.html',{'game_id':1,'title': '梦幻之翼泰国','type':1,'content':content})

def rofid_data(request):
    content = select()
    return render(request, 'game_data.html',{'game_id':2,'title': '梦幻之翼印尼','type':1,'content':content})

def e3kid_data(request):
    content = select()
    return render(request, 'game_data.html',{'game_id':3,'title': '乱轰三国印尼','type':2,'content':content})

def range_time(*args):
    cha_time_list = []
    print(args)
    if args:
        if str(args[0]) == 'all':
            date_from = datetime.datetime(2018, 1, 1, 0, 0,tzinfo=timezone.utc)
            year = int(datetime.datetime.now().strftime("%Y"))
            Month = int(datetime.datetime.now().strftime("%m"))
            daynub = monthrange(year, Month)[1]
            date_to = datetime.datetime(year, Month, daynub, 0, 0, tzinfo=timezone.utc)
        else:
            year = int(args[0][:4])
            Month = int(args[0][4:])
            daynub = monthrange(year, Month)[1]
            date_from = datetime.datetime(year, Month, 1, 0, 0,tzinfo=timezone.utc)
            date_to = datetime.datetime(year, Month, daynub, 0, 0,tzinfo=timezone.utc)
    else:
        year = int(datetime.datetime.now().strftime("%Y"))
        Month = int(datetime.datetime.now().strftime("%m"))
        daynub = monthrange(year, Month)[1]
        date_from = datetime.datetime(year, Month, 1, 0, 0, tzinfo=timezone.utc)
        date_to = datetime.datetime(year, Month, daynub, 0, 0, tzinfo=timezone.utc)
    cha_time_list.append(date_from)
    cha_time_list.append(date_to)
    return cha_time_list

def select(*args):
    content = {}
    b_year = 2018
    year = int(datetime.datetime.now().strftime("%Y"))
    Month = int(datetime.datetime.now().strftime("%m"))
    for i in range(b_year,year+1):
        if b_year<year:
            for i in range(12,0,-1):
                content['%s-%s' % (b_year,i)] = '%s%s' % (b_year,i)
        if b_year==year:
            for i in range(Month,0,-1):
                content['%s-%s' % (b_year,i)] = '%s%s' % (b_year,i)
        b_year +=1

    return content

def m_money(request):
    if request.method == 'POST':
        if 'cha_time' in request.POST:
            chg = request.POST['cha_time']
            print(chg)
            cha_time_list = range_time(chg)
        else:
            cha_time_list = range_time()
        date_from = cha_time_list[0]
        date_to = cha_time_list[1]
        rofmoney_th = rof_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(Sum('dayrun'),Sum('newaddaccount'),Avg('payrate'))
        rofmoney_id = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(Sum('dayrun'),Sum('newaddaccount'),Avg('payrate'))
        e3kmoney_id = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(Sum('dayrun'),Sum('dnu'),Avg('payrate'))
        rof_th = rof_day_data.objects.aggregate(Sum('dayrun'),Sum('newaddaccount'))
        rof_id = rofid_day_data.objects.aggregate(Sum('dayrun'), Sum('newaddaccount'))
        e3k_id = e3kid_day_data.objects.aggregate(Sum('dayrun'), Sum('dnu'))
        all_money = rofmoney_th['dayrun__sum']+rofmoney_id['dayrun__sum']+e3kmoney_id['dayrun__sum']
        all_dnu = rofmoney_th['newaddaccount__sum']+rofmoney_id['newaddaccount__sum']+e3kmoney_id['dnu__sum']
        Avg_payrate = (rofmoney_th['payrate__avg']+rofmoney_id['payrate__avg']+(e3kmoney_id['payrate__avg']*100))/3
        rate = (float(all_money)*0.7)/158980*100
        #rate = float(all_money) / 158980 * 100
        a_money = rof_th['dayrun__sum'] + rof_id['dayrun__sum'] + e3k_id['dayrun__sum']
        a_dnu = rof_th['newaddaccount__sum'] + rof_id['newaddaccount__sum'] + e3k_id['dnu__sum']
        ltv = a_money/a_dnu
        return JsonResponse({'all_money': '%.2f' % all_money,'all_dnu':all_dnu,'Avg_payrate': '%.2f' % Avg_payrate,'rate': '%.2f' % rate,'ltv': '%.2f' % ltv,'mon':int(date_to.strftime('%m'))} )


def game_data(request):
    if request.method == 'POST':
        mydata =[]
        if 'cha_time' in request.POST:
            chg = request.POST['cha_time']
            cha_time_list = range_time(chg)
        else:
            cha_time_list = range_time()
        date_from = cha_time_list[0]
        date_to = cha_time_list[1]
        #if not gameid:
        gameid = request.POST['gameid']
        if int(gameid) == 1:
            mon_data = rof_day_data.objects.filter(operationtime__range=(date_from, date_to))
        elif int(gameid) == 2 :
            mon_data = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to))
        elif int(gameid) == 3:
            mon_data = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to))
            e3k_id = rof_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(
                Sum('loginaccount'), Sum('dnu'), Sum('dayrun'), Avg('dnupay'), Sum('f_pay'),Sum('payrolenum'), Sum('f_paynum'), Avg('paynum'), Avg('arppu'), Avg('arpu'),Avg('AVEdnupay'),Avg('payrate'))
            for i in mon_data:
                tump = {}
                tump['operationtime'] = i.operationtime.strftime("%Y/%m/%d")
                tump['channel'] = i.channel
                tump['dau'] = i.dau
                tump['loginaccount'] = i.loginaccount
                tump['dnu'] = i.dnu
                tump['dayrun'] = '%.2f' % float(i.dayrun)
                tump['dnupay'] = '%.2f' % float(i.dnupay)
                tump['f_pay'] = '%.2f' % float(i.f_pay)
                tump['payrolenum'] = i.payrolenum
                tump['dnupaynum'] = i.dnupaynum
                tump['f_paynum'] =  '%.2f' % float(i.f_paynum)
                tump['paynum'] = i.paynum
                tump['dnupaycount'] = i.dnupaycount
                tump['arppu'] = '%.2f' % float(i.arppu)
                tump['arpu'] = '%.2f' % float(i.arpu)
                tump['AVEdnupay'] = str('%.2f' % (float(i.AVEdnupay)*100)) + "%"
                tump['payrate'] = str('%.2f' % (float(i.payrate)*100)) + "%"
                mydata.append(tump)
            return JsonResponse({'mydata': mydata,'e3k_id':e3k_id})
        rof_thid = rof_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(
            Sum('dayrun'), Sum('newaddaccount'), Avg('payrate'), Avg('loginarpu'), Avg('payarpu'),Sum('payrolenum'), Avg('tworemain'), Avg('threeremain'), Avg('sevenremain'), Avg('fourteenremain'),Avg('monthremain'),Avg('twoLTV'), Avg('threeLTV'), Avg('sevenLTV'), Avg('fourteenLTV'), Avg('monthLTV'))
        for i in mon_data:
            tump = {}
            tump['operationtime'] = i.operationtime.strftime("%Y/%m/%d")
            tump['channel'] = i.channel
            tump['newaddaccount'] = i.newaddaccount
            tump['loginaccount'] = i.loginaccount
            tump['dayrun'] = '%.2f' % float(i.dayrun)
            tump['payrolenum'] = i.payrolenum
            tump['payrate'] = str(float(i.payrate )) + "%"
            tump['loginarpu'] = '%.2f' % float(i.loginarpu )
            tump['payarpu'] = '%.2f' % float(i.payarpu )
            tump['tworemain'] = str(float(i.tworemain )) + "%"
            tump['threeremain'] = str(float(i.threeremain )) + "%"
            tump['sevenremain'] = str(float(i.sevenremain )) + "%"
            tump['fourteenremain'] = str(float(i.fourteenremain )) + "%"
            tump['monthremain'] = str(float(i.monthremain )) + "%"
            tump['twoLTV'] = '%.2f' % float(i.twoLTV)
            tump['threeLTV'] = '%.2f' % float(i.threeLTV)
            tump['sevenLTV'] = '%.2f' % float(i.sevenLTV)
            tump['fourteenLTV'] = '%.2f' % float(i.fourteenLTV)
            tump['monthLTV'] = '%.2f' % float(i.monthLTV)
            mydata.append(tump)
        return JsonResponse({'data': mydata,'rof_thid':rof_thid})

