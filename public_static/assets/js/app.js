$(function() {

        var dataType = $('body').attr('data-type');
            for (key in pageData) {
                if (key == dataType) {
                    pageData[key]();
                }
            }

        var $fullText = $('.admin-fullText');
        $('#admin-fullscreen').on('click', function() {
            $.AMUI.fullscreen.toggle();
        });

        $(document).on($.AMUI.fullscreen.raw.fullscreenchange, function() {
            $fullText.text($.AMUI.fullscreen.isFullscreen ? '退出全屏' : '开启全屏');
        });




        $('.tpl-switch').find('.tpl-switch-btn-view').on('click', function() {
            $(this).prev('.tpl-switch-btn').prop("checked", function() {
                    if ($(this).is(':checked')) {
                        return false
                    } else {
                        return true
                    }
                })


        })
    })
    // ==========================
    // 侧边导航下拉列表
    // ==========================

$('.tpl-left-nav-link-list').on('click', function() {
        $(this).siblings('.tpl-left-nav-sub-menu').slideToggle(80)
            .end()
            .find('.tpl-left-nav-more-ico').toggleClass('tpl-left-nav-more-ico-rotate');
    })
    // ==========================
    // 头部导航隐藏菜单
    // ==========================

$('.tpl-header-nav-hover-ico').on('click', function() {
    $('.tpl-left-nav').toggle();
    $('.tpl-content-wrapper').toggleClass('tpl-content-wrapper-hover');
})

// 页面数据
var pageData = {
    // ===============================================
    // 首页
    // ===============================================
    'index': function indexData() {
		var myDate = new Date();
		var Year = myDate.getFullYear();
		var month = myDate.getMonth()+1;
		change_month(String(Year)+String(month))
        document.getElementById("change_time").value = String(Year)+'年'+String(month)+'日';


        var myScroll = new IScroll('#wrapper', {
            scrollbars: true,
            mouseWheel: true,
            interactiveScrollbars: true,
            shrinkScrollbars: 'scale',
            preventDefault: false,
            fadeScrollbars: true
        });

        var myScrollA = new IScroll('#wrapperA', {
            scrollbars: true,
            mouseWheel: true,
            interactiveScrollbars: true,
            shrinkScrollbars: 'scale',
            preventDefault: false,
            fadeScrollbars: true
        });

        var myScrollB = new IScroll('#wrapperB', {
            scrollbars: true,
            mouseWheel: true,
            interactiveScrollbars: true,
            shrinkScrollbars: 'scale',
            preventDefault: false,
            fadeScrollbars: true
        });


		
        // document.addEventListener('touchmove', function(e) { e.preventDefault(); }, false);

        // ==========================
        // 百度图表A http://echarts.baidu.com/
        // ==========================

        var echartsA = echarts.init(document.getElementById('tpl-echarts-A'));
        option = {

            tooltip: {
                trigger: 'axis',
            },
            legend: {
                data: ['邮件', '媒体', '资源']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                boundaryGap: true,
                data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
            }],

            yAxis: [{
                type: 'value'
            }],
            series: [{
                    name: '邮件',
                    type: 'line',
                    stack: '总量',
                    areaStyle: { normal: {} },
                    data: [120, 132, 101, 134, 90, 230, 210],
                    itemStyle: {
                        normal: {
                            color: '#59aea2'
                        },
                        emphasis: {

                        }
                    }
                },
                {
                    name: '媒体',
                    type: 'line',
                    stack: '总量',
                    areaStyle: { normal: {} },
                    data: [220, 182, 191, 234, 290, 330, 310],
                    itemStyle: {
                        normal: {
                            color: '#e7505a'
                        }
                    }
                },
                {
                    name: '资源',
                    type: 'line',
                    stack: '总量',
                    areaStyle: { normal: {} },
                    data: [150, 232, 201, 154, 190, 330, 410],
                    itemStyle: {
                        normal: {
                            color: '#32c5d2'
                        }
                    }
                }
            ]
        };
        echartsA.setOption(option);

    },
    // ===============================================
    // 图表页
    // ===============================================
    'chart': function chartData() {
        // ==========================
        // 百度图表A http://echarts.baidu.com/
        // ==========================

        var echartsC = echarts.init(document.getElementById('tpl-echarts-C'));
        optionC = {
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                top: '0',
                feature: {
                    dataView: { show: true, readOnly: false },
                    magicType: { show: true, type: ['line', 'bar'] },
                    restore: { show: true },
                    saveAsImage: { show: true }
                }
            },
            legend: {
                data: ['蒸发量', '降水量', '平均温度']
            },
            xAxis: [{
                type: 'category',
                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
            }],
            yAxis: [{
                    type: 'value',
                    name: '水量',
                    min: 0,
                    max: 250,
                    interval: 50,
                    axisLabel: {
                        formatter: '{value} ml'
                    }
                },
                {
                    type: 'value',
                    name: '温度',
                    min: 0,
                    max: 25,
                    interval: 5,
                    axisLabel: {
                        formatter: '{value} °C'
                    }
                }
            ],
            series: [{
                    name: '蒸发量',
                    type: 'bar',
                    data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
                },
                {
                    name: '降水量',
                    type: 'bar',
                    data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
                },
                {
                    name: '平均温度',
                    type: 'line',
                    yAxisIndex: 1,
                    data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
                }
            ]
        };

        echartsC.setOption(optionC);

        var echartsB = echarts.init(document.getElementById('tpl-echarts-B'));
        optionB = {
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                x: 'center',
                data: ['某软件', '某主食手机', '某水果手机', '降水量', '蒸发量']
            },
            radar: [{
                    indicator: [
                        { text: '品牌', max: 100 },
                        { text: '内容', max: 100 },
                        { text: '可用性', max: 100 },
                        { text: '功能', max: 100 }
                    ],
                    center: ['25%', '40%'],
                    radius: 80
                },
                {
                    indicator: [
                        { text: '外观', max: 100 },
                        { text: '拍照', max: 100 },
                        { text: '系统', max: 100 },
                        { text: '性能', max: 100 },
                        { text: '屏幕', max: 100 }
                    ],
                    radius: 80,
                    center: ['50%', '60%'],
                },
                {
                    indicator: (function() {
                        var res = [];
                        for (var i = 1; i <= 12; i++) {
                            res.push({ text: i + '月', max: 100 });
                        }
                        return res;
                    })(),
                    center: ['75%', '40%'],
                    radius: 80
                }
            ],
            series: [{
                    type: 'radar',
                    tooltip: {
                        trigger: 'item'
                    },
                    itemStyle: { normal: { areaStyle: { type: 'default' } } },
                    data: [{
                        value: [60, 73, 85, 40],
                        name: '某软件'
                    }]
                },
                {
                    type: 'radar',
                    radarIndex: 1,
                    data: [{
                            value: [85, 90, 90, 95, 95],
                            name: '某主食手机'
                        },
                        {
                            value: [95, 80, 95, 90, 93],
                            name: '某水果手机'
                        }
                    ]
                },
                {
                    type: 'radar',
                    radarIndex: 2,
                    itemStyle: { normal: { areaStyle: { type: 'default' } } },
                    data: [{
                            name: '降水量',
                            value: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 75.6, 82.2, 48.7, 18.8, 6.0, 2.3],
                        },
                        {
                            name: '蒸发量',
                            value: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 35.6, 62.2, 32.6, 20.0, 6.4, 3.3]
                        }
                    ]
                }
            ]
        };
        echartsB.setOption(optionB);
        var echartsA = echarts.init(document.getElementById('tpl-echarts-A'));
        option = {

            tooltip: {
                trigger: 'axis',
            },
            legend: {
                data: ['邮件', '媒体', '资源']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                boundaryGap: true,
                data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
            }],

            yAxis: [{
                type: 'value'
            }],
            series: [{
                    name: '邮件',
                    type: 'line',
                    stack: '总量',
                    areaStyle: { normal: {} },
                    data: [120, 132, 101, 134, 90, 230, 210],
                    itemStyle: {
                        normal: {
                            color: '#59aea2'
                        },
                        emphasis: {

                        }
                    }
                },
                {
                    name: '媒体',
                    type: 'line',
                    stack: '总量',
                    areaStyle: { normal: {} },
                    data: [220, 182, 191, 234, 290, 330, 310],
                    itemStyle: {
                        normal: {
                            color: '#e7505a'
                        }
                    }
                },
                {
                    name: '资源',
                    type: 'line',
                    stack: '总量',
                    areaStyle: { normal: {} },
                    data: [150, 232, 201, 154, 190, 330, 410],
                    itemStyle: {
                        normal: {
                            color: '#32c5d2'
                        }
                    }
                }
            ]
        };
        echartsA.setOption(option);
    },
    'game': function gameData() {
        var myDate = new Date();
		var Year = myDate.getFullYear();
		var month = myDate.getMonth()+1;
		var day = myDate.getDate();
		month= month<10?"0"+month:month;
		day= day<10?"0"+day:day;
		document.getElementById("star_time").value = String(Year)+'-'+String(month)+'-01';
		document.getElementById("end_time").value = String(Year)+'-'+String(month)+'-'+String(day);
        $('#data_search').on('click',function () {
            var star_time = $('#star_time').val();
            var end_time = $('#end_time').val();
            $('#example').DataTable().ajax.reload();
        })
        if (game_id == 1 | game_id ==2){
            var columns= [
                    {data: 'operationtime'},
                    {data: 'channel'},
                    {data: 'newaddaccount'},
                    {data: 'loginaccount'},
                    {data: 'dayrun'},
                    {data: 'payrolenum'},
                    {data: 'payrate'},
                    {data: 'loginarpu'},
                    {data: 'payarpu'},
                    {data: 'tworemain'},
                    {data: 'threeremain'},
                    {data: 'sevenremain'},
                    {data: 'fourteenremain'},
                    {data: 'monthremain'},
                    {data: 'twoLTV'},
                    {data: 'threeLTV'},
                    {data: 'sevenLTV'},
                    {data: 'fourteenLTV'},
                    {data: 'monthLTV'},
                ]
        }else{
            var columns= [
                    {data: 'operationtime'},
                    {data: 'channel'},
                    {data: 'dau'},
                    {data: 'loginaccount'},
                    {data: 'dnu'},
                    {data: 'dayrun'},
                    {data: 'dnupay'},
                    {data: 'f_pay'},
                    {data: 'payrolenum'},
                    {data: 'dnupaynum'},
                    {data: 'f_paynum'},
                    {data: 'paynum'},
                    {data: 'dnupaycount'},
                    {data: 'arppu'},
                    {data: 'arpu'},
                    {data: 'AVEdnupay'},
                    {data: 'payrate'},
                ]
        }
        dt_rofth(game_id,columns)
        function dt_rofth(game_id,columns) {
         var table = $('#example').DataTable({
                "info": false,
                "paging": true,
                "processing": true,
                "ordering":false,//thead上的排序按钮
                "bLengthChange": true,//分页条数选择按钮
                "bProcessing": true,//显示加载中
                "bInfo": true,//页脚信息显示
                "searching": false,//搜索输入框显示
                "sPaginationType": "full_numbers",//分页显示样式
                "scrollX": true,//左右滚动条
                "iDisplayLength":10,//每页显示数
                "stripeClasses": [ 'strip1', 'strip2', 'strip3' ],//斑马线
                "order": [ 0, 'desc' ],
                "aLengthMenu" : [ [ 10, 25, -1 ], [ "10", "25", "所有" ] ],
                                     "oLanguage": {
                                    "sLengthMenu": "每页显示 _MENU_  条",
                                    "sZeroRecords": "没有找到符合条件的数据",
                                    "sProcessing": "正在加载数据...",
                                    "sInfo": "当前第 _START_ - _END_ 条　共计 _TOTAL_ 条",
                                    "sInfoEmpty": "没有有记录",
                                    "sInfoFiltered": "(从 _MAX_ 条记录中过滤)",
                                    "sSearch": "搜索：",
                                    "oPaginate": {
                                        "sFirst": "首页",
                                        "sPrevious": "前一页",
                                        "sNext": "后一页",
                                        "sLast": "尾页"
                                    }
                        },
                //使用对象数组，一定要配置columns，告诉 DataTables 每列对应的属性
                //data 这里是固定不变的，name，position，salary，office 为你数据里对应的属性
                columns: columns,
                //开启服务器模式
                serverSide: false,
                //使用ajax异步请求
                ajax: {
                    type: 'post',
                    url: '/game_data/',
                    data: function (d) {
                        d.star_time = $('#star_time').val();
                        d.end_time = $('#end_time').val();
                        d.gameid =game_id
                    }
                }
         });
        }
    }
}
//获取链接参数
function getQueryString() {
  var qs = location.search.substr(1), // 获取url中"?"符后的字串
    args = {}, // 保存参数数据的对象
    items = qs.length ? qs.split("&") : [], // 取得每一个参数项,
    item = null,
    len = items.length;

  for(var i = 0; i < len; i++) {
    item = items[i].split("=");
    var name = decodeURIComponent(item[0]),
      value = decodeURIComponent(item[1]);
    if(name) {
      args[name] = value;
    }
  }
  return args;
}

function datechange() {
    date_option = {isShowClear:false,readOnly:true,skin:'whyGreen',dateFmt:'yyyy年M月',minDate:'2018-1',maxDate:'%y-%M',position:{left:-50,top:-70},onpicked:pickedFunc}
    WdatePicker(date_option)
    return WdatePicker
}

function star_time() {
    date_option = {isShowClear:false,readOnly:true,skin:'whyGreen',minDate:'2018-1-1',position:{left:-50,top:-70},maxDate:'%y-%M-%d',maxDate:'#F{$dp.$D(\'end_time\')}'}
    WdatePicker(date_option)
    return WdatePicker
}

function end_time() {
    date_option = {isShowClear:false,readOnly:true,skin:'whyGreen',minDate:'2018-1-1',position:{left:-50,top:-70},maxDate:'%y-%M-%d',minDate:'#F{$dp.$D(\'star_time\')}'}
    WdatePicker(date_option)
    return WdatePicker
}

function pickedFunc() {
    c_year = $dp.cal.getP('y');
    c_month = $dp.cal.getP('M');
    change_month(c_year+c_month)

}

function change_month(month){
    $.post("/m_money/",{'cha_time':month},function(ret) {
        $('#m_money').html(ret.all_money );
        $('#all_dnu').html(ret.all_dnu );
        $('#Avg_payrate').html(ret.Avg_payrate+'%' );
        $('#rate').html(ret.rate+'%' );
        $('#ltv').html(ret.ltv );
        $('#nowmon').html(ret.mon+'月' );
        $('#est_money').html(ret.est_money);
        $('#est_rate').html(ret.est_rate+'%' );
        $('#all_rate').html(ret.all_rate+'%' );
        $('#est_all_rate').html(ret.est_all_rate+'%' );
        $('#dunpay_rate').html(ret.dunpay_rate+'%' );
        $('#Avg_arpu').html(ret.Avg_arpu );
        $('#Avg_arppu').html(ret.Avg_arppu);
        $('#ios_ltv').html(ret.ios_ltv);
        $('#and_ltv').html(ret.and_ltv);
        $('#and_num').html(ret.and_num);
        $('#ios_num').html(ret.ios_num);
        $('#ios_money').html(ret.ios_money);
        $('#and_money').html(ret.and_money);
    });
}
function ALERTCLACK(content) {
    AMUI.dialog.alert({
        title: '提示',
        content: content,
        onConfirm: function () {
            console.log('close');
        }
       })
}