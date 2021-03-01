<template>
<div class="container">
<ul class="list-unstyled">
  <div v-for="item in info" :key="item.id">
  <hr>
  <li class="media" @click="clto(item.id)">
    <img :src="item.thumbnail" class="mr-3 img-thumbnail" alt="...">
    <div class="media-body">
      <h5 class="mt-0 mb-1">{{item.name}}</h5>
      <p>{{item.text}}</p>
      <small class="text-muted">{{item.add_time}}</small>      
    </div>
  </li>
</div>

</ul>
    </div>
</template>

<script>
export default {
  data () {
    return {
      info: [],
    }
  },
  mounted () {
    if(this.$route.query.type==0){
      this.$https.get('getproductslistbytype/'+this.$route.query.typeid).then((res) => {this.info = res}).catch(err=>{console.log(err)})     
    }
    else if(this.$route.query.type==1){
      this.$https.get('getnewslistbytype/'+this.$route.query.typeid).then((res) => {this.info = res}).catch(err=>{console.log(err)})  
    }
    else{

    }
  },
  methods:{    
    clto:function(data){
      this.$router.push({ path: '/detail', query: { type:this.$route.query.type,id:data }})
    }
  }   
}
</script>