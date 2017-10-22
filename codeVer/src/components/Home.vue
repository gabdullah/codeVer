<template>
<!--<head>
  <title>codeVer - Code Authenticator</title>
</head>-->

<div id = "container">
    <codeVerHeader></codeVerHeader>

<p style="position:relative;color:#EBEBEB; align:center; font-size:30px;">Enter the sample code below</p>

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
  button{
    background-color: #a6a6a8;
    border: none;
    color: white;
    padding: 15px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
  }
  textarea{
    height: 225px;
    width: 1000px;
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
      return lines
    },

    search: function() {
       /*const concat = require("concat-stream");
       const FormData = require('form-data');
       const fd = new FormData();
       const fs = require('fs');

      fd.append("-u", fs.createReadStream("gabdullah"));
       fd.pipe(concat({encoding: 'buffer'}, data => {
         axios.post("https://api.github.com", data)
       }));*/

      //var curl = require('curlrequest');
       //var github = require('octonode');






      console.log('search called');
       var code = document.getElementById('textbox').value;
       this.$root.inputStrings = this.splitter(this.code);
       //for (var i = 0; i < 15; i++)
          //console.log(this.$root.inputStrings.pop());
       var counter = 0;

      //while (counter < lines.length){
       //  console.log("text: " + lines[counter]);
       //  counter++;
       //}

     /* return axios.post('https://api.github.com/user', {
         header: 'Accept: application/vnd.github.v3+json',
         username: 'gabdullah'
       })*/

      /*var gh = new Github({
         username: 'collinw9898',
         password: 'Cw122198!'
       });

      var me = gh.getUser();

      var code = "for (int i = 0; i < 10; i++)";
     console.log(gh.search({q: code}));

      var posts;
       var errors = [];
       return axios.get('https://api.github.com/users/gabdullah/repos')
       .then(response => {
         //var data = response.data
         //var meta = response.meta;
         //console.log(response.data)
         //console.log(response.meta);
       })
      // .catch(e => {
        // errors.push(e)
         //console.log(errors.pop())
       })

      //while (counter < posts.length){
       //  counsole.log(counter + posts[counter]);
       //  counter++;
       //}
       */
      this.$router.push('/final');
    },

   example: function() {
     console.log("example() invoked");
     this.code = "//This is a sample of our code\n<template>\n        <div id=\"heading\">\n          <router-link to=\"/\" class=\"routerLink\">\n            <img src=\"../assets/sineWave.png\" class=\"sine\"/>\n            <img src=\"../assets/flipSineWave.png\" class=\"cosine\"/>\n            <img src=\"../assets/block.png\" class=\"block\"/>\n            <img src=\"../assets/codeVerLogo.png\" class=\"logo\"/>\n            <h1>codeVer</h1>\n            <h2>Your premium code verification software.</h2>\n          </router-link>\n        </div>\n      </template>";
   }
}
}
</script>
