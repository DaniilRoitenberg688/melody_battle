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
    },
    remove (mbId) {
      this.$emit('delete', mbId)
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
          <div>
            <h2 class="card-title ms-3">{{item.name}}</h2>
            <a class="btn btn-danger mb-3 ms-3 mt-3" @click="remove(item.id)"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
              <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5M8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5m3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0"/>
            </svg></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>