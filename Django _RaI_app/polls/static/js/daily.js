google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic(fin_list) {
    var data = new google.visualization.DataTable();   
    data.addColumn({ type: 'string', id: 'Days' });
    data.addColumn('number', 'Footfall');   
    console.log('hi 2');
    var data1 ="{{fin_list}}";
    console.log({data1});
    data.addRows([ data1 ] );

      var options = {
        title: 'Weekly FootFall',
        hAxis:
            {
            title: 'Days of Week',
            format: 'DDD',
            viewWindow: 
                {
                min: ['Sunday'],
                max: ['Saturday']
                }
            },
        vAxis: 
            {
            title: 'Rating (scale of 1-10)'
            }
      };

    var chart = new google.visualization.ColumnChart(
    document.getElementById('chart_div'));

    chart.draw(data, options);
    }