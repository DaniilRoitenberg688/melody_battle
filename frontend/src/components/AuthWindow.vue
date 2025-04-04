<script>
export default {
  name: "AuthWindow",
  props: {
    fields: {
      type: Array,
    },
    submit_text: {
      type: String,
    },
    name: {
      type: String,
    },
    error_message: {
      type: String,

    },
    another_text: {
      type: String,

    },
    another_link: {
      type: String,
    }
  },
  methods: {
    sendData () {
      let is_error = false;
      for (let i = 0; i < this.fields.length; i++) {
        if (!this.fields[i].value) {
          console.log(this.fields[i].error)
          this.fields[i].error = 'field value is required'
          is_error = true;

        }
        else {
          this.fields[i].error = ''
        }
      }
      if (!is_error) {
        this.$emit('send', this.fields)
      }
    }
  }
}


</script>

<template>
  <div class="container">
    <div class="row">
      <div class="container position-relative">
        <div class="card col-12 col-lg-5 col-md-6 col-sm-6 px-4 py-4 mt-5 start-50 translate-middle-x text-center">

          <h1 class="card-title mb-4">{{ name }}</h1>

          <form method="post" action="" novalidate>
            <div v-for="field in fields" :key="field">
              <div class="mb-4">
                <label class="form-label" :for="field.label">{{ field.label }}</label>
                <input class="form-control" type="password" v-model="field.value" :id="field.label"
                       :placeholder="field.placeholder" v-if="field.label.indexOf('password') !== -1" required/>
                <input class="form-control" type="text" v-model="field.value" :id="field.label"
                       :placeholder="field.placeholder" v-else required/>
                <div class="alert alert-danger mt-2 p-2" v-if="field.error">{{field.error}}</div>
              </div>
            </div>
            <p class="text-danger mb-5">{{ error_message }}</p>
            <div>
              <a class="btn btn-outline-secondary mx-3" @click="this.$router.push(another_link)">{{ another_text }}</a>
              <a class="btn btn-primary" @click="sendData">{{ submit_text }}</a>
            </div>
          </form>

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>