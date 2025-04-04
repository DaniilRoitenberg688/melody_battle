<script>
import AuthWindow from "@/components/AuthWindow.vue";
import {register} from "@/api";
import data from "bootstrap/js/src/dom/data.js";

export default {
  name: 'RegisterView',
  components: {AuthWindow},
  data() {
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
      error_message: '',
      another_text: 'login',
      another_link: '/login',

    }
  },
  methods: {
    async sendData(fields) {
      let password = fields.filter((field) => field.label === 'password')[0];
      let password_again = fields.filter((field) => field.label === 'password_again')[0];
      if (password_again.value !== password.value) {
        this.error_message = 'passwords not match';
      } else {
        let user_data = {}
        for (let i = 0; i < this.fields.length; i++) {

          user_data[this.fields[i].label] = this.fields[i].value;
        }
        console.log(user_data);
        let data = await register(user_data)
        if (data.status_code === 201) {
          this.$router.push('/login');
        } else {
          console.log(data.data.reason)
          this.error_message = data.data.reason

        }
      }
    }
  }
}

</script>

<template>
  <AuthWindow :name="name" :submit_text="submit_text" :fields="fields" :error_message="error_message"
              :another_text="another_text" :another_link="another_link" @send="sendData"/>
</template>

<style scoped>

</style>