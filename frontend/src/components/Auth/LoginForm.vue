<template>
  <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Login</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-control">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input 
            v-model="form.email"
            type="email" 
            placeholder="email" 
            class="input input-bordered" 
            required
          />
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Password</span>
          </label>
          <input 
            v-model="form.password"
            type="password" 
            placeholder="password" 
            class="input input-bordered" 
            required
          />
        </div>
        <div v-if="error" class="alert alert-error mt-4">
          <span>{{ error }}</span>
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-primary" :disabled="loading">
            <span v-if="loading" class="loading loading-spinner"></span>
            Login
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const form = ref({
  email: '',
  password: ''
})
const loading = ref(false)
const error = ref(null)

const handleSubmit = async () => {
  error.value = null
  loading.value = true
  
  try {
    await authStore.login(form.value)
  } catch (err) {
    error.value = err
  } finally {
    loading.value = false
  }
}
</script>