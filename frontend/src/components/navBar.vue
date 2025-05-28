<script>
export default {
  name: "NavBar",
  props: {
    username: {
      type: String,
      required: true,
    }
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    }
  }
}
</script>

<template>
  <nav class="navbar navbar-dark" style="background-color: #052b6a; color: white">
    <div class="container-fluid">
      <a class="navbar-brand ms-5" href="/">Mb</a>
      <div class="nav-item dropdown me-5">
        <a class="nav-link dropdown-toggle" href="#" id="navDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="true">{{username}}</a>
        <ul class="dropdown-menu" aria-labelledby="navDropdown">
          <li class="pe-0"><a class="dropdown-item" @click="logout" href="/">logout</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>

</style>