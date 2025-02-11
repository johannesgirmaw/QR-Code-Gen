import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Base URL for your backend
  withCredentials: true, // Include credentials if needed
  headers: {
    'Content-Type': 'application/json',
  },
})

export const useQRCodeService = () => {
  const generateQRCode = async (url: string): Promise<string> => {
    try {
      const response = await axiosInstance.post('/api/generate-qr/', { url })
      console.log('================================', response)
      return response.data.qrCode
    } catch (error) {
      console.error('Error generating QR code:', error)
      throw new Error(error instanceof Error ? error.message : 'Failed to generate QR code')
    }
  }

  return {
    generateQRCode,
  }
}
