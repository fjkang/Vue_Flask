## 使用前端(vue.js+bootst)+跨域代理(axios)+后端(flask-restful)+数据库(Mongodb)
### vue:
1. vuex:
+ state->存储数据状态
+ actions->组件中通过dispatch激活的方法
+ mutations->action通过commit提交对state进行更改的方法
2. vue-router:
+ this.$router.push():改变<router-view/>中显示的内容,达到页面跳转的效果

### bootstrap:
+ bootstrap的安装和引用

### axios:
+ 使用axios的get\post\put\delete方法,获取后台api放回的数据

### flask:
1. CROS:打开/api路径下跨域请求的限制
2. PyMongo:与mango数据库通信的模块
3. RESTful:定义get\post\put\delete获取Resource的逻辑

### Mongodb:
+ 文档型数据库,与json基本无缝的转换,让数据的流转更顺畅

==========================
## 笔记:
### 链接mongo数据库代码
~~~bash
mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
MONGO_URI='mongodb://localhost:27017/Computers'
~~~
+ 使用mongo.db调用mongo集合的操作时,要在使用时调用.
~~~bash
RuntimeError: Working outside of application context.
~~~
如果提前初始化,会报以上错误!


### 在vue项目中引用bootstrap包
+ 先用npm安装jquery popper.js bootstrap包
~~~bash
npm install --save jquery popper.js bootstrap
~~~
+ 在main.js中import
~~~js
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
~~~

### 在前端使用axios获取后端的数据
#### 前端操作
+ 先用npm安装axios
~~~bash
npm install --save axios
~~~
+ 在组件中导入axios
~~~js
import axios from 'axios'
~~~
+ 然后把数据获取过来(这是本程序中对应的url和对用的data变量)
~~~js
axios
    .get('http://127.0.0.1:5000/api/computers')
    .then(response => (this.computers = response.data.computers))
~~~
#### 后端操作
+ 安装flask-cors扩展
~~~bash
pip install flask-cors
~~~
+ 然后在flask实例中添加cors设置
~~~python
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
~~~

### vue-router
~~~js
this.$router.push(`/`)
~~~
 里面要用``而不能用''
