<template>
  <div>
    <div class="container">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">编号</th>
            <th scope="col">部门</th>
            <th scope="col">使用人</th>
            <th scope="col">类型</th>
            <th scope="col">处理器</th>
            <th scope="col">内存</th>
            <th scope="col">购买日期</th>
            <th scope="col">价格</th>
            <th scope="col">曾用人</th>
            <th scope="col">操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(computer, index) in computers" :key="index">
            <th scope="row">{{index+1}}</th>
            <td v-for="(data, field) in computer" :key="field">
              {{data}}
            </td>
            <td>
              <button type="button" class="btn btn-info" @click="updateComputerBtn(computer.id)">修改</button>
              <button type="button" class="btn btn-danger" @click="removeComputerBtn(computer.id)">删除</button>
            </td>
          </tr>
          <tr>
            <button type="button" class="btn btn-success" @click="addComputerBtn()">添加</button>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import {
    mapState
  } from "vuex"
  export default {
    computed: mapState({
      'computers': state => state.computers
    }),
    beforeMount() {
      this.$store.dispatch('loadComputers')
    },
    methods: {
      removeComputerBtn(computerid) {
        this.$store.dispatch('removeComputer', {
          computerid: computerid
        })
      },
      updateComputerBtn(computerid) {
        this.$store.dispatch('editComputer', {
          computerid: computerid
        }).then(() => {
          this.$router.push(`/${computerid}`)
        })
      },
      addComputerBtn() {
        this.$router.push(`/add`)
      }
    }


  }

</script>

<style>


</style>
