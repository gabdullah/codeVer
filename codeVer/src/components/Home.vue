<template>
<div id = "container">
    <codeVerHeader></codeVerHeader>

<p>Enter the sample code below.</p>

<textarea id="codeSample" type="text" v-model="code" placeholder="Sample code here">
</textarea>
<br>
  <button @click="search()" id="textbox">Search</button>
  <br><br>
  <button @click="example()">Add sample code(for testing)</button>
</div>
</template>



<script>
import codeVerHeader from './codeVerHeader.vue'
export default {
  name: 'HelloWorld',

  data () {
    return {
      code: ''
    }
  },
  components:{
    codeVerHeader
  },

  methods: {
    split: function(code) {
      lines = code.split('\n')

      return lines
    },

    search: function() {

    } 
  }

}
</script>
