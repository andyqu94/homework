// from data.js
var tableData = data;
// YOUR CODE HERE!
var button = d3.select("#filter-btn")
// Use D3 to select the table body
var tbody = d3.select("tbody");

function appendtable(tableData) {

tableData.forEach((item) => {
    var row = tbody.append("tr");

    Object.entries(item).forEach(([key, value]) => {

        var cell = row.append("td");
        
        cell.text(value);
    });
});

}

appendtable(tableData)

button.on("click", function() {

    tbody.html("");

    var inputElement = d3.select("#datetime");
     
    var inputvalue = inputElement.property("value");

    console.log(inputvalue)

    if (inputvalue == '') {
        alert("Please enter a filter value");
        appendtable(tableData);}
       
    else {
        var filteredData = tableData.filter(item => item['datetime'] === inputvalue);

        filteredData.forEach((item) => {

        var row = tbody.append("tr");
        
        Object.entries(item).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
         });
     }
 })


