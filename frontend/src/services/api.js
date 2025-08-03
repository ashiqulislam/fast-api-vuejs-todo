import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import { toast } from 'vue3-toastify'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 5000
})

// Request interceptor to add auth token
api.interceptors.request.use(config => {
  const authStore = useAuthStore()
  
  if (authStore.token) {
    config.headers.Authorization = `Bearer ${authStore.token}`
  }
  return config
}, error => {
  toast.error('Network error occurred')
  return Promise.reject(error)
})

// Response interceptor to handle 401 errors
api.interceptors.response.use(response => response, error => {
  if (error.response?.status === 401) {
    const authStore = useAuthStore()
    authStore.logout()
  }
  return Promise.reject(error)
})

export default api