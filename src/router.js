import {createWebHistory, createRouter} from 'vue-router'
import CrossNought from './components/CrossNought.vue'
import MainPage from "./components/MainPage.vue"
const routes = [
    {
        path:'/', 
        name:'MainPage', 
        component:MainPage

    }, 
    {
      path: '/cross-nought',
      name: 'CrossNought',
      component: CrossNought
    }
]

const router = createRouter({
    history:createWebHistory(), 
    routes, 
})

export default router