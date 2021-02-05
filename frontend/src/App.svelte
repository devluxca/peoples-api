<script>
	import Router from 'svelte-spa-router';
	import routes from './routes';
</script>

<main>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand mb-0 h1" href="/">
            <img src="https://yungas-saas-static.s3-sa-east-1.amazonaws.com/assets/img/logo/logo.png" alt="">
		</a>

        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="/#/people">Pessoas <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/#/franchisor">Franqueados <span class="sr-only">(current)</span></a>
            </li>
        </ul>
    </nav>


	<Router {routes} />
</main>

<style>
	main {
		text-align: center;
		padding: 0px;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
