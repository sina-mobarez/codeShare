<template>
  <div id="editor-container">
    <div id="editor"></div>
  </div>
</template>

  <script>
import * as monaco from "monaco-editor";

export default {
  props: ["content"],
  data() {
    return {
      editor: null,
    };
  },
  mounted() {
    this.editor = monaco.editor.create(document.getElementById("editor"), {
      value: this.content,
      language: "javascript",
    });

    this.editor.onDidChangeModelContent((event) => {
      this.$emit("update-content", this.editor.getValue());
    });
  },
};
</script>

  <style scoped>
#editor-container {
  width: 100%;
  height: 500px;
}

#editor {
  width: 100%;
  height: 100%;
}
</style>
