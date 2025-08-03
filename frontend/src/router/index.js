import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Import your views/components
import HomeView from '@/views/HomeView.vue'
import AuthView from '@/views/AuthView.vue'
import TodosView from '@/views/TodosView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: AuthView
  },
  {
    path: '/register',
    name: 'register',
    component: AuthView
  },
  {
    path: '/todos',
    name: 'todos',
    component: TodosView,
    meta: { requiresAuth: true } // Protected route
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Navigation guard for protected routes
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router