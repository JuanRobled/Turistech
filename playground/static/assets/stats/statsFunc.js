function generarDatos(){
    ganancias();
    costos();
    ocupacion();
    solicitudes();
}


function ganancias(){
    var canva = document.getElementById("graficaGanacias").getContext("2d");
    chartG = new Chart(canva,{
        type:"pie",
        data:{
            labels:["S1", "S2", "S3"],
            textOffset:0,
            datasets:[{
                label:"Reservas mensuales servicios",
                data:[10,8,12],
                backgroundColor:[
                    'rgb(255, 0, 0)',
                    'rgb(0, 255, 0)',
                    'rgb(0, 0, 255)'
                ]
            }]
        },
        options:{
            responsive: true,
            plugins: {
            legend: {
                position: 'right',
            }}
        }
    });
}

function costos(){
    var canva = document.getElementById("graficaCostos").getContext("2d");
    chartC = new Chart(canva,{
        type:"pie",
        data:{
            labels:["S1", "S2", "S3"],
            textOffset:0,
            datasets:[{
                label:"Reservas mensuales servicios",
                data:[5,3,7],
                backgroundColor:[
                    'rgb(255, 0, 0)',
                    'rgb(0, 255, 0)',
                    'rgb(0, 0, 255)'
                ]
            }]
        },
        options:{
            responsive: true,
            plugins: {
            legend: {
                position: 'right',
            }}
        }
    });
}

function ocupacion(){
    var canva = document.getElementById("graficaOcupacion").getContext("2d");
    chartO = new Chart(canva,{
        type:"line",
        data:{
            labels:[
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            ],
            textOffset:0,
            datasets:[{
                label:"H1",
                borderColor:'rgb(255, 0, 0)',
                backgroundColor:'rgb(255, 0, 0)',
                data:[8, 5, 14, 9, 3, 11, 2, 6, 10, 12, 7, 1],
                backgroundColor:'rgb(255, 0, 0)'
            },{
                label:"H2",
                data:[13, 3, 6, 15, 11, 2, 8, 5, 14, 9, 1, 7],
                borderColor:'rgb(0, 255, 0)',
                backgroundColor:'rgb(0, 255, 0)',
                backgroundColor:'rgb(0, 255, 0)'
            }]
        },
        options:{
            responsive: true,
            plugins: {
            legend: {
                position: 'bottom',
            }}
        }
    });
}

function solicitudes(){
    var canva = document.getElementById("graficaSolicitudes").getContext("2d");
    chartO = new Chart(canva,{
        type:"line",
        data:{
            labels:[
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            ],
            textOffset:0,
            datasets:[{
                label:"S1",
                borderColor:'rgb(255, 0, 0)',
                backgroundColor:'rgb(255, 0, 0)',
                data:[5,3,7,3,7,8,9,10,2,11,13,1],
                backgroundColor:'rgb(255, 0, 0)'
            },{
                label:"S2",
                data:[7, 12, 3, 14, 9, 5, 2, 10, 8, 11, 6, 13],
                borderColor:'rgb(0, 255, 0)',
                backgroundColor:'rgb(0, 255, 0)',
                backgroundColor:'rgb(0, 255, 0)'
            }]
        },
        options:{
            responsive: true,
            plugins: {
            legend: {
                position: 'bottom',
            }}
        }
    });
}