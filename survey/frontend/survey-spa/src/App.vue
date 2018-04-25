<template>
  <div id="app">
    <app-header></app-header>
    <router-view/>
  </div>
</template>

<script>
import AppHeader from "@/components/Header"; 
// 导入时可以定义名字
export default {
  name: "App",
  components: { AppHeader }
  //AppHeader会自动跟app-header绑定
};
</script>

<style lang="scss">
@import "~bulma/bulma";
</style>  
