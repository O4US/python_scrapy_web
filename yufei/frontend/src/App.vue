<template>
  <div id="app">
    <header>
    <Navbar/>
    </header>
    <main role="main" class="mains">    
    <router-view/>
    </main>
    <footer class="blog-footer">
    <Footer/>   
    </footer>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Footer from './components/Footer'
export default {
  name: 'App',
  components:{
    Navbar,
    Footer,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.blog-footer {
  padding: 0.2cm 0;
  color: #999;
  background-color: #f9f9f9;
  /* border-top: 0.2cm solid #e5e5e5; */
}
</style>

