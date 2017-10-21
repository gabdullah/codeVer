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
    splitter: function(code) {
      console.log('split called');
      var lines = code.split('\n');
      //console.log(lines[0]);

      return lines
    },

    search: function() {
      /*var GitHubApi = require("node-github");
      var github = new GitHubApi({version: "3.0.0"});*/

      console.log('search called');
      var code = document.getElementById('textbox').value;
      var lines = this.splitter(this.code);
      var counter = 0;
      //console.log(lines.length);

      while (counter < lines.length){
        console.log("text: " + lines[counter]);
        counter++;
      }
      //console.log(lines[0]);
    } 
  }

}
</script>
