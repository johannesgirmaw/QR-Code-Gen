<template>
  <transition name="fade">
    <div v-if="message" class="notification" :class="typeClasses">
      <p>{{ message }}</p>
      <button @click="$emit('close')" class="close-button">
        <svg class="icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </div>
  </transition>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  message: {
    type: String,
    default: '',
  },
  type: {
    type: String,
    default: 'info',
  },
})

const typeClasses = computed(() => {
  switch (props.type) {
    case 'error':
      return 'error'
    case 'success':
      return 'success'
    default:
      return 'info'
  }
})

defineEmits(['close'])
</script>

<style scoped>
.notification {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  color: white;
}

.info {
  background-color: #3b82f6; /* Blue */
}

.success {
  background-color: #10b981; /* Green */
}

.error {
  background-color: #ef4444; /* Red */
}

.close-button {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 0.25rem;
  margin-right: 0.25rem;
  color: white;
  cursor: pointer;
}

.close-button:hover {
  color: #e5e7eb; /* Light gray */
}

.icon {
  height: 1rem;
  width: 1rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
