

let btn_inicio = document.getElementById('btn-inicio');
let btn_buscar = document.getElementById('btn-buscar');
let btn_equipos = document.getElementById('btn-equipos');
let btn_lideres = document.getElementById('btn-lideres');
let inicio = document.getElementById('inicio');
let buscar = document.getElementById('buscar');
let equipos = document.getElementById('equipos');
let lideres = document.getElementById('lideres');
let buscar_input = document.getElementById('search-input');
let n_jugador = document.getElementById('player_name');

btn_inicio.addEventListener('click', ()=> cambiar_pagina('inicio'))
btn_buscar.addEventListener('click', ()=> cambiar_pagina('buscar'))
btn_equipos.addEventListener('click', ()=> cambiar_pagina('equipos'))
btn_lideres.addEventListener('click', ()=> cambiar_pagina('lideres'))

function cambiar_pagina(pag) {
    switch (pag) {
        case 'inicio':
            inicio.style.left = '0'
            buscar.style.left = '100%'
            equipos.style.left = '200%'
            lideres.style.left = '300%'
            break;
    
        case 'buscar':
            inicio.style.left = '-100%'
            buscar.style.left = '0'
            equipos.style.left = '100%'
            lideres.style.left = '200%'
            break;
        case 'equipos':
            inicio.style.left = '-200%'
            buscar.style.left = '-100%'
            equipos.style.left = '0'
            lideres.style.left = '100%'
            break;
        case 'lideres':
            inicio.style.left = '-300%'
            buscar.style.left = '-200%'
            equipos.style.left = '-100%'
            lideres.style.left = '0'
                break;
    }
}

function buscar_jugador() {
    for (i in jugadores){
        if (buscar_input.upper() in i.nombre.upper()){
            n_jugador.innerText = buscar_input.value
        }
    }
        
}