<script setup>
const colorMode = useColorMode()
const changeColor = () => (colorMode.preference = (colorMode.value === 'light' ? 'dark' : 'light'))
</script>

<template>
    <div class="flex-none md:order-3 grow-0">
        <button aria-label="Color Mode" class="inline-block text-sm px-2 py-2 leading-none border rounded text-gray-900 bg-gray-100 border-gray:200 dark:border-gray-900 hover:border-transparent dark:bg-teal-800 mt-4 lg:mt-0"
                @click="changeColor">
            <ColorScheme placeholder="...">
                <Icon v-if="colorMode.value === 'dark'" name="heroicons-outline:moon" class="text-md " />
                <Icon v-else name="heroicons-outline:sun" class="text-md" />
            </ColorScheme>
        </button>
    </div>
</template>