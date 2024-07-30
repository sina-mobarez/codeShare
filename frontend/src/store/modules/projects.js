import axios from "@/plugins/axios";

const state = {
  projects: [],
};

const getters = {
  allProjects: (state) => state.projects,
};

const actions = {
  async fetchProjects({ commit }) {
    const response = await axios.get("projects/");
    commit("setProjects", response.data);
  },
  async addProject({ commit }, project) {
    const response = await axios.post("projects/", project);
    commit("newProject", response.data);
  },
  async deleteProject({ commit }, id) {
    await axios.delete(`projects/${id}`);
    commit("removeProject", id);
  },
};

const mutations = {
  setProjects: (state, projects) => (state.projects = projects),
  newProject: (state, project) => state.projects.push(project),
  removeProject: (state, id) =>
    (state.projects = state.projects.filter((project) => project.id !== id)),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
