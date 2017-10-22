<template>
  <div id="heading">
    <router-link to="/" class="routerLink">
      <img src="../assets/sineWave.png" class="sine"/>
      <img src="../assets/flipSineWave.png" class="cosine"/>
      <img src="../assets/block.png" class="block"/>
      <img src="../assets/codeVerLogo.png" class="logo"/>
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
  height: 175px;
  background: #b1e5f2;
  color: black;
  position: relative;
}
img{
  position: absolute;
}
.sine{
  filter: opacity(35%);
  height:100%;
  width:100%;
  z-index: 0;
  left:0px;
}
.cosine{
  filter: opacity(35%);
  top: 5px;
  height:100%;
  width:100%;
  z-index: 0;
  left: 0%;
}
.block{
  height:100%;
  width:100%;
  z-index:-1;
  left:0%;
  animation-name: slide;
  animation-duration: 5s;
}
@keyframes slide {
  from{left:0%; z-index:0;}
  to{left: 100%;z-index:0;}
}
.logo{
  right:0px;
  padding: 30px;
  height: 256px;
  width: 256px;
  z-index: 2;
}
h1{
  font-family: Georgia, serif;
  color: #708090;
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
  color: #a6a6a8;
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
