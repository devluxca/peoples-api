<script>
    import api from '../services/api'

    let full_name = '';
    let email = '';
    let franchisor_id = '';

    async function handlePeople() {
        try {
            const response = await api.post('people', {
                full_name,
                email,
                franchisor_id
            })

            if(response.status == 201) {
                alert('Nova pessoa criada com sucesso')
            }
        } catch (error) {
            if (error.request.status == 400) alert('Preencha o formulário corretamente')
            if (error.request.status == 404) alert(error.response.data.message)
            if (error.request.status == 409) alert(error.response.data.message)
        }

    }
</script>

<main>
    <div class="row mt-5">
        <div class="col">
            <h4 class="d-inline">adicionar nova pessoa</h4>
        </div>
    </div>
    <div class="container w-50 text-left mt-5">
        <form on:submit|preventDefault={handlePeople}>
            <div class="mb-3">
              <label for="inputname" class="form-label">Nome completo</label>
              <input type="text" bind:value={full_name} class="form-control" id="inputname">
            </div>
            <div class="mb-3">
                <label for="inputemail" class="form-label">Email</label>
                <input type="email" bind:value={email} class="form-control" id="inputemail">
            </div>
            <div class="mb-3">
              <label for="inputfranchisor" class="form-label">Franqueado</label>
              <input type="number" bind:value={franchisor_id} class="form-control" id="inputfranchisor">
            </div>
            <button type="submit" class="btn btn-primary">Adicionar</button>
        </form>
    </div>
</main>

<style>
	h4 {
		color: #008cff;
		text-transform: uppercase;
		font-size: 3em;
		font-weight: 300;
	}
</style>