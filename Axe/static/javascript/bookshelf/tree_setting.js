function select_init(select_id_01,select_id_02) {
    var selects = $("#" + select_id_01 + ",#" + select_id_02);
    $.ajax({
        type: "post",
        url: "/ajax_bookshelf/ajax_continent",
        dataType: "json",
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                var pOption = "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
                // $("#continent").append(pOption);
                selects.eq(0).append(pOption);
            }
        }
    });
　　　　　　　
    $.ajax({
        type: "post",
        url: "/ajax_bookshelf/ajax_state",
        dataType: "json",
        data: JSON.stringify({continent_id:1}),
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                var pOption = "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
                // $("#state").append(pOption);
                selects.eq(1).append(pOption);
            }
        }
    });
}

function select_change(main_select_id,relate_select_id){
    $("#" + relate_select_id).attr("disabled",false);
    // $("#state").children(":not(:first)").remove();
    $("#" + relate_select_id).children().remove();
    var val=$("#" + main_select_id + " option:selected").val();

    $.ajax({
        type: "post",
        url: "/ajax_bookshelf/ajax_state",
        dataType: "json",
        data: JSON.stringify({continent_id:val}),
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                var pOption = "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
                $("#state").append(pOption);
            }
        }
    });
}

// $("#continent").change(function(){
//     $("#state").attr("disabled",false);
//     // $("#state").children(":not(:first)").remove();
//     $("#state").children().remove();
//     var val=$("#continent option:selected").val();
//
//     $.ajax({
//         type: "post",
//         url: "/ajax_state",
//         dataType: "json",
//         data: JSON.stringify({continent_id:val}),
//         success: function (data) {
//             for (var i = 0; i < data.length; i++) {
//                 var pOption = "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
//                 $("#state").append(pOption);
//             }
//         }
//     });
// });