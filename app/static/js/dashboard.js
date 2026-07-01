fetch("/analytics/orders-chart")
.then(response=> response.json())
.then(result =>{
    
    const labels = result.data.labels;
    const values = result.data.values;

    new Chart(document.getElementById("salesChart"),{
        type:"line",
        data :{
            labels:labels,
            datasets: [{
                label:"Orders",
                data: values,
                borderColor:"#0d6efd",
                backgroundColor:"rgba(13,110,253,0.2)",
                borderWidth:3,
                fill:true,
                tension:0.4
            }]
        },

        options:{
            responsive:true,
            Plugins:{
                legend:{
                    display:true
                }
            },

            scales:{
                y:{
                    beginAtZero:true,
                    ticks:{
                        precision:0
                    }
                }
            }
        }
    });
});