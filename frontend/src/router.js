import Home from "@/views/Home.vue";
import Project from "@/views/Project.vue";
import Session from "@/views/Session.vue";
import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/project/:id",
    name: "Project",
    component: Project,
  },
  {
    path: "/session/:id",
    name: "Session",
    component: Session,
  },
];

export default new Router({
  mode: "history",
  routes,
});
