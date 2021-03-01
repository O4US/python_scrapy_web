<template>
    <div class="container">
<br>
<div class="jumbotron" v-for="item in info" :key="item.id">
  <h1 class="display-6">{{item.name}}</h1>
  <p class="lead left" id='ltime'>{{item.add_time}}</p>
  <hr class="my-4">
  <p  v-html="item.content"></p>
  <!-- <router-link class="btn btn-primary btn-md" to="" role="button" @click="$router.back(-1)">返 回</router-link> -->
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
    if(this.$route.query.type==0){
      this.$https.get('getproductbyid/'+this.$route.query.id).then((res) => {this.info = res}).catch(err=>{console.log(err)})      
    }
    else if(this.$route.query.type==1){
      this.$https.get('getnewsbyid/'+this.$route.query.id).then((res) => {this.info = res}).catch(err=>{console.log(err)})   
    }
    else{
      
    }
  }
}
</script>

<style scoped>
.display-6{text-align: center;}
#ltime{text-align: right;}
</style>