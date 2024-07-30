<template>
  <div>
    <Editor :content="initialContent" @update-content="handleUpdateContent" />
  </div>
</template>

  <script>
import Editor from "@/components/Editor.vue";
import { mapState } from "vuex";

export default {
  components: {
    Editor,
  },
  data() {
    return {
      initialContent: "",
      socket: null,
    };
  },
  computed: {
    ...mapState({
      session: (state) => state.session,
    }),
  },
  methods: {
    handleUpdateContent(content) {
      // Send updated content to WebSocket
      this.socket.send(
        JSON.stringify({
          message: content,
        })
      );
    },
  },
  mounted() {
    // Initialize WebSocket connection
    this.socket = new WebSocket(
      `ws://${window.location.host}/ws/editor/${this.$route.params.id}/`
    );

    this.socket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      this.initialContent = data.message;
    };

    this.socket.onclose = (e) => {
      console.error("Socket closed unexpectedly");
    };
  },
};
</script>
