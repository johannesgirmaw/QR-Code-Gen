<template>
  <div class="qr-form-container">
    <form @submit.prevent="generateQRCode" class="qr-form">
      <div class="input-container">
        <input
          id="url"
          v-model="url"
          type="text"
          class="url-input"
          :class="{ error: errors.url }"
          placeholder="Enter URL"
        />
        <label for="url" class="url-label"> Enter URL </label>
      </div>
      <p v-if="errors.url" class="error-message">{{ errors.url }}</p>
      <div class="button-container">
        <button type="submit" class="submit-button">Generate QR Code</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useQRCodeService } from '../services/qrCodeService'

const url = ref('')
const errors = reactive({})
const qrCodeService = useQRCodeService()

const validateURL = (url) => {
  const pattern = new RegExp(
    '^(https?:\\/\\/)?' +
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' +
      '((\\d{1,3}\\.){3}\\d{1,3}))' +
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' +
      '(\\?[;&a-z\\d%_.~+=-]*)?' +
      '(\\#[-a-z\\d_]*)?$',
    'i',
  )
  return pattern.test(url)
}

const generateQRCode = async () => {
  errors.url = ''
  console.log('Starting QR code generation for:', url.value) // Log the URL

  if (!url.value) {
    errors.url = 'URL is required'
    console.log('URL is missing:', errors.url) // Log the error
    return
  }

  if (!validateURL(url.value)) {
    errors.url = 'Please enter a valid URL'
    console.log('URL is invalid:', errors.url) // Log the error
    return
  }

  try {
    console.log('Calling qrCodeService...') // Log before the service call
    const qrCode = await qrCodeService.generateQRCode(url.value)
    console.log('QR Code generated:', qrCode) // Log the result

    emit('generated', qrCode)
    console.log("Emitted 'generated' event") // Log after emitting
  } catch (error) {
    console.error('Error generating QR code:', error) // Use console.error for errors
    emit('error', error.message || 'An error occurred ...')
    console.log("Emitted 'error' event") // Log after emitting
  }
}
const emit = defineEmits(['generated', 'error'])
</script>

<style scoped>
.qr-form-container {
  padding: 2rem 0;
  font-size: 1rem;
  line-height: 1.5;
  color: #4a5568;
}

.qr-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-container {
  position: relative;
}

.url-input {
  width: 100%;
  height: 2.5rem;
  padding: 0.5rem 0;
  border: none;
  border-bottom: 2px solid #e2e8f0;
  background-color: transparent;
  transition: border-color 0.3s;
  font-size: 1rem;
  color: #1a202c;
}

.url-input:focus {
  outline: none;
  border-color: #e53e3e;
}

.url-input::placeholder {
  color: transparent;
}

.url-label {
  position: absolute;
  left: 0;
  top: 0.5rem;
  transition: all 0.3s;
  font-size: 1rem;
  color: #718096;
}

.url-input:focus ~ .url-label,
.url-input:not(:placeholder-shown) ~ .url-label {
  top: -1rem;
  font-size: 0.875rem;
  color: #4a5568;
}

.url-input.error {
  border-color: #f56565;
}

.error-message {
  color: #f56565;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

.button-container {
  margin-top: 1rem;
}

.submit-button {
  background-color: #4299e1;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-size: 1rem;
  transition: background-color 0.3s;
  border: none;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #3182ce;
}

.submit-button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5);
}
</style>
