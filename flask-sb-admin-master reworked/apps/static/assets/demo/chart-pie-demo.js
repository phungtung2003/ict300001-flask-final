// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: [ "Negative", "Neutral", "Positive"],
    datasets: [{
      data: [2.815299853682518, 8.191619344117818, 53.066885471343994],
      backgroundColor: ['#dc3545', '#ffc107', '#28a745'],
    }],
  },
});
