// Seleccionar elementos del DOM
const formularioTarea = document.getElementById('task-form');
const entradaTarea = document.getElementById('task-input');
const listaTareas = document.getElementById('task-list');

// Cargar tareas desde localStorage
document.addEventListener('DOMContentLoaded', cargarTareas);

// Evento para agregar tarea
formularioTarea.addEventListener('submit', agregarTarea);

// Función para cargar tareas desde localStorage
function cargarTareas() {
    const tareas = JSON.parse(localStorage.getItem('tasks')) || [];
    tareas.forEach(tarea => renderizarTarea(tarea));
}

// Función para agregar una tarea
function agregarTarea(e) {
    e.preventDefault();
    const textoTarea = entradaTarea.value.trim();
    if (textoTarea === '') {
        alert('Por favor, ingresa una tarea.');
        return;
    }

    const tarea = { text: textoTarea, completed: false };
    guardarTareaEnLocalStorage(tarea);
    renderizarTarea(tarea);
    entradaTarea.value = '';
}

// Función para guardar una tarea en localStorage
function guardarTareaEnLocalStorage(tarea) {
    const tareas = JSON.parse(localStorage.getItem('tasks')) || [];
    tareas.push(tarea);
    localStorage.setItem('tasks', JSON.stringify(tareas));
}

// Función para renderizar una tarea en el DOM
function renderizarTarea(tarea) {
    const li = document.createElement('li');
    li.className = `task-item ${tarea.completed ? 'completed' : ''}`;
    li.innerHTML = `
        <span>${tarea.text}</span>
        <button class="delete-btn">Eliminar</button>
    `;

    // Agregar evento para el botón de eliminar
    li.querySelector('.delete-btn').addEventListener('click', () => {
        eliminarTarea(tarea.text);
        li.remove();
    });

    // Agregar evento para marcar tarea como completada
    li.addEventListener('click', () => {
        tarea.completed = !tarea.completed;
        li.classList.toggle('completed');
        actualizarTareaEnLocalStorage(tarea);
    });

    listaTareas.appendChild(li);
}

// Función para eliminar una tarea de localStorage
function eliminarTarea(textoTarea) {
    const tareas = JSON.parse(localStorage.getItem('tasks')) || [];
    const tareasActualizadas = tareas.filter(tarea => tarea.text !== textoTarea);
    localStorage.setItem('tasks', JSON.stringify(tareasActualizadas));
}

// Función para actualizar una tarea en localStorage
function actualizarTareaEnLocalStorage(tareaActualizada) {
    const tareas = JSON.parse(localStorage.getItem('tasks')) || [];
    const indiceTarea = tareas.findIndex(tarea => tarea.text === tareaActualizada.text);
    if (indiceTarea !== -1) {
        tareas[indiceTarea] = tareaActualizada;
        localStorage.setItem('tasks', JSON.stringify(tareas));
    }
}