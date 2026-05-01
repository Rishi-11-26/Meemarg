/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        'telangana': {
          primary: '#FF6B35',
          secondary: '#004E89',
          accent: '#F77F00'
        }
      }
    },
  },
  plugins: [],
}

// Made with Bob
