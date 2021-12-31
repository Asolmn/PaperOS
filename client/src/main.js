import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VueRouter from 'vue-router';
import axios from 'axios';
import App from './App.vue'

Vue.use(ElementUI);
Vue.use(VueRouter);


axios.defaults.baseURL = "http://127.0.0.1:5000";
Vue.prototype.$http = axios;

// 登录页面
import login from './components/login.vue';

// 学生管理
import index from './components/index.vue';
import stuinfo from './components/stuinfo.vue';
import stutopic from './components/stutopic.vue';
import stupaper from './components/stupaper.vue';

// 教师管理
import index2 from './components/index2.vue';
import teainfo from './components/teainfo.vue';
import teatopic from './components/teatopic.vue';
import teapaper from './components/teapaper.vue';


// 管理界面
import index3 from './components/index3.vue';
import admin from './components/admin.vue';




const router = new VueRouter({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      component: login
    },
    {
      path: '/index',
      component: index,
      children: [
        {
          path: '/stuinfo',
          component: stuinfo
        },
        {
          path: '/stutopic',
          component: stutopic
        },
        {
          path: '/stupaper',
          component: stupaper
        }
      ]
    },
    {
      path: '/index2',
      component: index2,
      children: [
        {
          path: '/teainfo',
          component: teainfo
        },
        {
          path: '/teatopic',
          component: teatopic
        },
        {
          path: '/teapaper',
          component: teapaper
        },
      ]
    },
    {
      path: '/index3',
      component: index3,
      children: [
        {
          path: '/admin',
          component: admin
        }
      ]
    }

  ]
})

Vue.config.productionTip = false

// 路由守卫
router.beforeEach((to, from, next)=>{
  if (to.path == '/login') return next();
  const id = window.sessionStorage.getItem('id');
  if (!id) return next('/login');
  next();
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
