<script>
import NavBar from "@/components/navBar.vue";
import MelodyBattleList from "@/components/melodyBattleList.vue";
import {getUser, getMelodyBattleApi} from "@/api.js";
export default {
  name: "MainView",
  components: {NavBar, MelodyBattleList},
  data() {
    return {
      name: 'sigma',
      token: '',
      melodyBattles: [],
      user: {},
    }
  },
  async mounted() {
    let token = localStorage.getItem("token");
    if (!token) {
      this.$router.push("/login");
    }
    this.token = token
    let request = await getUser(token)
    if (request.status_code !== 200) {
      this.$router.push("/login");
    }
    this.user = request.data;

    request = await getMelodyBattleApi(token);
    this.melodyBattles = request.data;

  }
}
</script>

<template>
  <NavBar :username="user.login" />
  <button class="position-absolute end-0 bottom-0 btn me-5 mb-5 text-center px-3 py-2 fs-5" @click="this.$router.push('/create-melody-battle')" style="color: black; background-color:rgba(0,255,255,0.98);">+</button>
  <MelodyBattleList :list="melodyBattles" />
</template>

<style scoped>

</style>