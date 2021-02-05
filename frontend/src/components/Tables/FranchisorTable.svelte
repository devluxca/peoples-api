<script>
    import api from '../../services/api'
    export let data;
    
    $: results = data.results

    async function deleteFranchisor(franchisor_id) {
        const response = await api.delete(`franchisor/${franchisor_id}`)

        if (response.status == 200) {
            results = results.filter(franchisor => franchisor.id != franchisor_id)
            alert('Franqueado deletado com sucesso.')
        }
    }
</script>

<table class="table mt-5">
    <thead>
    <tr>
        <th scope="col" class="text-center">ID</th>
        <th scope="col" class="text-center">Nome</th>
        <th scope="col" class="text-center">Actions</th>
    </tr>
    </thead>
    <tbody>
        {#each results as franchisor} 
            <tr>
                <th scope="row" class="text-center">{franchisor.id}</th>
                <td class="text-center">{franchisor.name}</td>
                <td>
                    <div class="row">
                        <div class="col-sm">
                            <a href="/#/edit/franchisor/{franchisor.id}" class="btn btn-success btn-block">Editar</a>
                        </div>
                        <div class="col-sm">
                            <button on:click={deleteFranchisor(franchisor.id)} class="btn btn-danger btn-block">Deletar</button>
                        </div>
                    </div>
                </td>
            </tr>
        {/each}
    </tbody>
</table>