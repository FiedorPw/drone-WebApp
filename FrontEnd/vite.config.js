import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path'; // Import the path module

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // Correct alias setup
    },
  },
  server: {
    host: '0.0.0.0',
    port: 80, // You can change this port if needed
  },
});
