$(document).ready(function (){
    function showRelated(id){
    $.get("/relatednode/" + encodeURIComponent(id),
        function (data){
            if(!data) return;
            t = $("#graph").empty();
            data.forEach(function(col){
            t.append("<tr><td>"+JSON.stringify(col)+"</td></tr>");
            });
        }
    ,"json");
    return false;
    }

    function getck(index){
        $.get()
    }

    function search(){
    var query = $("#search").find("input[name=searchnode]").val();
    $.get("/searchnode?q=" + encodeURIComponent(query),
        function (data){
            var t = $("table#result tbody").empty();
            if (!data || data.length == 0) return ;
            data.forEach(function (col){
                var str = JSON.stringify(col).replace(/[\[\]']+/g,'').replace(/[\{\}']+/g,'').split('\",\"');
                var display = "<tr>"
                for (var a in str){
                    display += ("<td>"+str[a]+"</td>");
                //$("<tr><td>"+JSON.stringify(col,null,4).replace(/[\[\]']+/g,'').replace(/[\{\}']+/g,'')+"</td></tr>").appendTo(t)
                //.click(function() )
                }
                t.append(display+"</tr>")
            });
            showRelated(1);
        },"json");
        return false;
    }
    $("#search").submit(search);
    search();
});