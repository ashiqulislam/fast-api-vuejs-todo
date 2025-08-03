<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const form = ref({
  name: '',
  email: '',
  password: '',
  confirmPassword: ''
})
const loading = ref(false)

const handleSubmit = async () => {
  if (form.value.password !== form.value.confirmPassword) {
    alert("Passwords don't match")
    return
  }
  
  loading.value = true
  try {
    await auth.register({
      name: form.value.name,
      email: form.value.email,
      password: form.value.password
    })
  } catch (error) {
    alert(error.message)
  } finally {
    loading.value = false
  }
}
</script>
<template>
  <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Register</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-control">
          <label class="label">
            <span class="label-text">Name</span>
          </label>
          <input 
            v-model="form.name"
            type="text" 
            placeholder="name" 
            class="input input-bordered" 
            required
          />
        </div>
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
        <div class="form-control">
          <label class="label">
            <span class="label-text">Confirm Password</span>
          </label>
          <input 
            v-model="form.confirmPassword"
            type="password" 
            placeholder="confirm password" 
            class="input input-bordered" 
            required
          />
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-primary" :disabled="loading">
            <span v-if="loading" class="loading loading-spinner"></span>
            Register
          </button>
        </div>
      </form>
      <div class="text-center mt-4">
        <router-link to="/login" class="link">Already have an account? Login</router-link>
      </div>
    </div>
  </div>
</template>

