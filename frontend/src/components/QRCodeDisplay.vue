<template>
  <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
    <div v-if="qrCode" class="flex justify-center">
      <img :src="qrCode" alt="Generated QR Code" class="w-40 h-40" />
    </div>
    <div v-else class="text-center text-gray-500">
      No QR code generated yet. Enter a URL above to get started.
    </div>
  </div>
</template>

<script setup>
defineProps({
  qrCode: {
    type: String,
    default: null,
  },
})
</script>
