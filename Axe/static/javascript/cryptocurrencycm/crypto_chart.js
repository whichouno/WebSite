var upColor = '#ec0000';
var upBorderColor = '#8A0000';
var downColor = '#00da3c';
var downBorderColor = '#008F28';

var rawData = document.getElementById("script_chart_data").getAttribute('rawData');

function splitData(rawData) {
    var categoryData = [];
    var values = [];
    var volumes = [];
    for (var i = 0; i < rawData.length; i++) {
        categoryData.push(rawData[i].splice(0, 1)[0]);
        values.push(rawData[i]);
        //volumes.push([i, rawData[i][4], rawData[i][0] > rawData[i][1] ? 1 : -1]);
        volumes.push(rawData[i][4]);
    }

    return {
        categoryData: categoryData,
        values: values,
        volumes: volumes
    };
}

function calculateMA(dayCount, data) {
    var result = [];
    for (var i = 0, len = data.values.length; i < len; i++) {
        if (i < dayCount) {
            result.push('-');
            continue;
        }
        var sum = 0;
        for (var j = 0; j < dayCount; j++) {
            sum += data.values[i - j][1];
        }
        result.push(+(sum / dayCount).toFixed(3));
    }
    return result;
}

var myChart = echarts.init(document.getElementById('div_cryptocurrency_main'),'vintage');

var data = splitData(JSON.parse(rawData));

function myChart_dateZoom_SetDate(startDate,endDate){

    myChart.setOption(option= {
        dataZoom: [
            {
                type: 'inside',
                xAxisIndex: [0, 1],
                startValue: startDate,
                endValue: endDate
            },
            {
                show: true,
                xAxisIndex: [0, 1],
                type: 'slider',
                top: '85%',
                startValue: startDate,
                endValue: endDate
            }

        ]
    });
}

function myChart_dateZoom_SetRange(start,end){
    myChart.setOption(option= {
        dataZoom: [
            {
                type: 'inside',
                xAxisIndex: [0, 1],
                start: start,
                end: end
            },
            {
                show: true,
                xAxisIndex: [0, 1],
                type: 'slider',
                top: '85%',
                start: start,
                end: end
            }

        ]
    });
    // return false;
}

myChart.on('datazoom', function (param) {
    var axis = myChart.getModel().option.xAxis[0];
    var starttime = axis.data[axis.rangeStart];
    var endtime = axis.data[axis.rangeEnd];
    set_datepickers_value("inp_start_date",starttime,"inp_end_date",endtime);
    // console.log(param);
});

myChart.setOption(option = {
    backgroundColor: '#fff',
    animation: false,
    legend: {
        left: 'center',
        data: [ 'MA5', 'MA10', 'MA20', 'MA30' ]
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross'
        },
        backgroundColor: 'rgba(245, 245, 245, 0.8)',
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
        textStyle: {
            color: '#000'
        },
        position: function (pos, params, el, elRect, size) {
            var obj = {top: 10};
            obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30;
            return obj;
        }
        // extraCssText: 'width: 170px'
    },
    axisPointer: {
        link: {xAxisIndex: 'all'},
        label: {
            backgroundColor: '#777'
        }
    },
    toolbox: {
        feature: {
            dataZoom: {
                yAxisIndex: false
            },
            brush: {
                type: ['lineX', 'clear']
            }
        }
    },
    brush: {
        xAxisIndex: 'all',
        brushLink: 'all',
        outOfBrush: {
            colorAlpha: 0.1
        }
    },
    visualMap: {
        show: false,
        seriesIndex: 5,
        dimension: 2,
        pieces: [{
            value: 1,
            color: downColor
        }, {
            value: -1,
            color: upColor
        }]
    },
    grid: [
        {
            left: '10%',
            right: '8%',
            height: '50%'
        },
        {
            left: '10%',
            right: '8%',
            top: '63%',
            height: '16%'
        }
    ],
    xAxis: [
        {
            id: 'coindateLine',
            type: 'category',
            data: data.categoryData,
            scale: true,
            boundaryGap: true,
            axisLine: {onZero: false},
            splitLine: {show: true},
            splitNumber: 20,
            min: 'dataMin',
            max: 'dataMax',
            axisPointer: {
                label: {
                    formatter: function (params) {
                        if (params.seriesData[0].data === undefined) {

                        }
                        else {
                            var closeValue = (params.seriesData[0].data[2] || {});
                            return params.value
                                + (closeValue !== null
                                        ? '\n' + 'Close : ' + echarts.format.addCommas(closeValue)
                                        : ''
                                );
                        }
                    }
                }
            }
        },
        {
            type: 'category',
            gridIndex: 1,
            data: data.categoryData,
            scale: true,
            boundaryGap: true,
            axisLine: {onZero: false},
            axisTick: {show: true},
            splitLine: {show: true},
            axisLabel: {show: true},
            splitNumber: 20,
            min: 'dataMin',
            max: 'dataMax',
            axisPointer: {
                label: {
                    formatter: function (params) {
                        var volumeValue = (params.seriesData[0] || {}).value;
                        return params.value
                            + (volumeValue !== null
                                    ? '\n' + 'Vol : ' + echarts.format.addCommas(volumeValue)
                                    : ''
                            );
                    }
                }
            }
        }
    ],
    yAxis: [
        {
            scale: true,
            name: 'Value(USD)',
            splitNumber: 10,
            splitArea: {
                show: true
            }
        },
        {
            scale: true,
            name: 'Volume(USD)',
            gridIndex: 1,
            splitNumber: 5,
            axisLabel: {show: true},
            axisLine: {show: true},
            axisTick: {show: true},
            splitLine: {show: true}
        }
    ],
    dataZoom: [
        {
            type: 'inside',
            xAxisIndex: [0, 1],
            start: 80,
            end: 100
        },
        {
            show: true,
            xAxisIndex: [0, 1],
            type: 'slider',
            top: '85%',
            start: 80,
            end: 100
        }
    ],
    series: [
        {
            name: '日线',
            type: 'candlestick',
            data: data.values,
            itemStyle: {
                normal: {
                    color: upColor,
                    color0: downColor,
                    borderColor: upBorderColor,
                    borderColor0: downBorderColor
                }
            },
            markPoint: {
                data: [
                    {
                        name: 'highest value',
                        type: 'max',
                        valueDim: 'highest'
                    },
                    {
                        name: 'lowest value',
                        type: 'min',
                        valueDim: 'lowest'
                    }
                ]

            },
            markLine : {
                data : [
                    {
                        name: 'highest value',
                        type : 'max',
                        valueDim: 'highest'
                    },
                    {
                        name: 'lowest value',
                        type : 'min',
                        valueDim: 'lowest'
                    }
                ]
            },
            tooltip: {
                formatter: function (param) {
                    param = param[0];
                    return [
                        'Date: ' + param.name + '<hr size=1 style="margin: 3px 0">',
                        'Open: ' + param.data[0] + '<br/>',
                        'Close: ' + param.data[1] + '<br/>',
                        'Lowest: ' + param.data[2] + '<br/>',
                        'Highest: ' + param.data[3] + '<br/>'
                    ].join('');
                }
            }
        },
        {
            name: 'MA5',
            type: 'line',
            data: calculateMA(5, data),
            smooth: true,
            lineStyle: {
                normal: {opacity: 0.5}
            }
        },
        {
            name: 'MA10',
            type: 'line',
            data: calculateMA(10, data),
            smooth: true,
            lineStyle: {
                normal: {opacity: 0.5}
            }
        },
        {
            name: 'MA20',
            type: 'line',
            data: calculateMA(20, data),
            smooth: true,
            lineStyle: {
                normal: {opacity: 0.5}
            }
        },
        {
            name: 'MA30',
            type: 'line',
            data: calculateMA(30, data),
            smooth: true,
            lineStyle: {
                normal: {opacity: 0.5}
            }
        },
        {
            name: 'Volume',
            type: 'bar',
            markLine : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            xAxisIndex: 1,
            yAxisIndex: 1,
            data: data.volumes
        }
    ]
}, true);

$('#div_main_parent').resize(function () {
    myChart.resize();
});

window.onresize = myChart.resize;
