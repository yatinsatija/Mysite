google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
      var data = new google.visualization.DataTable();
      
      data.addColumn({ type: 'string', id: 'Days' });
      data.addColumn('number', 'Footfall');   

      data.addRows([ 
        ["Sunday", 600],
        ["Monday", 650],
        ["Tuesday", 345],
        ["Wednesday", 235],
        ["Thursday", 875],
        ["Friday", 456],
        ["Saturday", 986],
  ]);

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