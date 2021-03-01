import Vue from 'vue'
import Router from 'vue-router'

import Home from '../pages/Home'
import Products from '../pages/Products'
import News from '../pages/News'
import About from '../pages/About'
import Detailslist from '../pages/Detailslist'
import Detail from '../pages/Detail'
import Registration from '../pages/Registration'

Vue.use(Router)

export default new Router({
  //mode:history,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/products',
      name: 'Products',
      component: Products
    },
    {
      path: '/news',
      name: 'News',
      component: News
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/detailslist',
      name: 'Detailslist',
      component: Detailslist
    },
    {
      path: '/detail',
      name: 'Detail',
      component: Detail
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration
    },
  ]
})
