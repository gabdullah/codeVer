<template>
<!--<head>
  <title>codeVer - Code Authenticator</title>
</head>-->

<div id = "container">
    <codeVerHeader></codeVerHeader>

<p style="position:relative;color:#EBEBEB; align:center;">Enter the sample code below.</p>

<textarea id="codeSample" type="text" v-model="code" placeholder="Sample code here">
</textarea>
<br>
  <button @click="search()">Search</button>
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

}
</script>
