<template>
  <NavigationBar></NavigationBar>
  <router-view></router-view>
</template>

<script>
import NavigationBar from "@/components/navigationBar/NavigationBar.vue";

export default {
  name: 'App',
  components: {
    NavigationBar,
  }
}
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
