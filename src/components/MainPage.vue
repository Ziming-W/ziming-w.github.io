<template>
    <div>
      <h1>Welcome to my portfolio</h1>
      <p>Click here to play cross-nought</p>
      <button @click="$router.push('/cross-nought')">cross-nought</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MainPage'
  }
  </script>