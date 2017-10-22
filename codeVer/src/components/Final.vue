<template>
  <div id = "container">
      <codeVerHeader></codeVerHeader>

      <h3>Projects of Interest</h3>

      <table>
        <tr><td class="percent">% Similar</td> <td class="project">Project</td></tr>
        <tr><td colspan="2"><hr></hr></td></tr>
        <tr><td class="percent">% Placeholder</td><td class="project">Project Placeholder</td></tr><br>
        <tr><td class="percent">% Placeholder</td><td class="project">Project Placeholder</td></tr><br>
        <tr><td class="percent">% Placeholder</td><td class="project">Project Placeholder</td></tr><br>
        <tr><td class="percent">% Placeholder</td><td class="project">Project Placeholder</td></tr><br>
        <tr><td class="percent">% Placeholder</td><td class="project">Project Placeholder</td></tr><br>
      </table>

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
.percent{
  text-align: left;
}
.project{
  text-align: right;
}
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
table{
  position: absolute;
  margin-left: 17%;
  margin-right: 23%;
  width: 60%;
}
tr{
  color:white;
  font-size:20px;
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
