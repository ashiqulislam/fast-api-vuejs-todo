<template>
  <div>
    <TodoForm @add-todo="addTodo" />
    <div class="bg-base-100 rounded-lg shadow">
      <div v-if="todos.length === 0" class="p-8 text-center">
        <p>No todos yet. Add one above!</p>
      </div>
      <TodoItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @toggle-complete="toggleComplete"
        @delete-todo="deleteTodo"
      />
    </div>
  </div>
</template>

<script setup>
import TodoForm from './TodoForm.vue'
import TodoItem from './TodoItem.vue'

const props = defineProps({
  todos: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['add-todo', 'toggle-complete', 'delete-todo'])

const addTodo = (text) => {
  emit('add-todo', text)
}

const toggleComplete = (id) => {
  emit('toggle-complete', id)
}

const deleteTodo = (id) => {
  emit('delete-todo', id)
}
</script>