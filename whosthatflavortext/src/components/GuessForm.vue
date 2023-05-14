<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    props: {
        solution: {type: String, required: true},
        choices: {type: String[], required: true}
    },
    data() {
        return {
            guess: ""
        }
    },
    methods: {
        submitGuess() {
            this.$emit('result', this.guess == this.solution)
        },
        autocomplete() {
            
        }
    }
})
</script>

<template>
    <div>
        <div class="autocomplete">
            <input v-model="guess" type="text" id="guess-input" name="guess-input" placeholder="Island">
        </div>
        <button class="guess-input-button" id="guess-input-button" @click="submitGuess">Guess</button>
    </div>
</template>

<style>
.autocomplete {
  /*the container must be positioned relative:*/
  position: relative;
  display: inline-block;
}


</style>