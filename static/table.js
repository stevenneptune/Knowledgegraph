$(document).ready(function (){
    function search(){
    var query = $("#search").find("input[name=searchnode]").val();
    $.get("/searchnode?q=" + encodeURIComponent(query),
        function (data){
            var t = $("table#result tbody").empty();
            if (!data || data.length == 0) return ;
            data.forEach(function (col){
                t.append("<tr><td>"+col+"<\tr><\td>")
            });
        },"json");
    }

    $("#search").submit(search);
});