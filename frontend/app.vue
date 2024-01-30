<script setup>
import { onMounted } from 'vue'
import { initModals } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
  initModals();
})
</script>


<template>
  <div>
    <AppHeader />
    <NuxtPage /> 
    <AppFooter />
  </div>
</template>