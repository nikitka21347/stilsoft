import Vue from 'vue';
import Router from 'vue-router';
import User from '@/components/User';
import Calendar from '@/components/Calendar';


import JwPagination from 'jw-vue-pagination';
Vue.component('jw-pagination', JwPagination);

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'User',
      component: User,
    },
    {
      path: 'calendar',
      name: 'Calendar',
      component: Calendar,
    },
  ],
  mode: 'history',
});