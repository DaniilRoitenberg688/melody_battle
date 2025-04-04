<script>
import AuthWindow from "@/components/AuthWindow.vue";
export default {
  name: 'App',
  components: {AuthWindow},
  data(){
    return {
      a: 'aaaaa',
      fields: [
        {
          label: 'login',
          placeholder: 'login',
          value: ''
        },
        {
          label: 'email',
          placeholder: 'email',
          value: 'test@example.com'
        },
        {
          label: 'password',
          placeholder: 'password',
          value: ''
        },
        {
          label: 'password_again',
          placeholder: 'password',
          value: ''
        }
      ],
      submit_text: 'register',
      name: 'register form',
      error_message: 'passwords not match',
    }
  },
  mounted() {
    this.$router.push('/');
  }
}

</script>

<template>
  <RouterView/>
</template>