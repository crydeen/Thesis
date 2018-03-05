var margin = {top: 2, right: 140, bottom: 30, left: 40},
    width = 1160 - margin.left - margin.right,
    height = 680 - margin.top - margin.bottom;

    //parseInt(String(d.year).slice(0,4))

var xValue = function(d) { return parseInt(String(d.year).slice(0,4)) }, // data -> value
    xLabel = function(d) { return d.year },
    xScale = d3.scale.linear().range([0, width]), // value -> display
    xMap = function(d) { return xScale(xValue(d));}, // data -> display
    xAxis = d3.svg.axis().scale(xScale).orient("bottom").tickFormat(d3.format("d0"));

// setup y
var yValue = function(d) { return d.score;}, // data -> value
    yScale = d3.scale.linear().range([height, 0]), // value -> display
    yMap = function(d) { return yScale(yValue(d));}, // data -> display
    yAxis = d3.svg.axis().scale(yScale).orient("left");

// setup fill color
var cValue = function(d) { return d.president;},
    color = d3.scale.category10();

// add the graph canvas to the body of the webpage
var svg = d3.select("body div#visual").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("class", "white-background")
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// add the tooltip area to the webpage
var tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

// load data
d3.csv("CSV/coordinates.csv", function(error, data) {
  var current_pres = data[0].president;
  console.log(data[0])
  console.log(current_pres)
  var president_counter = 1
  // change string (from CSV) into number format
  data.forEach(function(d) {
    d.year = +d.year;
    d.score = +d.score;
    if (d.president != current_pres) {
      president_counter = president_counter + 1;
      current_pres = d.president;
      if (current_pres === "Tyler" || current_pres === "Arthur") {
        president_counter = president_counter + 1;
      }
    }
    if (president_counter < 10){
      counter_string = "0" + String(president_counter);
    }
    else {
      counter_string = String(president_counter);
    }
    d.president = counter_string + " - " + current_pres;
//    console.log(d);
  });

  // don't want dots overlapping axis, so add in buffer to data domain
  xScale.domain([d3.min(data, xValue)-1, d3.max(data, xValue)+1]);
  yScale.domain([d3.min(data, yValue)-1, 1.05]);

  // x-axis
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("Year");

  // y-axis
  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Sentiment Score");

  // draw dots
  svg.selectAll(".dot")
      .data(data)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 4)
      .attr("cx", xMap)
      .attr("cy", yMap)
      .style("fill", function(d) { return color(cValue(d));})
      .on("mouseover", function(d) {
          tooltip.transition()
               .duration(200)
               .style("opacity", .9);
          tooltip.html(d.president + "<br/> (" + xLabel(d)
     	        + ", " + yValue(d) + ")" + "<br/>" + d.party)
               .style("left", (d3.event.pageX + 5) + "px")
               .style("top", (d3.event.pageY - 28) + "px");
      })
      .on("mouseout", function(d) {
          tooltip.transition()
               .duration(500)
               .style("opacity", 0);
      });

      // var svg2 = d3.select("body div.legend").append("svg")
      // .attr("width", 130)
      // .attr("height", 800 - margin.top - margin.bottom)
      // .attr("class","white-background")
      // draw legend
      var legend = svg.selectAll(".legend")
          .data(color.domain())
        .enter().append("g")
          .attr("class", "legend")
          .attr("transform", function(d, i) { return "translate(0," + i * 16 + ")"; });

      // draw legend colored rectangles
      legend.append("rect")
          .attr("y",2)
          .attr("x", width + 3)
          .attr("width", 18)
          .attr("height", 18)
          .style("fill", color);

      // draw legend text
      legend.append("text")
          .attr("x", width + 23)
          .attr("y", 10)
          .attr("dy", ".35em")
          .style("text-anchor", "start")
          .text(function(d) { return d;})

      legend.on("mouseover", function(type) {
          d3.selectAll(".legend")
            .style("opacity", 0.1);
          d3.select(this)
            .style("opacity", 1);
          d3.selectAll(".dot")
            .style("opacity", 0.1)
            .filter(function(d) { return d.president == type; })
            .style("opacity", 1);
        })
        .on("mouseout", function(type) {
          d3.selectAll(".legend")
            .style("opacity", 1);
          d3.selectAll(".dot")
            .style("opacity", 1);
        });
      // legend.on("click", function(type) {
      //   d3.selectAll(".legend")
      //     .style("opacity", 0.1);
      //   d3.select(this)
      //     .style("opacity",1);
      //   d3.selectAll(".dot")
      //     .style("opacity", 0.1)
      //     .filter(function(d) { return d.president == type; })
      //     .style("opacity", 1);
      // })
});
