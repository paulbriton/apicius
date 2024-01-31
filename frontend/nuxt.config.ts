// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/input.css'],
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/color-mode',
    'nuxt-icon',
    '@nuxtjs/apollo',
  ],
  colorMode: {
    classSuffix: ''
  },
  apollo: { 
    clients: { 
      default: { 
        httpEndpoint: 'http://127.0.0.1:8000/graphql' 
      } 
    }, 
  },
})
