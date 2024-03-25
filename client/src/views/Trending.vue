<template>
  <div class="trending">
    <h1>Trending Movies</h1>
<!--    <MovieList :movies="trendingMovies" title="What's Trending" />-->
  </div>
</template>

<script>
// import MovieList from '@/components/MovieList.vue';

export default {
  name: 'TrendingPage',
  // components: {
  //   MovieList
  // },
  data() {
    return {
      trendingMovies: [] // This would be fetched from the backend API
    };
  },
  mounted() {
    this.fetchTrendingMovies();
  },
  methods: {
    fetchTrendingMovies() {
      // Similar to the HomePage, make an API call to fetch trending movies
      // axios.get('/api/movies/trending')
      //     .then(response => this.trendingMovies = response.data)
      //     .catch(error => console.error(error));
    }
  }
};
</script>

<style>
.trending {
  padding: 20px;
}
</style>