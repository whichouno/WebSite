var rawData = document.getElementById("script_tree_data").getAttribute('rawData');
var data1 = JSON.parse(rawData);

var container = document.getElementById('div_bookshelf_main');
var myChart = echarts.init(container);

// myChart.showLoading();
// myChart.hideLoading();

var series_setting = new Array();
var allNode=0;

function series_init_mutiltrees() {
    echarts.util.each(data1, function (datum, index) {
        series_setting[index] = {
            type: 'tree',
            name: 'tree' + index,
            data: [datum],
            top: '5%',
            left: '7%',
            bottom: '2%',
            right: '30%',
            symbolSize: 7,
            label: {
                normal: {
                    position: 'left',
                    verticalAlign: 'middle',
                    align: 'right'
                },
                formatter: function (params) {
                    var count = Object.keys(datum).length;
                    return params.value + ":" + count;
                }
            },
            leaves: {
                label: {
                    normal: {
                        position: 'right',
                        verticalAlign: 'middle',
                        align: 'left'
                    }
                }
            },
            expandAndCollapse: true,
            animationDuration: 550,
            animationDurationUpdate: 750
        }
    });
}

function series_init_singletree() {
    series_setting[0] = {
        type: 'tree',
        name: 'tree1',
        data: [data1],
        top: '5%',
        left: '7%',
        bottom: '2%',
        right: '20%',
        symbolSize: 7,
        initialTreeDepth: -1,
        lineStyle: {
            // color: '#282828',
            curveness: 0.6,// 树图边曲度
            type: 'solid', // 'curve'|'broken'|'solid'|'dotted'|'dashed'
            // shadowColor: 'rgba(0, 0, 0, 0.5)',
            // shadowBlur: 10,
            // shadowOffsetY: 10
        },
        label: {
            color:'#000000',
            fontSize: 14,
            fontWeight: 500,
            position: 'left',
            verticalAlign: 'middle',
            align: 'right',
            formatter: function (params) {
                //非叶子节点，显示名称及子节点数量
                if (params.data.children !== undefined) {
                    return params.data.name + "(" + params.data.children.length + ")";
                }//叶子节点，只显示名称
                else {
                    return params.name;
                }
            },
        },
        expandAndCollapse: true,
        animationDuration: 550,
        animationDurationUpdate: 750
    }
}

function get_NodesCount() {
    var nodes = myChart._chartsViews[0]._data._graphicEls;
    for (var i = 0, count = nodes.length; i < count; i++) {
        var node = nodes[i];
        if (node === undefined)
            continue;
        allNode++;
    }
}

function windows_Resize() {
    var height = window.innerHeight;
    var currentHeight = 20 * allNode;
    var newWidth = Math.max(currentHeight, height);
    // container.style.width = window.innerWidth + 'px';
    container.style.height = newWidth + 'px';
    myChart.resize();
}

function update_book_status(param,book_id) {
    $.ajax({
        type: "post",
        url: "/ajax_bookshelf/ajax_update_book_status",
        dataType: "json",
        data: JSON.stringify({bookID: book_id}),
        success: function (data) {
            param.data.itemStyle.color = data['color'];
            param.data.status = data['description'];

            myChart.resize();
            get_read_count();
        }
    });
}

function get_read_count() {
    $.ajax({
        type: "post",
        url: "/ajax_bookshelf/ajax_get_read_count",
        dataType: "json",
        data: [],
        success: function (data) {
            document.getElementById("input_unread").setAttribute('value',data['unread_count']);
            document.getElementById("input_reading").setAttribute('value',data['reading_count']);
            document.getElementById("input_read").setAttribute('value',data['read_count']);
        }
    });
}

// series_init_mutiltrees();
series_init_singletree();

myChart.on("mousemove", function(param) {});

myChart.on("click", function(param) {
    // console.log(param);
    //非叶子节点，显示名称及子节点数量
    if (param.data.children !== undefined) {
        console.log("hahahahaha");
        allNode=0;
        get_NodesCount();
        windows_Resize();
    }//叶子节点，只显示名称
    else {
        var bookid = param.data.id;
        update_book_status(param,bookid);
    }
});

myChart.setOption(option = {
    tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove'
    },
    series: series_setting
},true);

get_NodesCount();
windows_Resize();

$('#div_main_parent').resize(function () {
    myChart.resize();
});

window.onresize = myChart.resize;