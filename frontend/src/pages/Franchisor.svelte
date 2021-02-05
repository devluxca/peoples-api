<script>
    import Pagination from '../components/Pagination.svelte'
    import FranchisorTable from '../components/Tables/FranchisorTable.svelte'
    import ButtonNewFranchisor from '../components/Buttons/ButtonNewFranchisor.svelte'
    import api from '../services/api'

    export let params = {}
    $: page = parseInt(params.page) || 1

    $: promise = api.get(`franchisor/${page}`)
</script>

<main>
    <div class="row mt-5">
        <div class="col">
            <h4 class="d-inline">lista de franqueados</h4>
        </div>
    </div>
    <div class="row">
        <div class="col mt-4">
            <ButtonNewFranchisor />
        </div>
    </div>
    <div class="container">
        {#await promise then { data }}
        <FranchisorTable {data} />
        <Pagination {data} {page} />
        {/await}

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

