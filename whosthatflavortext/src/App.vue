<script lang="ts">
import FlavorText from './components/FlavorText.vue'
import GuessForm from './components/GuessForm.vue'
export default {
  components: {
    FlavorText,
    GuessForm
  },
  data() {
    return {
      data: {},
      choices: [],
      guess: "",
      guessing: true,
      correct: false
    }
  },
  beforeMount(){
    this.getData();
  },
  methods: {
    async getData() {
      const res = await fetch(window.location.href + "data/cards.json");
      const data = await res.json();
      const startDate = new Date("11 May 2023");
      const timeDiff = new Date().getTime() - startDate.getTime();
      var index = Math.floor(Math.abs(timeDiff / (1000 * 3600 * 24))) % data.length;
      this.data = data[index];
      var choices = [];
      data.forEach(element => choices.push(element.name));
      this.choices = choices;
      console.log(this.data);
    },
    processResult(r: Boolean) {
      this.guessing = false;
      this.correct = r;
    }
  }
}
</script>

<template>
  <header>
    <span id="title">WHO'S THAT FLAVOR TEXT?</span>
  </header>
  <div class="wrapper">
    <div v-if="guessing" id="guessing-container">
      <div id="flavor-text-container">
        <FlavorText :text=data.text />
      </div>
      <div id="guess-container">
        <GuessForm :solution=data.name @result="processResult" />
      </div>
    </div>
    <div v-if="!guessing"><p>{{ correct }}</p></div>
  </div>
</template>

<style scoped>
header {
  height: 20%;
  border-bottom: 2px solid white;
  margin-bottom: 10%;
}

.wrapper {
  width: 100%;
}

#guessing-container {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
}

#flavor-text-container {
  width: 100%;
  float: left;
}

#guess-container {
  width: 100%;
  float: left;
  margin: 0 auto;
  text-align: center;
}

@media (min-width: 1024px) {
  .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
