<template>
  <div class="navbar bg-base-100 shadow-lg">
    <div class="flex-1">
      <router-link to="/" class="btn btn-ghost normal-case text-xl">Todo App</router-link>
    </div>
    <div class="flex-none gap-2">
      <template v-if="authStore.isAuthenticated">
        <router-link to="/todos" class="btn btn-ghost">My Todos</router-link>
        <button @click="handleLogout" class="btn btn-ghost">Logout</button>
      </template>
      <template v-else>
        <router-link to="/login" class="btn btn-ghost">Login</router-link>
        <router-link to="/register" class="btn btn-ghost">Register</router-link>
      </template>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'  // Adjusted path
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>