<template>
  <div class="featured-movie-container" v-if="featuredMovie">
    <div class="featured-movie-content">
      <div class="featured-movie-content">
        <h2 class="featured-movie-title">{{ featuredMovie.title }}</h2>
        <div class="featured-movie-info">
          <span class="featured-movie-year">{{ featuredMovie.releaseDate }}</span>
          <span class="featured-movie-rating">{{ featuredMovie.rating }}</span>
        </div>
        <p class="featured-movie-description">{{ featuredMovie.overview }}</p>
        <div class="featured-movie-actions">
          <button class="btn btn-red">
            <a :href="featuredMovie.homepage" target="_blank">
              Go to movie page
            </a>
          </button>
        </div>
      </div>
    </div>
    <div class="featured-movie-image">
      <img :src="`https://image.tmdb.org/t/p/original${featuredMovie.backdrop_path}`" alt="Movie Poster" />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const featuredMovie = ref(null);

    onMounted(async () => {
      try {
        const response = await axios.get('http://localhost:5000/recommend?user_id=1');
        featuredMovie.value = response.data.movies_info[0];
        console.log(featuredMovie.value);
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    });

    const backgroundImageStyle = (movie) => {
      return {
        backgroundImage: `url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center center'
      };
    };

    return {
      featuredMovie,
      backgroundImageStyle
    };
  }
};
</script>

<style scoped>
.featured-movie-container {
  display: flex;
  align-items: center;
  justify-content: end;
  margin-top: 2rem;
  margin-left: 15rem;
  width: 90%;
}

.featured-movie {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: end;
  justify-content: end;
  padding: 2em;
  overflow: hidden;
}

.featured-movie-content {
  color: white;
  text-align: left;
  max-width: 640px;
}

.featured-movie-title {
  font-size: 4rem;
  font-weight: 900;
  margin-bottom: 1rem;
}

.featured-movie-info {
  margin-bottom: 1rem;
}

.featured-movie-year,
.featured-movie-rating,
.featured-movie-seasons {
  margin-right: 1rem;
}

.featured-movie-description {
  margin-bottom: 2rem;
  font-size: 1rem;
}

.btn {
  padding: 10px 25px;
  margin: 0.5rem;
  font-weight: bold;
  text-transform: uppercase;
  border: 0.7px solid white;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  color: #fff;
  background-color: black;
}

a {
  text-decoration: none;
  color: #fff;
}

.btn-red {
  background-color: #1abc9c;
  box-shadow: 0 0 10px #1abc9c, 0 0 10px #1abc9c;
  border: none;
}

.btn-play {
  background-color: #181818;
  border: 1px solid #fff;
}

.btn-red:hover, .btn-play:hover {
  box-shadow: 0 0 5px #fff, 0 0 5px #fff;
  transform: scale(1.01);
}

.btn-red:active, .btn-play:active {
  transform: scale(0.99);
}

.featured-movie-image {
  width: 70%;
  height: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 50px 50px black inset;
  z-index: 1;
}

.featured-movie-image::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  background:
      linear-gradient(to top, transparent 30%, #000 90%),
      linear-gradient(to left, transparent 30%, #000 90%),
      linear-gradient(to right, transparent 30%, #000 90%),
      linear-gradient(to bottom, transparent 30%, #000 90%);
  background-repeat: no-repeat;
  background-position: top, left, right, bottom;
  background-size: 100% 90px, 90px 100%, 90px 100%, 100% 90px;
}

.featured-movie-image img {
  max-width: 100%;
  max-height: 100%;
  width: 100%;
  height: 100%;
  object-fit: contain;
}

</style>
