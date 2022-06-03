<template>
<div class="login">
    <el-card class="box-card">
            <el-form
                :model="loginform"
                :rules="rules"
                ref="loginFormRef"
                label-width="60px"
            >
            <h3>毕业设计系统</h3>
            <el-form-item label="用户名" prop="username">
                <el-input v-model="loginform.username" prefix-icon="el-icon-user-solid"></el-input>
            </el-form-item>

            <el-form-item label="密码" prop="password">
                <el-input v-model="loginform.password" prefix-icon="el-icon-lock" show-password></el-input>
            </el-form-item>
            <el-form-item class="radio">
                <el-radio  v-model="loginform.role" label="Admin" @change="adminbtn">管理员</el-radio>
                <el-radio  v-model="loginform.role" label="Teacher" @change="teacherbtn">教师</el-radio>
                <el-radio  v-model="loginform.role" label="Student" @change="studentbtn">学生</el-radio>
            </el-form-item>

            <el-form-item class="btns">
                <el-button type="primary" @click="userlogin">登录</el-button>
                <el-button type="info" @click="resetLoginForm">重置</el-button>
            </el-form-item>
        </el-form>
    </el-card>
</div>

</template>


<script>
// import axios from 'axios';
export default {
    name: 'login',
    data() {
        return {
            loginform: {
                username: '',
                password: '',
                role: ''
            },
            role: '',
            rules: {
                username: [
                    { rquired:true, message: '请输入用户名', trigger: 'blur'},
                    { min: 3, max: 5, message: "长度在3到5个字符", trigger: 'blur'}
                ],
                password: [
                    { rquired:true, message: '请输入用户名', trigger: 'blur'},
                    { min: 3, max: 5, message: "长度在3到20个字符", trigger: 'blur'}
                ]
            },
            userinfo: {

            }
        }
    },
    methods: {
        async userlogin(){      
            this.$refs.loginFormRef.validate(valid => {
                if (!valid) {
                    this.$message.error("内容错误");
                }
            });
            // 请求数据
            const {data: result} = await this.$http.post('/auth/login', this.loginform);
            console.log(result);
            
            // 获取不同用户的数据
            if (this.role == 'Admin') this.userinfo = result.userinfo[0];
            if (this.role == 'Student') this.userinfo = result.studentinfo[0];
            if (this.role == 'Teacher') this.userinfo = result.teacherinfo[0];

            // 请求失败
            if (result.flag == 0) {
                this.$message.error("登录失败");
            }
            // 请求成功并通过验证
            if (result.flag == 1){
                if (this.userinfo.username == this.loginform.username &&  this.userinfo.password == this.loginform.password){
                    if (this.role == 'Student'){
                        this.$message.success("登录成功");
                        window.sessionStorage.setItem("id", this.userinfo.id); // 记录id
                        this.$router.push('/index'); // 跳转到学生主页面
                    }
                    if (this.role == 'Teacher'){
                        this.$message.success("登录成功");
                        window.sessionStorage.setItem("id", this.userinfo.id); // 记录id
                        this.$router.push('/index2'); // 跳转到主页面
                    }
                    if (this.role == 'Admin'){
                        this.$message.success("登录成功");
                        window.sessionStorage.setItem("id", this.userinfo.id);
                        this.$router.push('/index3'); // 跳转到管理页
                    }

                }
            }
        },
        resetLoginForm() {
            // 重置方法
            this.$refs.loginFormRef.resetFields();
        },
        adminbtn() {
            this.role = 'Admin';
        },
        teacherbtn() {
            this.role = 'Teacher';
        },
        studentbtn() {
            this.role = 'Student';
            console.log(this.role);
        }
    }
}
</script>

<style>


.box-card {
    margin: 300px auto;
    width: 30%;
}
.box-card h3 {
    text-align: center;
}
.btns {
    display:block;
    margin:0 auto;
}
/* .radio {
    margin-left: 10px;
} */
</style>