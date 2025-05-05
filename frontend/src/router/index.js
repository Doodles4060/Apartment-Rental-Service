import { createRouter, createWebHistory } from 'vue-router'
import ApartmentList from '../components/ApartmentList.vue'
import ApartmentDetail from '../components/ApartmentDetail.vue'
// import Login from '../components/Login.vue'

const routes = [
    { path: '/', name: 'Home', component: ApartmentList },
    { path: '/apartment/:slug', name: 'ApartmentDetail', component: ApartmentDetail },
    // { path: '/login', name: 'Login', component: Login }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router