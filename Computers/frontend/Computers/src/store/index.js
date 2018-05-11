import Vue from 'vue'
import Vuex from 'vuex'

import {
  getComputers,
  getComputer,
  deleteComputer,
  putComputer,
  postComputer
} from '@/api'

Vue.use(Vuex)

const state = {
  computers: [],
  computer: {},
  computerid: ""
}

const actions = {
  loadComputers(context) {
    return getComputers()
      .then(response => {
        context.commit('setComputers', {
          computers: response.data.computers
        })
      })
  },
  loadComputer(context, {
    computerid
  }) {
    return getComputer(computerid)
      .then(response => {
        context.commit('setComputer', {
          computer: response.data.computer
        })
      })
  },
  removeComputer(context, {
    computerid
  }) {
    deleteComputer(computerid)
      .then(response => {
        alert(response.data.msg)
        if (response) {
          getComputers()
            .then(response => {
              context.commit('setComputers', {
                computers: response.data.computers
              })
            })
        }
      })
  },
  editComputer(context, {
    computerid
  }) {
    context.commit('setComputerId', {
      computerid
    })
  },
  updateComputer(context, {
    computerid,
    computer
  }) {
    return putComputer(computerid, computer)
      .then(response => {
        alert(response.data.msg)
      })
  },
  addComputer(context, {
    computer
  }) {
    return postComputer(computer)
      .then(response => {
        alert(response.data.msg)
      })
  }
}

const mutations = {
  setComputers(state, playload) {
    state.computers = playload.computers
  },
  setComputer(state, playload) {
    state.computer = playload.computer
  },
  setComputerId(state, playload) {
    state.computerid = playload.computerid
  }
}

const getters = {

}

const store = new Vuex.Store({
  state: state,
  actions: actions,
  mutations: mutations,
  getters: getters
})

export default store
