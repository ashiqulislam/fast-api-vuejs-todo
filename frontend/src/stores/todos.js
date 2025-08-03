import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/services/api' 
import { toast } from 'vue3-toastify'

export const useTodosStore = defineStore('todos', () => {
  const todos = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Fetch all todos from API
  const fetchTodos = async () => {
    loading.value = true
    error.value = null
    try {
      const response = await api.get('/todos')
      todos.value = response.data.data
    } catch (err) {
      error.value = err.response?.data?.data?.detail || 'Failed to fetch todos'
      console.error('Error fetching todos:', err)
    } finally {
      loading.value = false
    }
  }

  // Add new todo via API
  const addTodo = async (title) => {
    loading.value = true
    try {
      const response = await api.post('/todos', {
        title,
        completed: false
      })
      toast.success('Todo add successfully')
      todos.value.push(response.data.data)
    } catch (err) {
      error.value = err.response?.data?.data?.detail || 'Failed to add todo'
      console.error('Error adding todo:', err)
      toast.error(error.value)
      throw err
    } finally {
      loading.value = false
    }
  }

  // Toggle todo completion status via API
  const toggleComplete = async (id) => {
    const todo = todos.value.find(t => t.id === id)
    if (!todo) return

    loading.value = true
    try {
      const response = await api.put(`/todos/${id}`, {
        title: todo.title,
        completed: !todo.completed
      })
      Object.assign(todo, response.data.data)
      toast.success('Todo update successfully')
    } catch (err) {
      error.value = err.response?.data?.data?.detail || 'Failed to update todo'
      console.error('Error updating todo:', err)
      toast.error(error.value)
      throw err
    } finally {
      loading.value = false
    }
  }

  // Delete todo via API
  const deleteTodo = async (id) => {
    loading.value = true
    try {
      await api.delete(`/todos/${id}`)
      todos.value = todos.value.filter(todo => todo.id !== id)
      toast.success('Todo delete successfully')
    } catch (err) {
      error.value = err.response?.data?.data?.detail || 'Failed to delete todo'
      console.error('Error deleting todo:', err)
      toast.error(error.value)
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    todos,
    loading,
    error,
    fetchTodos,
    addTodo,
    toggleComplete,
    deleteTodo
  }
})