<template>
  <div class="container">
    <div class="inner-container">
      <div class="background"></div>
      <div class="content">
        <div class="max-width">
          <div>
            <h1 class="title">QR Code Generator</h1>
          </div>
          <div class="divider">
            <QRCodeForm @generated="onQRCodeGenerated" @error="onError" />
            <QRCodeDisplay :qrCode="qrCode" />
          </div>
        </div>
      </div>
    </div>
    <Notification
      :message="notificationMessage"
      :type="notificationType"
      @close="closeNotification"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import QRCodeForm from './components/QRCodeForm.vue'
import QRCodeDisplay from './components/QRCodeDisplay.vue'
import Notification from './components/Notification.vue'

const qrCode = ref(null)
const notificationMessage = ref('')
const notificationType = ref('')

const onQRCodeGenerated = (generatedQRCode) => {
  console.log(generatedQRCode)
  qrCode.value = generatedQRCode
}

const onError = (error) => {
  notificationMessage.value = error
  notificationType.value = 'error'
}

const closeNotification = () => {
  notificationMessage.value = ''
  notificationType.value = ''
}
</script>

<style scoped>
.container {
  min-height: 100vh;
  /* background-color: #f7fafc; */
  padding: 1.5rem 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.inner-container {
  position: relative;
  padding: 1.5rem;
  max-width: 24rem;
  margin: auto;
}

.background {
  width: 650px !important;
  height: 650px !important;
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, #22d3ee, #3b82f6);
  box-shadow:
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);
  transform: skewY(-6deg);
  border-radius: 1.5rem;
}

.content {
  width: 550px !important;
  height: 550px !important;
  position: relative;
  padding: 3rem;
  margin-top: 20px;
  margin-left: 25px;
  background-color: white;
  box-shadow:
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);
  border-radius: 1.5rem;
}

.max-width {
  max-width: 16rem;
  margin: auto;
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
}

.divider {
  border-top: 1px solid #e5e7eb;
  margin-top: 1rem;
  padding-top: 1rem;
}

@media (max-width: 640px) {
  .inner-container {
    max-width: 95%; /* Take up more screen width on smaller screens */
    padding: 0.75rem;
  }

  .content {
    padding: 1.5rem; /* Further reduced padding */
  }

  .title {
    font-size: 1rem; /* Even smaller title font */
  }
}
</style>
