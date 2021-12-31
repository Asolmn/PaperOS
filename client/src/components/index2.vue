<!--教师主界面-->
<template>
  <el-container class="home_container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <span>论文管理系统</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <el-divider></el-divider>
    <!-- 页面主体区域 -->
    <el-container>
      <!-- 左边侧边栏 -->
      <el-aside width="200px">
        <el-menu>
          
          <router-link to='/teainfo'>
            <el-menu-item>
              <template slot="title">
                <i class="el-icon-s-custom"></i>
                <span>用户信息</span>
              </template>
            </el-menu-item>
          </router-link>

          <router-link to="/teatopic">
            <el-menu-item>
              <template slot="title">
                <i class="el-icon-s-check"></i>
                <span>课题审核</span>
              </template>
            </el-menu-item>
          </router-link>

          <router-link to="/teapaper">
            <el-menu-item>
              <template slot="title">
                <i class="el-icon-s-goods"></i>
                <span>论文批阅</span>
              </template>
            </el-menu-item>
          </router-link>

        </el-menu>
      </el-aside>

      <!-- <el-divider direction="vertical"></el-divider> -->

      <!-- 右侧内容主体 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
export default {
    name: "index2",
    data(){
        return {

        }
    },
    methods: {
        logout () {
        window.sessionStorage.clear()
        this.$router.push('/login')
        this.$message.warning('退出登录')
        },
    }
}
</script>

<style>
.home_container {
  height: 100%;
}
.el-header {
  background-color: #FFFFFF;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #303133;
  font-size: 20px;
}
.el-header > div {
  display: flex;
  align-items: center;
}
.el-header > div > span {
  margin-left: 15px;
}
.el-header > div > img {
  width: 30px;
  height: 30px;
  margin-left: 15px;
}
.el-aside {
  background-color: #FFFFFF;
}
.el-menu {
  border-right: none;
}

.el-main {
  background-color: #FFFFFF;
}

a {
text-decoration: none;
}
.router-link-active {
text-decoration: none;
}
</style>