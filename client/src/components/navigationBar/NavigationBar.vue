<template>
  <nav class="navigationBar">
    <div class="navigationBar-container">
      <div class="logo-container">
        <img :src="logoSvg" alt="Logo" class="logo-svg" />
      </div>
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><SearchBar @queryEmit="fetchMovies" /></li>
        <li><router-link to="/trending">Trending</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script>
import axios from 'axios';
import SearchBar from './SearchBar.vue';
import LogoSvg from '@/assets/logo.svg';

export default {
  components: {
    SearchBar
  },
  data() {
    return {
      logoSvg: LogoSvg
    }
  },
  methods: {
    async fetchMovies(searchTerm) {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/movies', {params: {query: searchTerm}});
        console.log(response)
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    }
  }
}
</script>

<style>
.navigationBar {
  background-color: #2c3e50;
  color: white;
  padding: 1rem;
  box-shadow: 0 0px 12px 0 #2c3e50;
}

.navigationBar-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo-container {
  position: absolute;
  left: 2.5rem;
}

.logo-svg {
  width: 65px;
  height: auto;
}

.nav-links {
  list-style-type: none;
  display: flex;
  align-items: center;
  padding: 0;
  margin: 0;
  gap: 1rem;
}

.nav-links li {
  padding: 0.5rem 1rem;
}

.router-link-active, .nav-links a {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.nav-links a:hover, .router-link-active {
  color: #1abc9c;
  border-bottom: 2px solid #1abc9c;
}
</style>