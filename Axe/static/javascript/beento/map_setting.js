var geoCoordMap = '';
var geoCoordMapRegions = ''

var area_name = document.getElementById("script_map").getAttribute('areaName');
var area_grade = document.getElementById("script_map").getAttribute('areaGrade');
var province_js_path = document.getElementById("script_map").getAttribute('provinceJSPath');

// var myChart = echarts.init(document.getElementById('div_beento_main'));

var mainContainer = document.getElementById('div_beento_main');
//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
var resizeMainContainer = function () {
    // mainContainer.style.width = window.innerWidth + 'px';
    mainContainer.style.height = window.innerHeight * 0.8 + 'px';
};
//设置div容器高宽
resizeMainContainer();
// 初始化图表
var myChart = echarts.init(mainContainer);



function geo_inti() {
    var geo_setting = {
        map: area_name,
        aspectScale: 0.75,
        roam: false,
        zoom: 1.2,
        layoutCenter: ['30%', '30%'],
        label: {
            normal: {
                show: true,//显示省份标签
                textStyle: {color: "#afdead"}//省份标签字体颜色
            },
            emphasis: {//对应的鼠标悬浮效果
                show: true,
                textStyle: {color: "#800080"}
            }
        },
        itemStyle: {
            normal: {
                // areaColor: '#323c48',
                // areaColor: '#808080',
                areaColor: '#44566B'
                // borderWidth: 2.5,//区域边框宽度
                // borderColor: '#111'
            }
            ,
            emphasis: {
                // areaColor: '#2a333d'
                // areaColor: '#228B22'
                // borderWidth: 2.5,
                // borderColor: '#4b0082',
                areaColor: '#E5D5A1'
            }
        },
        selectedMode: 'multiple',
        regions: []
    };

    if (area_name === '黑龙江') {
        geo_setting.center = [127.5, 48];
        geo_setting.zoom = 0.80;
    }
    else if (area_name == '辽宁') {
        geo_setting.center = [122.5, 41];
        geo_setting.zoom = 0.85;
    }
    else if (area_name == '内蒙古') {
        geo_setting.center = [112.07, 45.08];
        geo_setting.zoom = 1.00;
    }
    else if (area_name == '上海') {
        geo_setting.center = [121.5, 31.25];
        geo_setting.zoom = 1.12;
    }
    else if (area_name == '贵州') {
        geo_setting.center = [106.9, 26.9];
        geo_setting.zoom = 1.08;
    }
    else if (area_name === '香港') {
        // geo_setting.center = [106.9, 26.9];
        geo_setting.zoom = 0.9;
    }

    return geo_setting;
}

function echart_enable_citysymbol() {
    var newoption = myChart.getOption();
    newoption['series'][0] =
        {
            name: "city",
            type: 'scatter',
            coordinateSystem: 'geo',
            // data: JSON.parse(geoCoordMap),
            data: geoCoordMap,
            symbolSize: 8,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            itemStyle: {
                emphasis: {
                    borderColor: '#fff',
                    borderWidth: 1
                }
            }
        };
    newoption['geo'][0]['regions'] = geoCoordMapRegions;
    myChart.setOption(newoption, true);
}

function echart_disenable_citysymbol() {
    var newoption = myChart.getOption();
    newoption['legend'] = null;
    newoption['visualMap'] = null;
    newoption['series'][0] = null;
    myChart.setOption(newoption, true);
}

function echart_init() {
    $.ajax({
        type: "post",
        url: "/ajax_beento/ajax_get_cities_beento",
        dataType: "json",
        data: JSON.stringify({areaName: area_name}),
        success: function (data) {
            geoCoordMap = data['citiesData'];
            geoCoordMapRegions = data['regions'];
            var option = {
                tooltip: {
                    trigger: 'item',
                    formatter: '{b}<br/>{c} (p / km2)'
                },
                // tooltip: {
                //     formatter: '{b}', //提示标签格式
                //     backgroundColor: "#ff7f30",//提示标签背景颜色
                //     textStyle: {color: "#fff"} //提示标签字体颜色
                // },
                geo: geo_inti(),
                series: []
            };
            myChart.setOption(option);
            echart_enable_citysymbol();
        }
    });
}

function load_script(path, callback) {
    const head = document.head;
    const script = document.createElement('script');
    script.type = 'text/javascript';
    var done = false;
    script.onreadystatechange = function () {
        if (this.readyState == "loaded" || this.readyState == "complete") {
            success();
        }
    };
    script.onload = function () {
        if (!done) {
            done = true;
            script.onload = script.onreadystatechange = script.onerror = null;
            head.removeChild(script);
            callback(true);
        }
    }
    script.onerror = function () {
        if (!done) {
            done = true;
            script.onload = script.onreadystatechange = script.onerror = null;
            head.removeChild(script);
            callback(false);
        }
    }
    script.src = path;
    head.appendChild(script);
}

function select_province(country_name, province_name) {
    $.ajax({
        type: "post",
        url: "/ajax_beento/ajax_get_province_pinyin",
        dataType: "json",
        data: JSON.stringify({countryName: country_name, provinceName: province_name}),
        success: function (data) {
            window.location.href = "/beento/" + area_name + "/" + data['pinyin'].toLowerCase();
        }
    });
}

function update_cities_beento_status(province_name, city_name) {
    $.ajax({
        type: "post",
        url: "/ajax_beento/ajax_update_cities_beento_status",
        dataType: "json",
        data: JSON.stringify({provinceName: province_name, cityName: city_name}),
        success: function (data) {
            geoCoordMap = data['citiesBeenToData'];
            geoCoordMapRegions = data['regions'];
            echart_enable_citysymbol();
        }
    });
}

// function select_province_noredirect(country_name,province_name) {
//     $.ajax({
//         type: "post",
//         url: "/ajax_select_province",
//         dataType: "json",
//         data: JSON.stringify({countryName: country_name, provinceName: province_name}),
//         success: function (data) {
//
//             load_script(data['path'], function () {
//                 area_name = province_name;
//                 echart_init();
//             });
//         }
//     });
// }

// myChart.on("mousemove", function (param) {
//     console.log(myChart.convertFromPixel({geoIndex: 0}, [param.event.event.offsetX, param.event.event.offsetY]));
// });

myChart.on("click", function (param) {
    // console.log(param.event.target._rect);
    // console.log(param.event.event.view.geoCoordMap);
    //console.log(param.event);
    // console.log(myChart.convertFromPixel({geoIndex: 0}, [param.event.event.pageX, param.event.event.pageY]));
    //console.log(myChart.convertFromPixel({geoIndex: 0}, [param.event.event.offsetX, param.event.event.offsetY]));
    // console.log(param.event.target.invTransform);
    // console.log(param.event.target._rectWithStroke);

    //选择国家
    if (area_grade == 0) {
        //目前只处理中国，其它国家不处理
        if (param.name == 'China') {
            window.location.href = "/beento/" + param.name.toLowerCase();
        }
    }
    //选择省份
    else if (area_grade == 1) {
        if (area_name == 'china') {
            if (param.componentType == "series") {
                //
            }
            else {
                select_province(area_name, param.name);
            }
            // 不跳转页面，直接加载
            // area_grade = 2;
            // select_province_noredirect(area_name,param.name);
        }
    }
    //选择市县
    else if (area_grade == 2) {
        update_cities_beento_status(area_name, param.name);
    }
});

if (province_js_path != '') {
    load_script(
        province_js_path, function () {
            echart_init();
        });
}
else {
    echart_init();
}

$('#div_main_parent').resize(function () {
    myChart.resize();
});

// window.onresize = myChart.resize;

$(window).on('resize', function () {
    resizeMainContainer();
    myChart.resize();
});


//
// var option = {
//     tooltip: {
//         formatter: '{b}', //提示标签格式
//         backgroundColor: "#ff7f30",//提示标签背景颜色
//         textStyle: {color: "#fff"} //提示标签字体颜色
//     },
//     geo: [{
//         map: area_name,
//         label: {
//             normal: {
//                 show: true,//显示省份标签
//                 textStyle: {color: "#c71585"}//省份标签字体颜色
//             },
//             emphasis: {//对应的鼠标悬浮效果
//                 show: true,
//                 textStyle: {color: "#800080"}
//             }
//         },
//         itemStyle: {
//             normal: {
//                 borderWidth: .5,//区域边框宽度
//                 borderColor: '#009fe8',//区域边框颜色
//                 areaColor: "#ffefd5",//区域颜色
//             },
//             emphasis: {
//                 borderWidth: .5,
//                 borderColor: '#4b0082',
//                 areaColor: "#afdead",
//             }
//         },
//         aspectScale: 0.75,
//         roam: false,
//         layoutCenter: ['30%', '30%'],
//         label: {
//             normal: {
//                 show: true,//显示省份标签
//                 textStyle: {color: "#afdead"}//省份标签字体颜色
//             },
//             emphasis: {
//                 show: true
//             }
//         },
//         itemStyle: {
//             normal: {
//                 // areaColor: '#323c48',
//                 // areaColor: '#808080',
//                 areaColor: '#44566B',
//                 // borderColor: '#111'
//             }
//             ,
//             emphasis: {
//                 // areaColor: '#2a333d'
//                 // areaColor: '#228B22'
//                 areaColor: '#E5D5A1'
//             }
//         },
//         selectedMode: 'multiple',
//         regions: [
//             {
//                 name: '绥化市',
//                 selected: true
//             },
//             {
//                 name: '哈尔滨市',
//                 selected: true
//             },
//             {
//                 name: '广西',
//                 selected: true
//             },
//             {
//                 name: '云南',
//                 selected: true
//             },
//         ]
//     }],
//     series: [
//         {
//             type: 'map',
//             mapType: area_name,
//             selectedMode: 'single',//multiple多选
//             label: {
//                 normal: {
//                     show: true,//显示省份标签
//                     textStyle: {color: "#c71585"}//省份标签字体颜色
//                 },
//                 emphasis: {//对应的鼠标悬浮效果
//                     show: true,
//                     textStyle: {color: "#800080"}
//                 }
//             },
//             itemStyle: {
//                 normal: {
//                     borderWidth: .5,//区域边框宽度
//                     borderColor: '#009fe8',//区域边框颜色
//                     areaColor: "#ffefd5",//区域颜色
//                 },
//                 emphasis: {
//                     borderWidth: .5,
//                     borderColor: '#4b0082',
//                     areaColor: "#afdead",
//                 }
//             },
//             data: [
//                 {name: '福建', selected: true}//福建为选中状态
//             ]
//         },
//     ],
// }


// option = {
//     bmap: {
//         center: [104.114129, 37.550339],
//         zoom: 5,
//         roam: true,
//     },
// };

// tooltip = {                                      //提示框组件
//     trigger: 'item',                            //触发类型,'item'数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。 'axis'坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
//     triggerOn: "mousemove",                      //提示框触发的条件,'mousemove'鼠标移动时触发。'click'鼠标点击时触发。'mousemove|click'同时鼠标移动和点击时触发。'none'不在 'mousemove' 或 'click' 时触发
//     showContent: true,                           //是否显示提示框浮层
//     alwaysShowContent: true,                     //是否永远显示提示框内容
//     showDelay: 0,                                  //浮层显示的延迟，单位为 ms
//     hideDelay: 100,                                //浮层隐藏的延迟，单位为 ms
//     enterable: false,                             //鼠标是否可进入提示框浮层中
//     confine: false,                               //是否将 tooltip 框限制在图表的区域内
//     transitionDuration: 0.4,                      //提示框浮层的移动动画过渡时间，单位是 s,设置为 0 的时候会紧跟着鼠标移动
//     position: ['50%', '50%'],                    //提示框浮层的位置，默认不设置时位置会跟随鼠标的位置,[10, 10],回掉函数，inside鼠标所在图形的内部中心位置，top、left、bottom、right鼠标所在图形上侧，左侧，下侧，右侧，
//     formatter: "{b0}: {c0}<br />{b1}: {c1}",     //提示框浮层内容格式器，支持字符串模板和回调函数两种形式,模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等
//     backgroundColor: "transparent",            //标题背景色
//     borderColor: "#ccc",                        //边框颜色
//     borderWidth: 0,                              //边框线宽
//     padding: 5,                                  //图例内边距，单位px  5  [5, 10]  [5,10,5,10]
//     textStyle: mytextStyle,                     //文本样式
// };