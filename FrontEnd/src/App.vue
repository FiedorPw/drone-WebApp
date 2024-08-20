<template>
  <div class="app">
    <!-- SIDEBAR -->
    <Sidebar />
    <!-- To co widzi router -->
    <router-view />
  </div>
</template>

<script setup>
import Sidebar from "./components/Sidebar.vue";
</script>

<style lang="scss">
:root {
  /* Paleta kolorów wykorzystana na stronie */
  --primary: #4ade80;
  --dark-alt: #334155;
  --grey: #64748b;
  --light: #f1f5f9;
  --dark: #1e293b;
  --background: #1c2430;

  --sidebar-width: 200px;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  /* Ustawienie linkowanej czcionki*/
  font-family: "Fira sans", sans-serif;
  //
}

body {
  overflow: hidden;
}

button {
  cursor: pointer;
  appearance: none;
  border: none;
  outline: none;
  background: none;
}

.app {
  display: flex;
}

main {
  flex: 1 1 0;
  padding: 2rem;

  @media (max-width: 768px) {
    padding-left: 6rem;
  }
}
</style>
