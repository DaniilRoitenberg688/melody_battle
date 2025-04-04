<script>
import NavBar from "@/components/navBar.vue";
import {getUser} from "@/api.js";
import {createMelodyBattleApi} from "@/api.js";

export default {
  name: 'createMelodyBattle',
  components: {NavBar},
  data() {
    return {
      user: {},
      url: '',
      is_created: false,
      is_error: false,
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
  },
  methods: {
    async createMelodyBattle() {
      let token = localStorage.getItem("token");
      let request = await createMelodyBattleApi(token, this.url);
      if (request.status_code !== 201) {
        this.is_error = true;
        console.log(request.data);
      }
      else {
        this.is_created = true;
        this.is_error = false
      }

    }
  }
}

</script>

<template>
  <NavBar :username="user.login"/>
  <div class="container">
    <div class="row">
      <div class="container position-relative">
        <div class="card col-12 col-lg-5 col-md-6 col-sm-6 px-4 py-4 mt-5 start-50 translate-middle-x text-center">

          <h1 class="card-title mb-3">Create melody battle</h1>

          <form method="post" action="" novalidate>
            <div class="mb-4">
              <label class="form-label" for="a"></label>
              <input class="form-control" id="a" required placeholder="play list url" v-model="url" />

            </div>
            <div class="alert alert-success" v-if="is_created">Melody battle created successfully</div>
            <div class="alert alert-danger" v-if="is_error">Something went wrong</div>
            <div>
              <a class="btn btn-outline-danger mx-3" v-if="is_created || is_error" href="/">back</a>
              <a class="btn btn-success mx-3" @click="createMelodyBattle">create</a>
            </div>
          </form>


        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>