<script lang="ts">
import { defineComponent, PropType } from 'vue'
export default defineComponent({
    props: {
        solution: {type: String, required: true},
        choices: {type: Array as PropType<string[]>, required: true}
    },
    data() {
        return {
            guess: "",
            currentFocus: 0
        }
    },
    methods: {
        submitGuess() {
            this.$emit('result', this.guess == this.solution)
        },
        autocompleteInput(event) {
            var inp = document.getElementById("guess-input");
            var a, b, i, val = inp.value;
            this.closeAllLists()
            if (!val) { return false; }
            this.currentFocus = -1;
            a = document.createElement("DIV");                  //create DIV for autocomplete list
            a.setAttribute("id", inp.id + "-autocomplete-list"); //ADD autocomplete-list to ID
            a.setAttribute("class", "autocomplete-items");      //ADD autocomplete-items class
            inp.parentNode.appendChild(a);
            for (i = 0; i < this.choices.length; i++) {
                if (this.choices[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                    b = document.createElement("DIV"); //create DIV per suggestion
                    b.innerHTML = "<strong>" + this.choices[i].substr(0, val.length) + "</strong>";
                    b.innerHTML += this.choices[i].substr(val.length);
                    b.innerHTML += '<input type="hidden" value="' + this.choices[i] + '">';
                    b.addEventListener("click", function(e) {
                        var inp = document.getElementById("guess-input");
                        inp.value = this.getElementsByTagName("input")[0].value;
                        this.closeAllLists();
                    });
                    a.appendChild(b);
                }
            }
        },
        autocompleteKeydown(event) {
            var inp = document.getElementById("guess-input");
            var x = document.getElementById(inp.id + "-autocomplete-list");
            if (x) x = x.getElementsByTagName("div");
            if (event.keyCode == 40) { //DOWN ARROW
                currentFocus++;
                this.addActive(x);
            } else if (event.keyCode == 38) {   //UP ARROW
                currentFocus--;
                this.addActive(x);
            } else if (event.keyCode == 13) {   //ENTER
                if (currentFocus > -1) {
                    if (x) x[currentFocus].click();
                }
            }
        },
        addActive(x) {
            if (!x) return false;
            this.removeActive(x);
            if (currentFocus >= x.length) currentFocus = 0;
            if (currentFocus < 0) currentFocus = (x.length - 1);
            x[currentFocus].classList.add("autocomplete-active");
        },
        removeActive(x) {
            for (var i = 0; i < x.length; i++) {
                x[i].classList.remove("autocomplete-active");
            }
        },
        closeAllLists(element) {
            var inp = document.getElementById("guess-input");
            var x = document.getElementsByClassName("autocomplete-items");
            for (var i = 0; i < x.length; i++) {
                if (element != x[i] && element != inp) {
                    x[i].parentNode.removeChild(x[i]);
                }
            }
        }
    },
    mounted() {
        this.$el.addEventListener("click", this.closeAllLists);
    },
    destroyed() {
        this.$el.removeEventListener("click", this.closeAllLists);
    }
})
</script>

<template>
    <div>
        <div class="autocomplete">
            <input v-model="guess" type="text" id="guess-input" name="guess-input" placeholder="Island" @input="autocompleteInput" @keydown="autocompleteKeydown">
        </div>
        <button class="guess-input-button" id="guess-input-button" @click="submitGuess">Guess</button>
    </div>
</template>

<style>
.autocomplete {
  position: relative;
  display: inline-block;
  background: white;
}


</style>