<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    props: {
        text: {type: String, required: true}
    }
})
</script>

<template>
    <div>
        <span id="FlavorText-text">{{ text }}</span>
    </div>
</template>

<style scoped>
#FlavorText-text {
  font-style: italic;
  text-align: center;
}
</style>