## Vue_Flask
### main.js
程序主入口,用于注册vue实例和相关扩展.
### App.vue
顶级程序组件,用于包含程序总体布局.由3个部分组成:
1. <template>:html部分
2. <script>:部分vue对象和javascript的实现
3. <style>:影响整个程序所有的元素样式
### router/index.js
用于定义URL并映射到组件上
### Home.vues
主页的容器,展示所有survey的列表
### Survey.vue
survey的容器,展示每个survey的内容

------------------------
 v-for 迭代数组或对象
 v-bind:key 把变量作为迭代的关键字
 => (箭头函数):类似于匿名函数
 `surveys/${survey.id}` JavaScript模板字符串,注意是:`不是'
 ### $route与$router
 #### $route
1. $route.path
 字符串，对应当前路由的路径，总是解析为绝对路径，如 "/foo/bar"。
2. $route.params
 一个 key/value 对象，包含了 动态片段 和 全匹配片段，
 如果没有路由参数，就是一个空对象。
3. $route.query
 一个 key/value 对象，表示 URL 查询参数。
 例如，对于路径 /foo?user=1，则有 $route.query.user == 1，
 如果没有查询参数，则是个空对象。
4. $route.hash
 当前路由的 hash 值 (不带 #) ，如果没有 hash 值，则为空字符串。
5. $route.fullPath
 完成解析后的 URL，包含查询参数和 hash 的完整路径。
6. $route.matched
 数组，包含当前匹配的路径中所包含的所有片段所对应的配置参数对象。
7. $route.name    当前路径名字


#### $router
1. 字符串
this.$router.push('home')
2. 对象
this.$router.push({ path: 'home' })
3. 命名的路由
this.$router.push({ name: 'user', params: { userId: 123 }})
4. 带查询参数，变成 /register?plan=123
this.$router.push({ path: 'register', query: { plan: '123' }})

push方法其实和<router-link :to="...">是等同的。
注意：push方法的跳转会向 history 栈添加一个新的记录，当我们点击浏览器的返回按钮时可以看到之前的页面。

------------------------
### computed:({ [key: string]: Function | { get: Function, set: Function } })
将被混入到 Vue 实例中。所有 getter 和 setter 的 this 上下文自动地绑定为 Vue 实例。

### methods:({ [key: string]: Function })
将被混入到 Vue 实例中。可以直接通过 VM 实例访问这些方法，或者在指令表达式中使用。方法中的 this 自动绑定为 Vue 实例。

### watch:({ [key: string]: string | Function | Object | Array })
一个对象，键是需要观察的表达式，值是对应回调函数。值也可以是方法名，或者包含选项的对象。Vue 实例将会在实例化时调用 $watch()，遍历 watch 对象的每一个属性。

------------------------
### Vuex下的四个属性
state:单一状态树
getter:store的计算属性
mutation:更改store中的状态
action:与mutation类似,但是提交mutation,不是直接变更状态
