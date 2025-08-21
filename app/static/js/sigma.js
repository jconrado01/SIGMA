<script>
document.getElementById('formCambiarPassword').addEventListener('submit', function(e) {
  e.preventDefault(); // Evita el envío normal

  const form = e.target;
  const datos = new FormData(form);

  fetch('/cambiar_password', {
    method: 'POST',
    body: datos
  })
  .then(res => res.json())
  .then(data => {
    const respuesta = document.getElementById('respuestaPassword');
    respuesta.innerHTML = `
      <div class="alert alert-${data.estado} alert-dismissible fade show" role="alert">
        ${data.mensaje}
        <button type="button" class="close" data-dismiss="alert" aria-label="Cerrar">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
    `;

    if (data.estado === 'success') {
      form.reset(); // limpia campos
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
</script>
