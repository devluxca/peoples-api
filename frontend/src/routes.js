import Home from './pages/Home.svelte';
import People from './pages/People.svelte';
import NewPeople from './pages/NewPeople.svelte';

import Franchisor from './pages/Franchisor.svelte';
import NewFranchisor from './pages/NewFranchisor.svelte';
import EditFranchisor from './pages/EditFranchisor.svelte';
import NotFound from './pages/NotFound.svelte';

export default {
    '/': Home,
    '/people': People,
    '/people/:page': People,
    '/new/people': NewPeople,
    '/franchisor': Franchisor,
    '/franchisor/:page': Franchisor,
    '/new/franchisor': NewFranchisor,
    '/edit/franchisor/:franchisor_id': EditFranchisor,
    '*': NotFound
};
