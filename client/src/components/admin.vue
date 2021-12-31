<template>
    <div>
        <el-tabs type="border-card">

            <el-tab-pane label="教师管理">
            <el-table
                :data="teainfolist"
                style="width: 100%"
                >
                    <el-table-column 
                    label="姓名" 
                    prop="username">
                    </el-table-column>
                    <el-table-column
                    label="角色"
                    prop="role">
                    </el-table-column>
                    <el-table-column
                    align="right"
                    >
                        <template slot-scope="scope">
                            <el-button
                            size="mini"
                            type="danger"
                            @click="deleteuser(scope.row)">Delete</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="学生管理">
            <el-table
                :data="stuinfolist"
                style="width: 100%"
                >
                    <el-table-column 
                    label="姓名" 
                    prop="username">
                    </el-table-column>
                    <el-table-column
                    label="所属教师"
                    prop="teacher">
                    </el-table-column>
                    <el-table-column
                    align="right"
                    >
                        <template slot-scope="scope">
                            <el-button
                            size="mini"
                            type="danger"
                            @click="deleteuser(scope.row)">Delete</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-tab-pane>

            <el-tab-pane label="管理员">
                <el-table
                    :data="adminfolist"
                    style="width: 100%"
                    >
                        <el-table-column 
                        label="姓名" 
                        prop="username">
                        </el-table-column>
                        <el-table-column
                        label="角色"
                        prop="role">
                        </el-table-column>
                        <el-table-column
                        align="right"
                        >
                            <template slot-scope="scope">
                                <el-button
                                size="mini"
                                type="danger"
                                @click="deleteuser(scope.row)">Delete</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
            </el-tab-pane>

            <el-tab-pane label="用户创建">
                <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
                添加用户
                </el-button>

                <el-drawer
                title="添加用户"
                :visible.sync="drawer"
                :direction="direction"
                :before-close="handleClose">
                    <el-form
                    :model="userForm"
                    ref="teaFormRef"
                    label-width="auto"
                    >
                        <el-form-item label="用户名" prop="username" style="width: 60%; margin-left: 5px">
                            <el-input v-model="userForm.username"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password" style="width: 60%; margin-left: 5px">
                            <el-input v-model="userForm.password"></el-input>
                        </el-form-item>
                        <el-form-item label="角色" prop="role" style="width: 60%; margin-left: 5px">
                            <el-select v-model="rolevalue" placeholder="请选择juese">
                                <el-option v-for="(i, index) in roleForm" :value="i.role" :key="index"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="createuser">创建</el-button>
                            <el-button type="info" @click="resetLoginForm">重置</el-button>
                        </el-form-item>
                    </el-form>
                </el-drawer>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
export default {
    name: "admin",
    data(){
        return {
            userForm: {
                "username": "",
                "password": "",
                "role": "",
                "teac": ""
            },
            roleForm: [
                {role: 'Admin'},
                {role: 'Student'},
                {role: 'Teacher'}
            ],
            stuinfolist: [],
            teainfolist: [],
            adminfolist: [],
            rolevalue: null,
            drawer: false,
            direction: 'rtl',
        }
    },
    async created(){
        // var id = window.sessionStorage.getItem("id");
        var stu_info_data = {
            "role": "Student"
        };
        var tea_info_data = {
            "role": "Teacher"
        }
        var adm_info_data = {
            "role": "Admin"
        };
        // 获取不同角色的用户列表
        const {data: admdata} = await this.$http.post('/auth/userinfo', adm_info_data);
        this.adminfolist = admdata

        const {data: studata} = await this.$http.post('/auth/userinfo', stu_info_data);
        this.stuinfolist = studata;

        const {data: teadata} = await this.$http.post('/auth/userinfo', tea_info_data);
        this.teainfolist = teadata;
    }
    ,
    methods: {
        handleClose(done) {
            this.$confirm('确认关闭？')
            .then(_ => {
                done();
                console.log(_);
            })
            .catch(_ => {
                console.log(_);
            });
        },
        async deleteuser(row){
            var user_del_data = {
                "id": row.id,
                "role": row.role
            }
            const {data: result} = await this.$http.delete('/auth/deleteuser', {data:user_del_data})
            if (result.flag == 1){
                this.$message.success("删除成功");
            }

            // 判断不同的角色，刷新不同的数据表
            if (row.role == 'Admin'){
                var adm_info_data = {
                    "role": "Admin"
                };
                const {data: admdata} = await this.$http.post('/auth/userinfo', adm_info_data);
                this.adminfolist = admdata
            }
            if (row.role == 'Teacher'){
                var tea_info_data = {
                    "role": "Teacher"
                }
                const {data: teadata} = await this.$http.post('/auth/userinfo', tea_info_data);
                this.teainfolist = teadata;
            }
            if (row.role == 'Student'){
                var stu_info_data = {
                    "role": "Student"
                };
                const {data: studata} = await this.$http.post('/auth/userinfo', stu_info_data);
                this.stuinfolist = studata;
            }
        },
        resetLoginForm(){
            // 重置方法
            this.$refs.teaFormRef.resetFields();
        },
        async createuser(){
            console.log(this.rolevalue);
            this.userForm['role'] = this.rolevalue;
            const {data: userdata} = await this.$http.post('/auth/register', this.userForm);
            console.log(userdata);

            this.$message.success("用户创建成功");
            // 判断不同的角色，刷新不同的数据表
            if (this.rolevalue == 'Admin'){
                var adm_info_data = {
                    "role": "Admin"
                };
                const {data: admdata} = await this.$http.post('/auth/userinfo', adm_info_data);
                this.adminfolist = admdata
            }
            if (this.rolevalue == 'Teacher'){
                var tea_info_data = {
                    "role": "Teacher"
                }
                const {data: teadata} = await this.$http.post('/auth/userinfo', tea_info_data);
                this.teainfolist = teadata;
            }
            if (this.rolevalue == 'Student'){
                var stu_info_data = {
                    "role": "Student"
                };
                const {data: studata} = await this.$http.post('/auth/userinfo', stu_info_data);
                this.stuinfolist = studata;
            }
        }
    }
}
</script>