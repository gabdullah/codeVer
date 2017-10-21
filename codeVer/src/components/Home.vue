<template>
<div id = "container">
    <codeVerHeader></codeVerHeader>

<p>Enter the sample code below.</p>

<textarea id="codeSample" type="text" v-model="code" placeholder="Sample code here">
</textarea>
<br>
  <button @click="search()">Search</button>
  <br><br>
  <button @click="example()">Add sample code(for testing)</button>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    split: function() {
      
    }

    search: function() {

    }
  }

}
</script>