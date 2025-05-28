<script>
import {host} from "@/api.js";

export default {
  name: 'MelodyBattleList',
  props: {
    list: []
  },
  methods: {
    async get_image() {
      let image = await fetch(`${host}/get_image/melody_battles_images/12.png`, {method: "GET"})
      return image
    }
  }
}
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-3 col-md-6 col-sm-12 col-12 mt-5" v-for="item in list">
        <div class="card">
<!--          <img class="card-img-top" :src="`${host}/get_image/melody_battles_images/12.png`" />-->
<!--          <img class="card-img-top" :src="`../../backend/app/static/melody_battles_images/12.png`" />-->
<!--          <img class="card-img-top" src="https://localhost:5000/app/static/melody_battles_images/12.png" />-->
<!--          <img src="url">-->
          <img :src="`static/${item.id}.png`" class="card-img-top" @click="console.log(item.image_url)"  />
          <h2 class="card-title ms-3">{{item.name}}</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>