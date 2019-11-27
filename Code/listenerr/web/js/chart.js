var ctx = document.getElementById('myChart').getContext('2d');
Chart.defaults.global.defaultFontColor = 'white';
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['0', '0:20', '0:40', '1:00', '1:20', '1:40'],
        datasets: [{
            label: 'Data Result',
            data: [0, 1, 0, 0, 1, 0],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },

        legend: {
            labels: {
                fontColor: 'rgba(255, 255, 255, 1)'
            }
        }
    }
});
