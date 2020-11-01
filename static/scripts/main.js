// Get all the elements from the form to create a new task
let btn = document.querySelector('.material-icons');
let options = document.querySelector('.items-wrap');
let form = document.querySelector('.form-wrap');
let form_input = document.querySelector('.input');

// Get all the elements from the modal window to delete the task!

let form_delete = document.querySelector('.delete_form');
let clear_list = document.querySelectorAll('#clear_btn');


btn.addEventListener('click', open_menu)
function open_menu(event){

    if(event.target == this) {
       options.classList.toggle('open')
    }
    
}

console.log(form);

// Restrict the raw input field in the creating of task
form.addEventListener('submit', (e) => {
    if(form_input.value == null || form_input.value == '') {
        e.preventDefault()
        alert('The input field can\'t be blank!')
    } 
})

