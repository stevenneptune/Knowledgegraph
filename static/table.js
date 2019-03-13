$(document).ready(function (){
    function showRelated(id){
    $.get("/relatednode/" + encodeURIComponent(id),
        function (data){
            if(!data) return;
            t = $("table#details tbody").empty();
            data.forEach(function(col){
            t.append("<tr><td>"+JSON.stringify(col)+"</td></tr>");
            });
        }
    ,"json");
    return false;
    }


    function search(){
    var query = $("#search").find("input[name=searchnode]").val();
    $.get("/searchnode?q=" + encodeURIComponent(query),
        function (data){
            var t = $("table#result tbody").empty();
            if (!data || data.length == 0) return ;
            var i = 0;
            data.forEach(function (col){
                var str = JSON.stringify(col).replace(/[\[\]']+/g,'').replace(/[\{\}']+/g,'').split(',\"');
                var display = "<tr>"
                for (var a in str){
                    display += ("<td>"+str[a].replace('\"','')+"</td>");
                //$("<tr><td>"+JSON.stringify(col,null,4).replace(/[\[\]']+/g,'').replace(/[\{\}']+/g,'')+"</td></tr>").appendTo(t)
                //.click(function() )
                }
                $(display+"</tr>").appendTo(t).click(function( ){showRelated(col.ck)});
                i++;
            });
            showRelated(data[0].ck);
        },"json");
        return false;
    }
    $("#search").submit(search);
    search();
});