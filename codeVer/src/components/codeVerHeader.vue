<template>
  <div id="heading">
    <router-link to="/" class="routerLink">
      <img src="../assets/codeVerLogo.png"/>
      <h1>codeVer</h1>
      <h2>Your premium code verification software.</h2>
    </router-link>
  </div>
</template>

<style>
  .routerLink{
    color:white;
  }
#heading{
  width: 100%;
  margin-top: 0px;
  padding:0px;
  height: 200px;
  background: #b1e5f2;
  color: black;
  position: relative;
}
img{
  position: absolute;
  right:0px;
  padding: 20px;
  height: 256px;
  width: 256px;
}
h1{
  color: #a6a6a8;
  position: absolute;
  font-size: 90px;
  bottom: 50px;
  padding-top: 10px;
  padding-bottom: 30px;
  margin: 0px;
    transition-duration: 3s;
}
  h1:hover{
    letter-spacing: 10px;
    color: #272635;
  }
h2{
  position: absolute;
  color: #52489C;
  bottom: 0px;
  left: 5px;
  font-size: 50px;
  font-style: italic;
  margin: 0px;
  padding-bottom: 25px;
    transition-duration: 2s;
}
  h2:hover{
    color: #272635;
  }

</style>
