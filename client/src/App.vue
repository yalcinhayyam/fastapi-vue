<template>
  <div>
    <input placeholder="Title" type="text" v-model="item.title" />
    <input placeholder="Value" type="number" v-model="item.value" />
    <input type="button" @click="post" value="Send" />
  </div>
  <ul>
    <li v-for="item in items">{{ item.title }} - {{ item.value }}</li>
  </ul>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      items: [],
      item: {
        title: "",
        value: 0,
      },
    };
  },
  methods: {
    clearFileds() {
      this.item = { title: "", value: 0 };
    },
    checkFields() {
      return this.item.title != "" && this.item.value != 0;
    },
    post() {
      if (!this.checkFields()) return alert("Please check fileds!");
      axios
        .post("http://127.0.0.1:8000", { ...this.item })
        .then((res) => (this.items = [...this.items, res.data.data.item]));
      this.clearFileds();
    },
  },
  watch: {
    items(newItems, oldItems) {
      console.log({ newItems, oldItems });
    },
  },
};
</script>
