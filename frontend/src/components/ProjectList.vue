<template>
  <div>
    <ul>
      <li v-for="project in projects" :key="project.id">
        <router-link :to="'/project/' + project.id">{{
          project.name
        }}</router-link>
      </li>
    </ul>
  </div>
</template>

  <script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["allProjects"]),
  },
  mounted() {
    this.$store.dispatch("fetchProjects");
  },
};
</script>
