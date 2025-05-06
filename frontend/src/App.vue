<script setup>
</script>

<template>
  <header class="header grid">
    <div class="brand h-full flex flex-row gap-2 items-center">
      <img src="./assets/logo.svg" alt="Logo" class="brand-logo"/>
      <span class="brand-name h6">Apartment Rental Service</span>
    </div>
  </header>
  <main class="main">
    <router-view/>
  </main>
  <footer class="footer">
  </footer>
</template>
