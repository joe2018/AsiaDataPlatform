from django.db import models

class Menu(models.Model):
    keyid = models.IntegerField(verbose_name= '菜单编号')
    name = models.CharField(verbose_name= '菜单名',max_length=30,primary_key=True)
    mod_name = models.CharField(verbose_name= '所属模块',max_length=30)
    power_id = models.IntegerField(verbose_name= '所属权限')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MENUTABLE'


class user(models.Model):
    user_id = models.AutoField(verbose_name= '用户ID',primary_key=True)
    user_name = models.CharField(verbose_name= '用户名', max_length=13)
    user_hashpas = models.CharField(verbose_name= '密码', max_length=32)
    user_key = models.CharField(verbose_name= '识别码', max_length=32)
    user_email = models.EmailField(verbose_name= '邮箱')
    user_vip = models.IntegerField(verbose_name= '权限等级',default='1')
    user_status = models.IntegerField(verbose_name= '账号状态',default='1')
    user_reg_time = models.DateTimeField(verbose_name= '注册时间',auto_now_add=True)

    class Meta:
        db_table = 'USERINFO'


class rof_day_data(models.Model):
    id = models.IntegerField(primary_key=True)
    channel = models.CharField(verbose_name = '渠道',max_length=300)
    dau = models.IntegerField(verbose_name = '老用户数')
    loginaccount = models.IntegerField(verbose_name = '活跃')
    payrate = models.DecimalField(verbose_name = '付费率',max_digits=8, decimal_places=4)
    loginarpu = models.DecimalField(verbose_name = 'arpu',max_digits=8, decimal_places=4)
    dayrun = models.DecimalField(verbose_name = '日流水',max_digits=8, decimal_places=4)
    payrolenum = models.IntegerField(verbose_name = '付费人数')
    payarpu = models.DecimalField(verbose_name = 'arppu',max_digits=8, decimal_places=4)
    newaddaccount = models.IntegerField(verbose_name = '新增用户')
    dnupay = models.DecimalField(verbose_name = '新玩家付费',max_digits=8, decimal_places=4)
    dnupaynum = models.IntegerField(verbose_name = '新玩家付费人数')
    dnurate = models.DecimalField(verbose_name = '新玩家付费率',max_digits=8, decimal_places=4)
    dnuarppu = models.DecimalField(verbose_name = '新玩家arppu',max_digits=8, decimal_places=4)
    dnuarpu = models.DecimalField(verbose_name = '新玩家arpu',max_digits=8, decimal_places=4)
    oldpay = models.DecimalField(verbose_name = '老玩家付费',max_digits=8, decimal_places=4)
    oldpaynum = models.IntegerField(verbose_name = '老玩家付费人数')
    oldrate = models.DecimalField(verbose_name = '老玩家付费率',max_digits=8, decimal_places=4)
    oldarppu = models.DecimalField(verbose_name = '老玩家arppu',max_digits=8, decimal_places=4)
    oldarpu = models.DecimalField(verbose_name = '老玩家arpu',max_digits=8, decimal_places=4)
    operationtime = models.DateTimeField(verbose_name = '日期')
    tworemain = models.DecimalField(verbose_name = '2留',max_digits=8, decimal_places=4)
    threeremain = models.DecimalField(verbose_name = '3留',max_digits=8, decimal_places=4)
    fourremain = models.DecimalField(verbose_name = '4留',max_digits=8, decimal_places=4)
    fiveremain = models.DecimalField(verbose_name = '5留',max_digits=8, decimal_places=4)
    sixremain = models.DecimalField(verbose_name = '6留',max_digits=8, decimal_places=4)
    sevenremain = models.DecimalField(verbose_name = '7留',max_digits=8, decimal_places=4)
    fourteenremain = models.DecimalField(verbose_name = '14留',max_digits=8, decimal_places=4)
    monthremain = models.DecimalField(verbose_name = '月留',max_digits=8, decimal_places=4)
    twoLTV = models.DecimalField(verbose_name = 'LTV2',max_digits=8, decimal_places=4)
    threeLTV = models.DecimalField(verbose_name = 'LTV3',max_digits=8, decimal_places=4)
    fourLTV = models.DecimalField(verbose_name = 'LTV4',max_digits=8, decimal_places=4)
    fiveLTV = models.DecimalField(verbose_name = 'LTV5',max_digits=8, decimal_places=4)
    sixLTV = models.DecimalField(verbose_name = 'LTV6',max_digits=8, decimal_places=4)
    sevenLTV = models.DecimalField(verbose_name = 'LTV7',max_digits=8, decimal_places=4)
    fourteenLTV = models.DecimalField(verbose_name = 'LTV14',max_digits=8, decimal_places=4)
    monthLTV = models.DecimalField(verbose_name = 'LTV30',max_digits=8, decimal_places=4)
    twomonthLTV = models.DecimalField(verbose_name = 'LTV60',max_digits=8, decimal_places=4)
    exchangemoney = models.DecimalField(verbose_name = '外币',max_digits=15, decimal_places=4)

    class Meta:
        db_table = 'rof_day_data'
        ordering = ['operationtime']

class rofid_day_data(models.Model):
    id = models.IntegerField(primary_key=True)
    channel = models.CharField(verbose_name = '渠道',max_length=300)
    dau = models.IntegerField(verbose_name = '老用户数')
    loginaccount = models.IntegerField(verbose_name = '活跃')
    payrate = models.DecimalField(verbose_name = '付费率',max_digits=8, decimal_places=4)
    loginarpu = models.DecimalField(verbose_name = 'arpu',max_digits=8, decimal_places=4)
    dayrun = models.DecimalField(verbose_name = '日流水',max_digits=8, decimal_places=4)
    payrolenum = models.IntegerField(verbose_name = '付费人数')
    payarpu = models.DecimalField(verbose_name = 'arppu',max_digits=8, decimal_places=4)
    newaddaccount = models.IntegerField(verbose_name = '新增用户')
    dnupay = models.DecimalField(verbose_name = '新玩家付费',max_digits=8, decimal_places=4)
    dnupaynum = models.IntegerField(verbose_name = '新玩家付费人数')
    dnurate = models.DecimalField(verbose_name = '新玩家付费率',max_digits=8, decimal_places=4)
    dnuarppu = models.DecimalField(verbose_name = '新玩家arppu',max_digits=8, decimal_places=4)
    dnuarpu = models.DecimalField(verbose_name = '新玩家arpu',max_digits=8, decimal_places=4)
    oldpay = models.DecimalField(verbose_name = '老玩家付费',max_digits=8, decimal_places=4)
    oldpaynum = models.IntegerField(verbose_name = '老玩家付费人数')
    oldrate = models.DecimalField(verbose_name = '老玩家付费率',max_digits=8, decimal_places=4)
    oldarppu = models.DecimalField(verbose_name = '老玩家arppu',max_digits=8, decimal_places=4)
    oldarpu = models.DecimalField(verbose_name = '老玩家arpu',max_digits=8, decimal_places=4)
    operationtime = models.DateTimeField(verbose_name = '日期')
    tworemain = models.DecimalField(verbose_name = '2留',max_digits=8, decimal_places=4)
    threeremain = models.DecimalField(verbose_name = '3留',max_digits=8, decimal_places=4)
    fourremain = models.DecimalField(verbose_name = '4留',max_digits=8, decimal_places=4)
    fiveremain = models.DecimalField(verbose_name = '5留',max_digits=8, decimal_places=4)
    sixremain = models.DecimalField(verbose_name = '6留',max_digits=8, decimal_places=4)
    sevenremain = models.DecimalField(verbose_name = '7留',max_digits=8, decimal_places=4)
    fourteenremain = models.DecimalField(verbose_name = '14留',max_digits=8, decimal_places=4)
    monthremain = models.DecimalField(verbose_name = '月留',max_digits=8, decimal_places=4)
    twoLTV = models.DecimalField(verbose_name = 'LTV2',max_digits=8, decimal_places=4)
    threeLTV = models.DecimalField(verbose_name = 'LTV3',max_digits=8, decimal_places=4)
    fourLTV = models.DecimalField(verbose_name = 'LTV4',max_digits=8, decimal_places=4)
    fiveLTV = models.DecimalField(verbose_name = 'LTV5',max_digits=8, decimal_places=4)
    sixLTV = models.DecimalField(verbose_name = 'LTV6',max_digits=8, decimal_places=4)
    sevenLTV = models.DecimalField(verbose_name = 'LTV7',max_digits=8, decimal_places=4)
    fourteenLTV = models.DecimalField(verbose_name = 'LTV14',max_digits=8, decimal_places=4)
    monthLTV = models.DecimalField(verbose_name = 'LTV30',max_digits=8, decimal_places=4)
    twomonthLTV = models.DecimalField(verbose_name = 'LTV60',max_digits=8, decimal_places=4)
    exchangemoney = models.DecimalField(verbose_name = '外币',max_digits=15, decimal_places=4)

    class Meta:
        db_table = 'rofid_day_data'
        ordering = ['operationtime']

class e3kid_day_data(models.Model):
    id = models.IntegerField(primary_key=True)
    operationtime = models.DateTimeField(verbose_name='日期')
    channel = models.CharField(verbose_name = '渠道',max_length=300)
    dau = models.IntegerField(verbose_name = '活跃')
    loginaccount = models.IntegerField(verbose_name = '登入次数')
    dnu = models.IntegerField(verbose_name='新增用户')
    dayrun = models.DecimalField(verbose_name='日流水', max_digits=8, decimal_places=4)
    dnupay = models.DecimalField(verbose_name='新玩家付费', max_digits=8, decimal_places=4)
    f_pay = models.DecimalField(verbose_name='首冲金额', max_digits=8, decimal_places=4)
    payrolenum = models.IntegerField(verbose_name='付费人数')
    dnupaynum = models.IntegerField(verbose_name='新玩家付费人数')
    f_paynum = models.DecimalField(verbose_name='首冲金额', max_digits=8, decimal_places=4)
    paynum = models.IntegerField(verbose_name='充值次数')
    dnupaycount = models.IntegerField(verbose_name='新用户充值次数')
    arppu = models.DecimalField(verbose_name='arppu', max_digits=8, decimal_places=4)
    arpu = models.DecimalField(verbose_name='arpu', max_digits=8, decimal_places=4)
    AVEdnupay = models.DecimalField(verbose_name='新用户平均付费', max_digits=8, decimal_places=4)
    payrate = models.DecimalField(verbose_name = '付费率',max_digits=8, decimal_places=4)

    class Meta:
        db_table = 'e3kid_day_data'
        ordering = ['operationtime']