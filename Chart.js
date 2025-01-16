const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [], // Etiquetas dinámicas
        datasets: [{
            label: 'Eventos detectados',
            data: [], // Datos dinámicos
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

function updateChart(data) {
    myChart.data.labels = data.labels;
    myChart.data.datasets[0].data = data.values;
    myChart.update();
}
