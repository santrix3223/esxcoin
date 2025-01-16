$(document).ready(function () {
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

    const table = $('#eventsTable').DataTable();

    function fetchEvents() {
        $.getJSON('/events', function (data) {
            // Actualizar tabla
            table.clear();
            data.forEach(event => {
                table.row.add([
                    event.device,
                    event.event,
                    event.timestamp
                ]).draw();
            });

            // Procesar datos para el gráfico
            const labels = data.map(event => event.timestamp);
            const values = data.map(() => 1); // Contar cada evento

            // Actualizar gráfico
            myChart.data.labels = labels;
            myChart.data.datasets[0].data = values;
            myChart.update();
        });
    }

    // Actualizar los datos cada 5 segundos
    setInterval(fetchEvents, 5000);
    fetchEvents(); // Llama una vez al cargar
});

