import {createWebHistory, createRouter} from 'vue-router'
import RegisterView from "@/views/RegisterView.vue";
import LoginView from "@/views/LoginView.vue";
import MainView from "@/views/MainView.vue";
import CreateMelodyBattle from "@/views/createMelodyBattle.vue";
import createMelodyBattle from "@/views/createMelodyBattle.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/register',
            name: 'home',
            component: RegisterView
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/',
            name: 'index',
            component: MainView
        },
        {
            path: '/create-melody-battle',
            name: 'createMelodyBattle',
            component: createMelodyBattle
        }
    ]
})

export default router