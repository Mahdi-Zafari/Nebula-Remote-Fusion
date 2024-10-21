document.getElementById('dropdown-btn').addEventListener('click', function () {
    var menu = document.getElementById('power-options');
    menu.classList.toggle('show');
});

const buttons = document.querySelectorAll('#option-btn');

buttons.forEach(button => {
    button.addEventListener('click', function() {
        const option = this.getAttribute('data');

        if (option === 'Mouse Controller') {
            window.location.href = '/mouse_controller';
        } else if (option === 'Task Manager') {
            window.location.href = '/task_manager';
        } else if (option === 'Remote File Management') {
            window.location.href = '/remote_file_management';
        } else if (option === 'Remote Command Prompt') {
            window.location.href = '/remote_command_prompt';
        }
    });
});
