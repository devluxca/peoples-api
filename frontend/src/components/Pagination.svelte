<script>
    export let page;
    export let data;
</script>

<div id="navigator">
    <nav>
        <ul class="pagination">
          {#if page - 1 < 1}
          <li class="page-item disabled"><a class="page-link" href="/#/">Anterior</a></li>
          {:else}
          <li class="page-item"><a class="page-link" href="/#/franchisor/{ page - 1 }">Anterior</a></li>
          {/if}

          {#each [...Array(data.total_pages + 1).keys()].splice(1, data.total_pages) as pages}
            {#if page == pages}
            <!-- svelte-ignore a11y-missing-attribute -->
            <li class="page-item active"><a class="page-link">{pages}</a></li>
            {:else}
            <li class="page-item"><a class="page-link" href="/#/franchisor/{ pages }">{pages}</a></li>
            {/if}
          {/each}
          {#if page + 1 > data.total_pages}
          <li class="page-item disabled"><a class="page-link" href="/#/">Próximo</a></li>
          {:else}
          <li class="page-item"><a class="page-link" href="/#/franchisor/{ page + 1 }">Próximo</a></li>
          {/if}
        </ul>
    </nav>
</div>