// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  data(){
  	return{
  		inputStrings: [],
  		dirtyStrings: [0, 0, 0, 0, 0],
  		percentage: [1.0, 1.0, 1.0, 1.0, 1.0]
  	}
  },
  router,
  template: '<App/>',
  components: { App }
})
