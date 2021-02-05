<script>
    import { onMount } from 'svelte';
    import Input from '../components/Input/Input.svelte'

    import api from '../services/api'

    export let params = {}
    $: franchisor_id = params.franchisor_id || ''

    let response;
    let name;
    onMount(async () => {
        response = await api.get(`franchisor/show/${franchisor_id}`)
        name = response.data.name
    })

    async function handleUpdateFranchisor(){
        
        const res = await api.put(`franchisor/${franchisor_id}`, {name})
        if (res.status == 200) {
            alert('Franqueado salvo!')
        }
    }
</script>

<main>
    <div class="row mt-5">
        <div class="col">
            <h4 class="d-inline">editar franqueado</h4>
        </div>
    </div>
    <div class="container w-50 text-left mt-5">
        <form on:submit|preventDefault={handleUpdateFranchisor}>
            <div class="mb-3">
              <label for="inputname" class="form-label">Nome</label>
              <Input type="text" bind:data={name} class="form-control" id="inputname" />
            </div>
            <button type="submit" class="btn btn-primary">Salvar</button>
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

