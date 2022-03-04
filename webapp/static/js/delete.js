var modalDelete = document.getElementById('modalDelete');
modalDelete.addEventListener('show.bs.modal', function (event) {
    var modalTrigger = event.relatedTarget

    var modalForm = modalDelete.querySelector('form')
    var modalObjectDescription = modalDelete.querySelector('.object-description')

    modalForm.action = modalTrigger.getAttribute('data-bs-url');
    modalObjectDescription.textContent = modalTrigger.getAttribute('data-bs-object');
})
