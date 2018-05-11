<template>
  <div>
    <div class="text-center">
      <h2>修改电脑信息</h2>
    </div>
    <div class="container">
      <form>
        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">编号</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.id" id="id">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">部门</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.department" id="department">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">使用人</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.user" id="user">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">类型</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.type" id="type">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">处理器</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.cpu" id="cpu">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">内存</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.memory" id="memory">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">购买日期</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.buydate" id="buydate">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">价格</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.price" id="price">
          </div>
        </div>

        <div class="form-group">
          <div class="input-group mb-2">
            <div class="input-group-prepend">
              <span class="input-group-text">曾用人</span>
            </div>
            <input type="text" class="form-control" v-model.lazy="computer.used" id="used">
          </div>
        </div>

        <button type="submit" class="btn btn-primary" @click="addComputerBtn()">提交</button>
        <button class="btn btn-dark" @click="backIndex()">返回</button>
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        computer: {}
      }
    },
    methods: {
      addComputerBtn() {
        this.$store.dispatch('addComputer', {
            computer: this.computer
          })
          .then(() => {
            this.$router.push(`/`)
          })
      },
      backIndex() {
        this.$router.push(`/`)
      }
    }
  }

</script>

<style>


</style>
