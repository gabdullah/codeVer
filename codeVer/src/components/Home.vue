<template>
<div id = "container">
    <codeVerHeader></codeVerHeader>

<p style="color:#EBEBEB;">Enter the sample code below.</p>

<textarea id="codeSample" type="text" v-model="code" placeholder="Sample code here">
</textarea>
<br>
  <button @click="search()" id="textbox">Search</button>
  <br><br>
  <button @click="example()">Add sample code(for testing)</button>
</div>
</template>

<style>
  #container{
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    height: 100%;
    width: 100%;
    text-align: center;
    justify-content: center;
    flex-flow: column;
    background: #2f4f4f;
  }
  textarea{
    height: 300px;
    width: 600px;
    color: #F45B69;
  }
</style>

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
