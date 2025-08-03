<template>
  <div class="flex items-center justify-between p-4 border-b">
    <div class="flex items-center gap-4">
      <input 
        type="checkbox" 
        :checked="todo.completed" 
        @change="emit('toggle-complete', todo.id)"
        class="checkbox checkbox-primary"
      />
      <span :class="{ 'line-through': todo.completed }">{{ todo.title }}</span>
    </div>
    <button 
      @click="emit('delete-todo', todo.id)"
      class="btn btn-sm btn-error"
    >
      Delete
    </button>
  </div>
</template>

<script setup>
defineProps({
  todo: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['toggle-complete', 'delete-todo'])
</script>