<template>
  <div class="carousel-container">
    <h2 class="carousel-title">Movies tailored just for you</h2>
    <carousel :itemsToShow="5" :wrapAround="true" :centerMode="true" snapAlign="start" :navigationEnabled="true">
      <slide v-for="movie in moviesInfo" :key="movie.id">
        <a :href="movie.homepage" target="_blank" class="movie-card-link">
          <div class="movie-card">
            <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Poster">
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.overview }}</p>
            <a :href="movie.homepage" target="_blank" class="more-info">More Info</a>
          </div>
        </a>
      </slide>

      <template #addons>
        <Navigation />
      </template>
    </carousel>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import { Carousel, Slide, Navigation } from 'vue3-carousel';
import 'vue3-carousel/dist/carousel.css';
import axios from 'axios';
export default {
  components: {
    Carousel,
    Slide,
    Navigation
  },
  setup() {
    const moviesInfo = ref([]);

    onMounted(async () => {
      try {
        const response = await axios.get('http://localhost:5000/recommend?user_id=1');
        moviesInfo.value = response.data.movies_info;
        console.log(moviesInfo.value);
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    });

    return {
      moviesInfo
    };
  }
};
</script>

<style scoped>
.carousel-container {
  background-color: dark-gray;
  padding-top: 4rem;
  padding-bottom: 8rem;
}

.carousel{
  max-width: 80%;
  margin: 0 auto;
}

.movie-card {
  cursor: pointer;
  border-radius: 6px;
  overflow: hidden;
  transition: transform 0.3s ease-in-out;
  position: relative;
  max-widht: 300px;
  padding: 0;
}

.movie-card:hover {
  transform: translateY(-10px);
}

.movie-card img {
  width: 100%;
  height: auto;
  display: block;
}

.movie-card h3 {
  display: none;
}

.movie-card p {
  display: none;
}

.movie-card a {
  display: none;
}

.carousel-title {
  font-size: 1.5em;
  color: white;
  padding-left: 1em;
  padding-bottom: 1rem;
  display: flex;
  max-width: 80%;
  margin: 0 auto;
}

.carousel__icon {
  color: #1abc9c !important;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}

</style>
