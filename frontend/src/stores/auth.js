import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { toast } from 'vue3-toastify'
import api from '@/services/api' 

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()
  const user = ref(null)
  const token = ref(localStorage.getItem('token') || null)
  
  // Set axios default headers if token exists
  if (token.value) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
  }

  const isAuthenticated = computed(() => !!token.value)

  const login = async (credentials) => {
    try {
      const response = await api.post('auth/login', credentials)
      
      // Store token and user data
      token.value = response.data.data.access_token
      user.value = response.data.data.user
      
      // Set axios auth header
      api.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
      
      // Save to localStorage
      localStorage.setItem('token', token.value)
      localStorage.setItem('user', JSON.stringify(user.value))
      toast.success('Login successfully')
      router.push('/todos')
      return response.data
    } catch (error) {
      const message = error.response?.data?.data?.detail || 'Login failed'
      toast.error(message)
      throw message
    }
  }

  const register = async (userData) => {
    try {
      const response = await api.post(api_url+'auth/register', userData)
      return response.data
    } catch (error) {
      throw error.response?.data?.data?.detail || 'Registration failed'
    }
  }

  const logout = () => {
    // Clear all auth data
    token.value = null
    user.value = null
    delete api.defaults.headers.common['Authorization']
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    // toast.info('You have been logged out')
    router.push('/login')
  }

  // Initialize from localStorage
  const initFromStorage = () => {
    const storedUser = localStorage.getItem('user')
    if (storedUser) {
      user.value = JSON.parse(storedUser)
    }
  }

  return {
    user,
    token,
    isAuthenticated,
    login,
    register,
    logout,
    initFromStorage,
  }
})