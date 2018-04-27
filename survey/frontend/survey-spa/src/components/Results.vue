<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">实时投票数据</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div v-for="survey in surveys" :key="survey.id" class="my-5">
          <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
            <thead>
              <tr>
                <p class="title has-text-centered">{{ survey.name }}</p>
              </tr>
            </thead>
            <tbody v-for="(question) in survey.questions" :key="question.id">
              <tr>
                <th>{{ question.text }}</th>
                <th>count</th>
              </tr>
              <tr v-for="choice in question.choices" :key="choice.id">
                <th>{{ choice.text }}</th>
                <td>{{ choice.selected }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  computed: mapState({
    surveys: state => state.surveys
  }),
  beforeMount() {
    this.$store.dispatch("loadSurveys");
  }
};
</script>
<style>

</style>


