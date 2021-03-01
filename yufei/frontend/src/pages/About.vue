<template>

<div class="jumbotron jumbotron-fluid">
  <div class="container" v-for="item in info" :key="item.id">
    <!-- <h1 class="display-4">Fluid jumbotron</h1> -->
    <p class="lead" v-html="item.content"></p>
  </div>
</div>
</template>

<script>
export default {
  data () {
    return {
      info: []
    }
  },
  mounted () {
    this.$https.get('getaboutus').then((res) => {this.info = res}).catch(err=>{console.log(err)})      
  }
}
</script>

<style scoped>
/* .container{margin-top: 30px;} */
</style>

