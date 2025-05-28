import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './views/HomeView.vue';
import AnalyzeLicitacao from './views/AnalyzeLicitacao.vue';
import ReportsView from './views/ReportsView.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/analyze', name: 'Analyze Licitacao', component: AnalyzeLicitacao },
  { path: '/reports', name: 'Reports', component: ReportsView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;