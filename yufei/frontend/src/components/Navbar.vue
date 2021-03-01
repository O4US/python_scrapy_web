<template>
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top ">
  <div class="container-xl">
    <router-link class="navbar-brand" to="/home">义乌市雨菲针织</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample07XL" aria-controls="navbarsExample07XL" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsExample07XL">
      <ul class="navbar-nav mr-auto">
          <li v-for="item in navList" v-bind:key="item.id" v-bind:class="[item.navclass,{active:item.isActive}]" @click="changeActive(item)"><!--导航栏激活状态改变-->
            <router-link class="nav-link" v-bind:to="item.link">{{item.text}}</router-link>
      </li>

        <!--
        <li class="nav-item dropdown">
          <router-link class="nav-link dropdown-toggle" to="#" id="dropdown07XL" data-toggle="dropdown" aria-expanded="false">Dropdown</router-link>
          <div class="dropdown-menu" aria-labelledby="dropdown07XL">
            <router-link class="dropdown-item" to="#">Action</router-link>
            <router-link class="dropdown-item" to="#">Another action</router-link>
            <router-link class="dropdown-item" to="#">Something else here</router-link>
          </div>
        </li>
        -->

      </ul>
      <!-- <form class="form-inline mt-2 mt-md-0">
        <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form> -->
      &nbsp;&nbsp;&nbsp;&nbsp;
      <router-link class="btn btn-md btn-primary" to="/registration" role="button">联系我们</router-link>
    </div>
  </div>
</nav>
</template>
  
<script>
export default {
  name: 'navbar',
  data () {
    return {
      navList: [
        {text: '首页',link:'/home',navclass:'nav-item', isActive: true},
        {text: '产品展示',link:'/products',navclass:'nav-item', isActive: false},
        {text: '新闻资讯',link:'/news',navclass:'nav-item', isActive: false},
        {text: '关于我们',link:'/about',navclass:'nav-item', isActive: false},
      ]
    }
  },
  methods: {
    
  /* changeActive: (data) => (console.log(this.navList))
  * 箭头函数的this指向为当前对象
  * */
    changeActive: function (data) {
      this.navList.forEach((obj) => (obj.isActive = false))
      data.isActive = !data.isActive
    },
  }
}
</script>
