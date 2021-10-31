import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

// Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  {
    // home router to display org information
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    // input form page
    path: '/create',
    name: 'create',
    component: () => import('../components/CreateIndividualComponent')
  },
  {
    // graph router
    path: '/view',
    name: 'view',
    component: () => import('../components/ListLocationComponent')
  },
  {
    path: '/edit/:id',
    name: 'edit',
    component: () => import('../components/EditComponent')
  },
  {
    path: '/events/:id',
    name: 'events',
    component: () => import('../components/EventComponent')
  },
  {
    path: '/editEvents/:id',
    name: 'editEvents',
    component: () => import('../components/EditEventComponent')
  },
  {
    path: '/addEvent/:id',
    name: 'addEvent',
    component: () => import('../components/AddEventComponent')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/graph',
    name: 'graph',
    component: () => import('../components/GraphComponent')
  }
]

// Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes // short for `routes: routes`
})

export default router
