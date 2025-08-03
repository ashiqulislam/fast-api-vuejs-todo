<template>
  <div class="mb-8">
    <form @submit.prevent="handleSubmit" class="flex gap-2">
      <input
        v-model="newTodo"
        type="text"
        placeholder="Add a new todo"
        class="input input-bordered w-full"
        required
      />
      <button type="submit" class="btn btn-primary">
        Add
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const newTodo = ref('')
const emit = defineEmits(['add-todo'])

const handleSubmit = () => {
  emit('add-todo', newTodo.value)
  newTodo.value = ''
}
</script>