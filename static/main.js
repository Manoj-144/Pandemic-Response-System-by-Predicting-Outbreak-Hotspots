// Animate Counter Values Using CountUp
document.addEventListener('DOMContentLoaded', () => {
    if (typeof stats !== 'undefined') {
      const counters = [
        { id: 'cases', value: stats.cases },
        { id: 'deaths', value: stats.deaths },
        { id: 'recoveries', value: stats.recoveries },
        { id: 'taluks', value: stats.taluks }
      ];
  
      counters.forEach(counter => {
        const countUp = new countUp.CountUp(counter.id, counter.value);
        if (!countUp.error) {
          countUp.start();
        } else {
          console.error(countUp.error);
          document.getElementById(counter.id).textContent = counter.value;
        }
      });
    } else {
      console.warn("Stats not loaded");
    }
  
    // Plotly Line Chart for Daily Trends
    if (typeof dailyTrend !== 'undefined') {
      const trace = {
        x: dailyTrend.dates,
        y: dailyTrend.cases,
        mode: 'lines+markers',
        name: 'Daily Cases',
        line: { color: 'indigo', width: 3 },
        marker: { size: 6 }
      };
  
      const layout = {
        margin: { t: 40, l: 40, r: 30, b: 50 },
        xaxis: {
          title: 'Date',
          type: 'date',
          tickangle: -45
        },
        yaxis: {
          title: 'Number of Cases'
        },
        responsive: true
      };
  
      Plotly.newPlot('line-chart', [trace], layout, { responsive: true });
    } else {
      console.warn("Daily trend data not loaded");
    }
  });
  