import Vue from 'vue'
import Router from 'vue-router'
import ComputerList from '@/components/ComputerList'
import UpdateComputer from '@/components/UpdateComputer'
import AddComputer from '@/components/AddComputer'


Vue.use(Router)

export default new Router({
  // mode:'history',
  routes: [
    {
      path: '/',
      name: 'ComputerList',
      component: ComputerList
    },
    {
      path: '/add',
      name: 'AddComputer',
      component: AddComputer
    },
    {
      path: '/:id',
      name: 'UpdateComputer',
      component: UpdateComputer
    }
    
  ]
})
