<script>
import AuthWindow from "@/components/AuthWindow.vue";
import {login} from "@/api.js";

export default {
  name: 'RegisterView',
  components: {AuthWindow},
  data() {
    return {
      a: 'aaaaa',
      fields: [
        {
          label: 'email',
          placeholder: 'email',
          value: 'test@example.com',
          error: ''
        },
        {
          label: 'password',
          placeholder: 'password',
          value: '',
          error: ''
        },

      ],
      submit_text: 'login',
      name: 'Login',
      error_message: '',
      another_text: 'register',
      another_link: '/register'
    }
  },
  methods:{
    async loginUser(){
      let data = {
        email: this.fields[0].value,
        password: this.fields[1].value
      }
      let request = await login(data)
      if (request.status_code !== 200){
        this.error_message = 'check your email or password'
      }
      else {
        localStorage.setItem('token', request.data.token)
        this.$router.push('/')
      }
    }
  }
}
</script>

<template>
  <AuthWindow @send="loginUser" :name="name" :submit_text="submit_text" :fields="fields" :error_message="error_message" :another_text="another_text" :another_link="another_link" />
  <div class="text-center mt-0">
  </div>
</template>

<style scoped>

</style>