<template>
  <div class="home">
    <FeaturedMovie />
    <MovieCarousel />
  </div>
</template>

<script>
import FeaturedMovie from "../components/movies/FeaturedMovie.vue";
import MovieCarousel from "../components/movies/MovieCarousel.vue";
export default {
  name: 'HomePage',
  components: {
    FeaturedMovie,
    MovieCarousel
  }
}
</script>

<style>

.movie-slider {
  max-width: 1200px;
  margin: auto;
}

.movie-card {
  margin: 10px;
  padding: 20px;
  background: #f0f0f0;
  border-radius: 8px;
}

.movie-poster {
  width: 100%;
  height: auto;
  border-radius: 4px;
}

.tagline {
  font-style: italic;
}
</style>