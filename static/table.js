$(document).ready(function (){
    function showRelated(id){

        var width = 400, height = 400;

        var force = d3.layout.force()
                .charge(-200).linkDistance(30).size([width,height]);

        d3.select("svg").remove();

        var svg = d3.select("#graph").append("svg")
                .attr("width","50%").attr("height","50%")
                .attr("pointer-events","all");

        d3.json("/relatednode/" + encodeURIComponent(id),
            function (error, graph){
            if (error) return;

            force.nodes(graph.nodes).links(graph.links).start();

            var link = svg.selectAll(".link")
                    .data(graph.links).enter()
                    .append("line").attr("class","link");

            var node = svg.selectAll(".node")
                    .data(graph.nodes).enter()
                    .append("circle")
                    .attr("class", function (d) { return "node "+d.id})
                    .attr("r", 10)
                    .call(force.drag);

            var linkText = svg.selectAll(".link")
                            .append("text")
                            .attr("class", "link-label")
                            .attr("font-family", "Arial, Helvetica, sans-serif")
                            .attr("fill", "Black")
                            .style("font", "normal 12px Arial")
                            .attr("dy", ".35em")
                            .attr("text-anchor", "middle")
                            .text(function(d) {
                             return d.caption;
                             });

            node.append("title")
                        .text(function(d){return d.caption;})


            force.on("tick",function(){
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);

                linkText
                    .attr("x", function(d) {
                        return ((d.source.x + d.target.x)/2);
                    })
                    .attr("y", function(d) {
                        return ((d.source.y + d.target.y)/2);
                    });
            })
        })
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