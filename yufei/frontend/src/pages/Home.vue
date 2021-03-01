<template>
  <div>
  <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" v-for="(item,i) in info" v-bind:key="item.id" v-bind:data-slide-to="i+1"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="/static/media/upimages/products/default(2).jpg" class="d-block w-100" alt="...">
      <div class="container">
          <div class="carousel-caption text-center">
            <h1> 因 为 专 业 , 所 以 出 色 </h1>
            <p>十年来我们一直用心做品质</p>
          </div>
        </div>
    </div>
    <div class="carousel-item" v-for="item in info" v-bind:key="item.id">
      <img v-bind:src="item.imgurl" class="d-block w-100" alt="...">
      <div class="container">
          <div class="carousel-caption text-center">
            <h1>{{item.name}}</h1>
            <p>{{item.text}}</p>
            <!-- <p><router-link class="btn btn-lg btn-primary" to="#" role="button">查看</router-link></p> -->
          </div>
        </div>
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">上一张</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">下一张</span>
  </a>
</div>
    <!-- Main jumbotron for a primary marketing message or call to action -->
  <div class="jumbotron">
    <div class="container">
      <h1 class="display-3">欢迎,光临!</h1>
      <p>织造染整</p>
      <p><router-link class="btn btn-primary btn-lg" to="/registration" role="button">联 系 我 们 &raquo;</router-link></p>
    </div>
  </div>

  <div class="container">
    <!-- Example row of columns -->
    <div class="row">
      <div class="col-md-4">
        <h2>Heading</h2>
        <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
        <p><router-link class="btn btn-secondary" to="#" role="button">View details &raquo;</router-link></p>
      </div>
      <div class="col-md-4">
        <h2>Heading</h2>
        <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
        <p><router-link class="btn btn-secondary" to="#" role="button">View details &raquo;</router-link></p>
      </div>
      <div class="col-md-4">
        <h2>Heading</h2>
        <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        <p><router-link class="btn btn-secondary" to="#" role="button">View details &raquo;</router-link></p>
      </div>
    </div>
  </div> <!-- /container -->
  </div>
</template>

<script>
export default {
  name:'home',
  data(){
    return {
      info:[]
    }
  },
  mounted () {
    this.$https.get('getallimglist').then((res) => {this.info = res}).catch(err=>{console.log(err)});
  },
}
</script>