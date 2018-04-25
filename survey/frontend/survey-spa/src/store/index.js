// scr/store/index.js

import Vue from 'vue'
import Vuex from 'vuex'

// 所有AJAX的方式可以写在下面
import { fetchSurveys, fetchSurvey, saveSurveyResponse, postNewSurvey } from '@/api'

Vue.use(Vuex)

const state = {
    // 访问和监视更变的数据
    surveys: [],
    currentSurvey: {}
}
const actions = {
    // 用于处理异步操作
    loadSurveys(context) {
        return fetchSurveys()
            .then((response) => context.commit('setSurveys', { surveys: response }))
    },
    loadSurvey(context, { id }) {
        return fetchSurvey(id)
            .then((response) => context.commit('setSurvey', { survey: response }))
    },
    addSurveyResponse(context) {
        return saveSurveyResponse(context.state.currentSurvey)
    },
    submitNewSurbey(context, survey) {
        return postNewSurvey(survey)
    }
}
const mutations = {
    // 数据提交时,更改应用的状态
    setSurveys(state, payload) {
        state.surveys = payload.surveys
    },
    setSurvey(state, payload) {
        const nQuestions = payload.survey.questions.length
        for (let i = 0; i < nQuestions; i++) {
            payload.survey.questions[i].choice = null
        }
        state.currentSurvey = payload.survey
    },
    setChoice(state, payload) {
        const { questionId, choice } = payload
        const nQuestions = state.currentSurvey.questions.length
        for (let i = 0; i < nQuestions; i++) {
            if (state.currentSurvey.questions[i].id === questionId) {
                state.currentSurvey.questions[i].choice = choice
                break
            }
        }
    }
}
const getters = {
    // 获取属性的值
}

const store = new Vuex.Store({
    state,
    actions,
    mutations,
    getters
})

export default store