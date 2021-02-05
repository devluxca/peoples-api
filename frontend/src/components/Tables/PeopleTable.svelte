<script>
    import api from '../../services/api'
    export let data;
    
    $: results = data.results

    async function deletePeople(people_id) {
        const response = await api.delete(`people/${people_id}`)

        if (response.status == 200) {
            results = results.filter(people => people.id != people_id)
            alert('Pessoa deletada com sucesso.')
        }
    }
</script>

<table class="table mt-5">
    <thead>
    <tr>
        <th scope="col" class="text-center">ID</th>
        <th scope="col" class="text-center">Nome</th>
        <th scope="col" class="text-center">E-mail</th>
        <th scope="col" class="text-center">ID Franqueado</th>
        <th scope="col" class="text-center">Actions</th>
    </tr>
    </thead>
    <tbody>
        {#each results as people} 
            <tr>
                <th scope="row" class="text-center">{people.id}</th>
                <td class="text-center">{people.full_name}</td>
                <td class="text-center">{people.email}</td>
                <td class="text-center">{people.franchisor_id}</td>
                <td>
                    <button on:click={deletePeople(people.id)} class="btn btn-danger btn-block">Deletar</button>
                </td>
            </tr>
        {/each}
    </tbody>
</table>