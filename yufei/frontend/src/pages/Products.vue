<template>
    <!-- <div id="app">
  <p v-for="item in info" :key="item.id">{{item.name}}</p>
</div> -->
<div class="album py-5 bg-light">
    <div class="container">
      <div class="row">

        <div class="col-md-4" v-for="item in info" :key="item.id">
          <div class="card mb-4 shadow-sm" @click="clto(item.id)">
            <img :src="item.thumbnail" class="card-img-top " alt="...">
            <div class="card-body">
              <h5 class="card-title">{{item.name}}</h5>
              <p class="card-text">{{item.text}}</p>
              <div class="d-flex justify-content-between align-items-center">
                <!-- <small class="text-muted">9 mins</small> -->
              </div>
            </div>
          </div>
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
    this.$https.get('getallproductstype').then((res) => {this.info = res}).catch(err=>{console.log(err)});
  },
  methods:{
    clto:function(data){
      this.$router.push({ path: '/detailslist', query: { type:0,typeid:data }})
    }
  } 
}
</script>