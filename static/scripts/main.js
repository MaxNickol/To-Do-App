// Get all the elements from the form to create a new task
let btn = document.querySelector('.material-icons');
let options = document.querySelector('.items-wrap');
let form = document.querySelector('.form-wrap');

// Get all the elements from the modal window to delete the task!
let module_window_delete = document.querySelector('.module-window');
let form_delete = document.querySelector('.delete_form');
let clear_list = document.querySelectorAll('#clear_btn');
const clear_btn = document.querySelector('.clear');

console.log(clear_btn);

btn.addEventListener('click', open_menu)
function open_menu(event){

    if(event.target == this) {
       options.classList.toggle('open')
    }
    
}

// Restricting of raw input field in the creating of task
form.addEventListener('submit', (e) => {
    if(form_input.value == null || form_input.value == '') {
        e.preventDefault()
        alert('The input field can\'t be blank!')
    } 
})

// Add event listener on all the clear buttons (crosses)
for (const crosses of clear_list) {
    crosses.addEventListener('click', openModule) 
}

// Add the functionality to close the modal window
clear_btn.addEventListener('click', openModule)

function openModule() {
    module_window_delete.classList.toggle('modal-open');
}