function datepickers_init(start_element_id,end_element_id) {
    var datepickers = $("#" + start_element_id + ",#" + end_element_id);
    var minDate = data.categoryData[0];
    var maxDate = data.categoryData[data.categoryData.length - 1];
    datepickers.datepicker(
        {
            dateFormat: "yy-mm-dd",
            showOtherMonths: true,
            selectOtherMonths: true,
            changeYear: true,
            changeMonth: true,
            monthNamesShort: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
            minDate: minDate,
            maxDate: maxDate,
            hideIfNoPrevNext: true,
            onSelect: function (selectedDate) {
                var dateLimit = this.id == "inp_start_date" ? "minDate" : "maxDate";
                datepickers.not(this).datepicker("option", dateLimit, selectedDate);

                if(this.id == "inp_start_date"){
                    myChart_dateZoom_SetDate(selectedDate,$.datepicker.formatDate('yy-mm-dd', datepickers.not(this).datepicker('getDate')));
                }
                else{
                    myChart_dateZoom_SetDate($.datepicker.formatDate('yy-mm-dd',datepickers.not(this).datepicker("getDate")),selectedDate)
                }
            }
        }
    );

    var axis = myChart.getModel().option.xAxis[0];
    datepickers.eq(0).datepicker("setDate", axis.data[axis.rangeStart]);
    //datepickers.eq(0).datepicker("setDate", minDate);
    datepickers.eq(1).datepicker("setDate", maxDate);
}

function set_datepickers_value(start_element_id,startdate,end_element_id,enddate) {
    var datepickers = $("#" + start_element_id + ",#" + end_element_id);
    datepickers.eq(0).datepicker("setDate", startdate);
    datepickers.eq(1).datepicker("setDate", enddate);
}
