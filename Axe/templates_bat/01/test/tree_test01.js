var categories = [];
    for (var i = 0; i < 5; i++) {
        categories[i] = {
            name: '类目' + i
        };
    }

var myChart = echarts.init(document.getElementById('main'));

var option= {
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove"
    },
    legend: [{
        // selectedMode: 'single',
        data: categories.map(function (a) {
            return a.name;
        })
    }],
    "series": [
        {
            "type": "tree",
            name: '类目1',
            "top": "18%",
            "bottom": "14%",
            "layout": "radial",
            direction: 'inverse',
            "symbol": "circle",
            label: {
                normal: {
                    position: 'left',
                    verticalAlign: 'middle',
                    //align: 'right',
                    fontSize: 9
                }
            },
            leaves: {
                label: {
                    normal: {
                        position: 'right',
                        verticalAlign: 'middle',
                        //align: 'left',
                        rotate: 0,
                        formatter: '{b}asdasd'
                    }
                }
            },
            categories: categories,
            "symbolSize": 5,
            "initialTreeDepth": 3,
            "animationDurationUpdate": 750,
            "data": [
                {
                    "name": "",
                    "category": 0,
                    "symbolSize": 40,
                    itemStyle: {
                        normal: {
                            color: 'red'
                        }
                    },
                    label: {
                        normal: {
                            color: 'green'
                        }
                    },
                    "children": [
                        {
                            "name": "股东",
                            "category": 1,
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "股东",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "股东1",
                                        },
                                        {
                                            "name": "股东2",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "并购",
                            "category": 1,
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "并购",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "子公司1",
                                        },
                                        {
                                            "name": "子公司2",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "category": 1,
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "category": 1,
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "category": 1,
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "支线",
                            "symbolSize": 20,
                            "children": [
                                {
                                    "name": "支线",
                                    "symbolSize": 10,
                                    "children": [
                                        {
                                            "name": "叶节点",
                                        },
                                        {
                                            "name": "叶节点",
                                        }
                                    ]
                                }
                            ]
                        },
                    ]
                }
            ],
        }
    ]
};

myChart.setOption(option = option);