<template>
  <div class="hero min-h-screen bg-base-200">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Todo App</h1>
        <p class="py-6">Organize your life with this simple todo application.</p>
      </div>
      <component :is="authComponent" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import LoginForm from '../components/Auth/LoginForm.vue'
import RegisterForm from '../components/Auth/RegisterForm.vue'

const route = useRoute()
const authComponent = computed(() => route.path === '/login' ? LoginForm : RegisterForm)
</script>