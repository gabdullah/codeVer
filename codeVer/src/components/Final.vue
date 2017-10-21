<template>
  <div id = "container">
      <codeVerHeader></codeVerHeader>

  <h3>Possible Plagerised Projects</h3>
  <br>
  <p style="left:0px;">% of Similarity</p> <p style="right:0px;">Project</p>
    <br>

  </div>
</template>

<style>
p{
  font-size:20px;
  position:absolute;
  color:#EBEBEB;
}
h3{
  position:relative;
  font-size:30px;
  color:#EBEBEB;
}
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
