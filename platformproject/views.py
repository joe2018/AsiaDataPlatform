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
    return render(request, 'index.html')

def rofth_data(request):

    return render(request, 'game_data.html',{'game_id':1,'title': '梦幻之翼泰国','type':1})

def rofid_data(request):

    return render(request, 'game_data.html',{'game_id':2,'title': '梦幻之翼印尼','type':1})

def e3kid_data(request):

    return render(request, 'game_data.html',{'game_id':3,'title': '乱轰三国印尼','type':2})

def range_time(*args):
    cha_time_list = []
    year = int(datetime.datetime.now().strftime("%Y"))
    Month = int(datetime.datetime.now().strftime("%m"))
    daynub = monthrange(year, Month)[1]
    date_from = datetime.datetime(year, Month, 1, 0, 0, tzinfo=timezone.utc)
    date_to = datetime.datetime(year, Month, daynub, 0, 0, tzinfo=timezone.utc)
    cha_time_list.append(date_from)
    cha_time_list.append(date_to)
    return cha_time_list

def m_money(request):
    if request.method == 'POST':
        if 'cha_time' in request.POST:
            chg = request.POST['cha_time']
            date_from = datetime.datetime(int(chg[:4]), int(chg[4:]), 1, 0, 0, tzinfo=timezone.utc)
            daynub = monthrange(int(chg[:4]), int(chg[4:]))[1]
            date_to = datetime.datetime(int(chg[:4]), int(chg[4:]), daynub, 0, 0, tzinfo=timezone.utc)
        else:
            cha_time_list = range_time()
            date_from = cha_time_list[0]
            date_to = cha_time_list[1]
        day = int(datetime.datetime.now().strftime("%d"))
        Month = int(datetime.datetime.now().strftime("%m"))
        rofmoney_th = rof_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(Sum('dayrun'),Sum('newaddaccount'),Avg('payrate'),Avg('payarpu'),Avg('loginarpu'),Sum('dnupay'))
        rofmoney_id = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(Sum('dayrun'),Sum('newaddaccount'),Avg('payrate'),Avg('payarpu'),Avg('loginarpu'),Sum('dnupay'))
        e3kmoney_id = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(Sum('dayrun'),Sum('dnu'),Avg('payrate'),Avg('arppu'),Avg('arpu'),Sum('dnupay'))
        all_money = rofmoney_th['dayrun__sum']+rofmoney_id['dayrun__sum']+e3kmoney_id['dayrun__sum']
        all_dnu = rofmoney_th['newaddaccount__sum']+rofmoney_id['newaddaccount__sum']+e3kmoney_id['dnu__sum']
        Avg_payrate = (rofmoney_th['payrate__avg']+rofmoney_id['payrate__avg']+(e3kmoney_id['payrate__avg']*100))/3
        rate = (float(all_money)*0.7)/158980*100
        all_rate = float(all_money) / 158980 * 100
        if int(chg[4:]) == Month:
            est_rate = rate / (day - 1) * 30
            est_all_rate = all_rate/(day-1)*30
            est_money = all_money / (day - 1) * 30
        else:
            est_rate = rate
            est_all_rate = all_rate
            est_money = all_money
        Avg_arppu = (rofmoney_th['payarpu__avg']+rofmoney_id['payarpu__avg']+(e3kmoney_id['arppu__avg']))/3
        Avg_arpu = (rofmoney_th['loginarpu__avg']+rofmoney_id['loginarpu__avg']+(e3kmoney_id['arpu__avg']))/3
        sum_dunpay = rofmoney_th['dnupay__sum'] + rofmoney_id['dnupay__sum'] + e3kmoney_id['dnupay__sum']
        dunpay_rate = sum_dunpay/all_money*100
        rof_th = rof_day_data.objects.aggregate(Sum('dayrun'),Sum('newaddaccount'))
        rof_id = rofid_day_data.objects.aggregate(Sum('dayrun'), Sum('newaddaccount'))
        e3k_id = e3kid_day_data.objects.aggregate(Sum('dayrun'), Sum('dnu'))
        a_money = rof_th['dayrun__sum'] + rof_id['dayrun__sum'] + e3k_id['dayrun__sum']
        a_dnu = rof_th['newaddaccount__sum'] + rof_id['newaddaccount__sum'] + e3k_id['dnu__sum']
        ltv = a_money/a_dnu
        rofadn_th = rof_day_data.objects.filter(operationtime__range=(date_from, date_to),channel__iexact='Android').aggregate(Sum('newaddaccount'),Sum( 'dayrun'))
        rofadn_id = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to),channel__iexact='Android').aggregate(Sum('newaddaccount'), Sum(
            'dayrun'))
        rofios_th = rof_day_data.objects.filter(operationtime__range=(date_from, date_to),channel__iexact='iOS').aggregate(Sum('newaddaccount'),Sum( 'dayrun'))
        rofios_id = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to),channel__iexact='iOS').aggregate(Sum('newaddaccount'), Sum(
            'dayrun'))
        e3kadn_id = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to),channel__iexact='android').aggregate(Sum('dnu'),Sum('dayrun'))
        e3kios_id = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to),channel__iexact='ios').aggregate(Sum('dnu'),Sum('dayrun'))
        and_num = (rofadn_th['newaddaccount__sum']+rofadn_id['newaddaccount__sum']+(e3kadn_id['dnu__sum']))
        print(rofadn_th['newaddaccount__sum'],rofadn_id['newaddaccount__sum'],(e3kadn_id['dnu__sum']))
        ios_num = (rofios_th['newaddaccount__sum']+rofios_id['newaddaccount__sum']+(e3kios_id['dnu__sum']))
        print(rofios_th['newaddaccount__sum'],rofios_id['newaddaccount__sum'],(e3kios_id['dnu__sum']))
        and_money = (rofadn_th['dayrun__sum']+rofadn_id['dayrun__sum']+(e3kadn_id['dayrun__sum']))
        ios_money = (rofios_th['dayrun__sum'] + rofios_id['dayrun__sum'] + (e3kios_id['dayrun__sum']))
        and_ltv = and_money/and_num
        ios_ltv = ios_money/ios_num
        return JsonResponse({'ios_money':'%.2f' % ios_money,'and_money':'%.2f' % and_money,'ios_num':ios_num,'and_num':and_num,'ios_ltv':'%.2f' % ios_ltv,'and_ltv':'%.2f' % and_ltv,'dunpay_rate':'%.2f' % dunpay_rate,'Avg_arpu':'%.2f' % Avg_arpu,'Avg_arppu':'%.2f' % Avg_arppu,'est_all_rate':'%.2f' % est_all_rate,'est_money':'%.2f' % est_money,'est_rate':'%.2f' % est_rate,'all_rate':'%.2f' % all_rate,'all_money': '%.2f' % all_money,'all_dnu':all_dnu,'Avg_payrate': '%.2f' % Avg_payrate,'rate': '%.2f' % rate,'ltv': '%.2f' % ltv,'mon':int(date_to.strftime('%m'))} )


def game_data(request):
    if request.method == 'POST':
        mydata =[]
        if 'star_time' and  'end_time' in request.POST:
            star_time = request.POST['star_time']
            end_time = request.POST['end_time']
            date_from = datetime.datetime.strptime(star_time, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            date_to = datetime.datetime.strptime(end_time, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        else:
            cha_time_list = range_time()
            date_from = cha_time_list[0]
            date_to = cha_time_list[1]
        gameid = request.POST['gameid']
        if int(gameid) == 1:
            mon_data = rof_day_data.objects.filter(operationtime__range=(date_from, date_to))
            rof_thid = rof_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(
                Sum('dayrun'), Sum('newaddaccount'), Avg('payrate'), Avg('loginarpu'), Avg('payarpu'),
                Sum('payrolenum'), Avg('tworemain'), Avg('threeremain'), Avg('sevenremain'), Avg('fourteenremain'),
                Avg('monthremain'), Avg('twoLTV'), Avg('threeLTV'), Avg('sevenLTV'), Avg('fourteenLTV'),
                Avg('monthLTV'))
        elif int(gameid) == 2 :
            mon_data = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to))
            rof_thid = rofid_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(
                Sum('dayrun'), Sum('newaddaccount'), Avg('payrate'), Avg('loginarpu'), Avg('payarpu'),
                Sum('payrolenum'), Avg('tworemain'), Avg('threeremain'), Avg('sevenremain'), Avg('fourteenremain'),
                Avg('monthremain'), Avg('twoLTV'), Avg('threeLTV'), Avg('sevenLTV'), Avg('fourteenLTV'),
                Avg('monthLTV'))
        elif int(gameid) == 3:
            mon_data = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to))
            e3k_id = e3kid_day_data.objects.filter(operationtime__range=(date_from, date_to)).aggregate(
                Sum('loginaccount'), Sum('dnu'), Sum('dayrun'), Sum('dnupay'), Sum('f_pay'), Sum('payrolenum'),
                Sum('f_paynum'), Avg('paynum'), Avg('arppu'), Avg('arpu'), Avg('AVEdnupay'), Avg('payrate'))
            tump = {}
            tump['operationtime'] = '合计'
            tump['channel'] = '-'
            tump['dau'] = '-'
            tump['loginaccount'] = e3k_id['loginaccount__sum']
            tump['dnu'] = e3k_id['dnu__sum']
            tump['dayrun'] = '%.2f' % float(e3k_id['dayrun__sum'])
            tump['dnupay'] = '%.2f' % float(e3k_id['dnupay__sum'])
            tump['f_pay'] = '%.2f' % float(e3k_id['f_pay__sum'])
            tump['payrolenum'] = e3k_id['payrolenum__sum']
            tump['dnupaynum'] = '-'
            tump['f_paynum'] = '%.2f' % float(e3k_id['f_paynum__sum'])
            tump['paynum'] = e3k_id['paynum__avg']
            tump['dnupaycount'] = '-'
            tump['arppu'] = '%.2f' % float(e3k_id['arppu__avg'])
            tump['arpu'] = '%.2f' % float(e3k_id['arpu__avg'])
            tump['AVEdnupay'] = '%.2f' % (float(e3k_id['AVEdnupay__avg']))
            tump['payrate'] = str('%.2f' % (float(e3k_id['payrate__avg']) * 100)) + "%"
            mydata.append(tump)
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
                tump['AVEdnupay'] = '%.2f' % (float(i.AVEdnupay))
                tump['payrate'] = str('%.2f' % (float(i.payrate)*100)) + "%"
                mydata.append(tump)

            return JsonResponse({'data': mydata})

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
        return JsonResponse({'data': mydata})

