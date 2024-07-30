<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
    </nav>
    <router-view />
  </div>
</template>

  <script>
export default {
  name: "App",
};
</script>

  <style>
/* Add some basic styling */
body {
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  text-align: center;
}

nav {
  background-color: #42b983;
  padding: 1em;
}

nav a {
  color: white;
  margin: 0 1em;
  text-decoration: none;
}

nav a.router-link-active {
  font-weight: bold;
}
</style>
