<template>
<div class="container">

<div v-for="item in info" :key="item.id">
<hr>
<div class="row"></div>
<div class="card bg-dark text-white" @click="clto(item.id)">
  <img v-bind:src="item.thumbnail" class="card-img" alt="...">
  <div class="card-img-overlay">
    <h1 class="card-title">{{item.name}}</h1>
    <p class="card-text">{{item.text}}</p>
  </div>
</div>
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
    this.$https.get('getallnewstype').then((res) => {this.info = res}).catch(err=>{console.log(err)})
  },
  methods:{
    clto:function(data){
      this.$router.push({ path: '/detailslist', query: { type:1,typeid:data }})
    }
  } 
}
</script>

<style scoped>
.card-img-overlay{text-align: center;margin-top:2cm;}
</style>