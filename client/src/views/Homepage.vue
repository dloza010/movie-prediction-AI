<template>
  <div class="home">
    <h1>Welcome to MyMovieApp</h1>
    <MovieList :movies="popularMovies" title="Popular Movies" />
  </div>
</template>

<script>
// import MovieList from '@/components/MovieList.vue';

export default {
  name: 'HomePage',
  // components: {
  //   MovieList
  // },
  data() {
    return {
      popularMovies: [] // This would be fetched from the backend API
    };
  },
  mounted() {
    this.fetchPopularMovies();
  },
  methods: {
    fetchPopularMovies() {
      // Here you would make an API call to your backend to fetch the popular movies
      // For example:
      // axios.get('/api/movies/popular')
      //     .then(response => this.popularMovies = response.data)
      //     .catch(error => console.error(error));
    }
  }
};
</script>

<style>
.home {
  padding: 20px;
}
</style>