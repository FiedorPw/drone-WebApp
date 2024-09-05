import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Gallery from "../views/Gallery.vue";
import Cockpit from "../views/Cockpit.vue";
import Contact from "../views/Contact.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: Dashboard,
    },
    {
      path: "/gallery",
      component: Gallery,
    },
    {
      path: "/cockpit",
      component: Cockpit,
    },
    {
      path: "/contact",
      component: Contact,
    },
  ],
});

export default router;
