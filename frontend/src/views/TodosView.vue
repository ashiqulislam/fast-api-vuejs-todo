<template>
  
  <div class="container mx-auto p-4">
    <div class="max-w-2xl mx-auto">
      <h1 class="text-3xl font-bold mb-8">My Todos</h1>
      <div class="text-center" v-if="todos.loading">
        <span class="loading loading-spinner loading-xl"></span>
      </div>
      <TodoList  v-if="!todos.loading"
        :todos="todos.todos" 
        @add-todo="todos.addTodo"
        @toggle-complete="todos.toggleComplete"
        @delete-todo="todos.deleteTodo"
      />
    </div>
  </div>
</template>

<script setup>
import TodoList from '@/components/Todo/TodoList.vue'
import { useTodosStore } from '@/stores'


const todos = useTodosStore()

todos.fetchTodos()


)
</script>