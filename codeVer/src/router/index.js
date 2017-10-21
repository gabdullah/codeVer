import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Final from '@/components/Final'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Home
    },
    {
      path: '/Final',
      name: 'Goodbye',
      component: Final
    }
  ]
})
