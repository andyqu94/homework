const url = "data/samples.json";

function demographic(id) {
    d3.json(url).then(function(data) {
        var sample_metadata = d3.select("#sample-metadata");
        sample_metadata.html("");
        var metadata=data.metadata;
        var samples = metadata.filter(item => item.id.toString() === id)[0];
        Object.entries(samples).forEach(function (key) {
            sample_metadata.append("h5").text(key[0]+":"+key[1]+"\n")
        });
    })
    };

function buildplot(id) {
d3.json(url).then(function(data) {
    var sample = data.samples
    var samples = sample.filter(item => item.id.toString() === id)[0];
    var sample_values = samples.sample_values.slice(0,10).reverse();
    var otu_ids_sliced = samples.otu_ids.slice(0,10);
    var otu_id = otu_ids_sliced.map(d => "OTU"+d)
    var labels = samples.otu_labels.slice(0,10)
    var bar = [{
        x: sample_values,
        y: otu_id,
        text: labels,
        orientation: 'h',
        type: "bar",
      }];
      
    var layout ={title:"top 10 otu"};

    Plotly.newPlot("bar", bar, layout)

d3.json(url).then(function(id) {
    var x_values = samples.otu_ids;
    var y_values = samples.sample_values;
    var m_size = samples.sample_values;
    var m_colors = samples.otu_ids; 
    var t_values = samples.otu_labels;
    
        var bubble = [{
          x: x_values,
          y: y_values,
          text: t_values,
          mode: 'markers',
          marker: {
            color: m_colors,
            size: m_size
          } 
        }];
      
        var layout = {
          xaxis: { title: "OTU ID"},
        };
    
        Plotly.newPlot('bubble', bubble , layout);
       
});
});
};


function init() {

    var selector = d3.select("#selDataset");
  
    d3.json(url).then((data) => {
      data.names.forEach((item) => {
        selector
          .append("option")
          .text(item)
          .property("value", item);
      });
  
      const firstSample = data.names[0];
      buildplot(firstSample);
      demographic(firstSample);
    });
  }
  
  function optionChanged(newSample) {
    buildplot(newSample);
    demographic(newSample);
  }

  init();
