from django.contrib import admin
from platformproject.models import *
from platformproject.form import *
import random
import hashlib

admin.site.site_header = '东南亚数据后台运维管理系统'
admin.site.site_title = '东南亚数据后台运维'

#生成大小写字母加数字的随机码
def radm():
    code_list = []
    code = ''
    for i in range(50):
        code_list.append(chr(int(random.random() * 1000000 % 26 + 65)))
        code_list.append(chr(int(random.random() * 1000000 % 26 + 97)))
        code_list.append(int(random.random() * 1000000 % 9))
    random.shuffle(code_list)
    code_list = random.sample(code_list,32)
    for i in code_list:
        code = code + str(i)
    return code

#密码处理
def hash(value,code):
    hash = hashlib.md5(code.encode('utf-8'))
    hash.update(value.encode('utf-8'))
    print(code)
    _password_ = hash.hexdigest()
    print(_password_)
    return _password_

@admin.register(user)
class ContactAdmin(admin.ModelAdmin):
    #fields = ('user_name', 'user_email','user_vip','user_status')
    list_display = ('user_name','user_email','user_vip','user_status')
    exclude = ('user_key',)
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-user_reg_time',)
    #list_editable 设置默认可编辑字段
    #list_editable = ['user_email', 'user_vip','user_status']
    #readonly_fields = ('user_name','user_hashpas',)
    form = UserInfo
    def save_model(self, request, obj, form, change):
        obj.user_name = request.POST.get('user_name')
        password = request.POST.get('user_hashpas')
        _code_ = radm()
        obj.user_key = _code_
        _password_ = hash(password,_code_)
        obj.user_hashpas = _password_
        obj.user_email = request.POST.get('user_email')
        obj.user_vip = request.POST.get('user_vip')
        obj.user_status = request.POST.get('user_status')
        obj.save()


@admin.register(rof_day_data,rofid_day_data)
class rof_data_Admin(admin.ModelAdmin):
    list_display = ('operationtime','channel', 'loginaccount','newaddaccount', 'payrate','loginarpu','dayrun','payrolenum','payarpu','tworemain','threeremain','sevenremain',
                    'twoLTV','threeLTV','sevenLTV','exchangemoney')
    ordering = ('-operationtime',)

@admin.register(e3kid_day_data)
class e3kid_data_Admin(admin.ModelAdmin):
    list_display = (
    'operationtime', 'channel', 'dau', 'loginaccount', 'dnu', 'dayrun', 'dnupay', 'f_pay',
    'payrolenum', 'dnupaynum', 'f_paynum', 'paynum',
    'dnupaycount', 'arppu', 'arpu', 'AVEdnupay','payrate')
    ordering = ('-operationtime',)

class rof_data_Admin(admin.ModelAdmin):
    list_display = ('keyid','name', 'mod_name','power_id')


admin.site.register(Menu,rof_data_Admin)

#admin.site.register(rof_day_data,rof_data_Admin)
# Register your models here.
