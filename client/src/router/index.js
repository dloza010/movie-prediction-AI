import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/Homepage.vue';
import Trending from '@/views/Trending.vue';

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/trending',
        name: 'TrendingPage',
        component: Trending
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
