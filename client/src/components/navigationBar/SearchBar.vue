<template>
  <div class="search-bar">
    <input
        type="text"
        v-model="searchQuery"
        @keyup.enter="emitSearch"
        placeholder="Search movies..."
        class="search-input"
    />
  </div>
</template>

<script>

  export default {
    data() {
      return {
        searchQuery: ''
      }
    },
    methods: {
      emitSearch() {
        this.$emit("queryEmit", this.searchQuery);
        this.searchQuery = "";
      },
    }
  }
</script>

<style>
.search-bar {
  display: flex;
  justify-content: center;
}

.search-input {
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>