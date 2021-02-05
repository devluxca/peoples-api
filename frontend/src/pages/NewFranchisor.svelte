<script>
    import api from '../services/api'
    import { push } from 'svelte-spa-router'

    let name = '';

    async function handleFranchisor() {
        const response = await api.post('franchisor', { name })
        if(response.status == 201) {
            alert('Novo franqueado criado com sucesso')
        }
    }
</script>

<main>
    <div class="row mt-5">
        <div class="col">
            <h4 class="d-inline">adicionar novo franqueado</h4>
        </div>
    </div>
    <div class="container w-50 text-left mt-5">
        <form on:submit|preventDefault={handleFranchisor}>
            <div class="mb-3">
              <label for="inputname" class="form-label">Nome</label>
              <input type="text" bind:value={name} class="form-control" id="inputname">
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