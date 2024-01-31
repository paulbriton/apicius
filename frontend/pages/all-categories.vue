<template>
    <div class="flex flex-col place-content-center place-items-center">
        <div class="py-8 border-b-2">
            <h1 class="text-5xl font-extrabold">All Categories</h1>
        </div>
        <div class="flex flex-wrap py-8">
            <NuxtLink v-for="category in data.allRecipeTypes" :key="category.name" class=". . ."
                :to="`/category/${category.name}`">{{ category.name }}</NuxtLink>
        </div>
    </div>
</template>
  

<script lang="ts" setup>

const query = gql`  
    query getCategories {    
        allRecipeTypes {      
            id      
            name    
        }  
    }`
const { data } = await useAsyncQuery(query)
console.log(data.allRecipeTypes)
</script>