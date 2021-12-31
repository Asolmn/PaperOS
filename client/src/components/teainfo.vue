<template>
    <div>
        <el-tabs type="border-card">

        <el-tab-pane label="教师信息">
            <el-descriptions title="用户信息">
                <el-descriptions-item label="用户ID">{{ teainfodata.id }}</el-descriptions-item>
                <el-descriptions-item label="用户名">{{ teainfodata.username }}</el-descriptions-item>
                <el-descriptions-item label="角色">{{ teainfodata.role }}</el-descriptions-item>
                <el-descriptions-item label="学生数量">
                <el-tag size="small">{{ studentnum }}</el-tag>
                </el-descriptions-item>
                <el-descriptions-item label="学校">广州南方学院</el-descriptions-item>
            </el-descriptions>
        </el-tab-pane>

        <el-tab-pane label="学生列表">
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
                        @click="deletestu(scope.row)">Delete</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>

        <el-tab-pane label="学生信息" >
            <el-descriptions title="学生信息" v-for="(i,j) in stuinfolist" :key="j">
                <el-descriptions-item label="用户ID">{{ i.id }}</el-descriptions-item>
                <el-descriptions-item label="用户名">{{ i.username }}</el-descriptions-item>
                <el-descriptions-item label="角色">{{ i.role }}</el-descriptions-item>
                <el-descriptions-item label="所属教师">
                <el-tag size="small">{{i.teacher}}</el-tag>
                </el-descriptions-item>
                <el-descriptions-item label="学校">广州南方学院</el-descriptions-item>
            </el-descriptions>
        </el-tab-pane>
        
        </el-tabs>
    </div>
</template>
<script>
export default {
    name: "teainfo",
    data(){
        return {
            teainfodata: {

            },
            studentnum: 0,
            stuinfolist: []
        }
    },
    async created(){
        // 加载页面后，首次请求用户数据
        // console.log(window.sessionStorage.getItem('id'));
        var show_tea_data = {
            'id': window.sessionStorage.getItem('id'),
            'role': 'Teacher'
        }
        // 获取教师信息
        this.teainfodata = (await this.$http.post('/auth/getuserid', show_tea_data)).data['teacherinfo'][0];
        console.log(this.teainfodata);
        // 统计学生数量
        this.studentnum = this.teainfodata.students.length;
        // console.log(this.studentnum);

        // 获取教师下的学生信息
        var show_tea_stu_data = {
            'id': window.sessionStorage.getItem('id')
        }
        const{data: result} = await this.$http.post('/auth/teastulist', show_tea_stu_data);
        this.stuinfolist = result;
        // console.log(this.stuinfolist);

    },
    methods: {
        async deletestu(row){
            console.log(row.id);
            var relieve_stu_data = {
                "stuid": row.id
            }
            // 接触关系
            const {data:result} = await this.$http.put('/auth/relievestu', relieve_stu_data);
            console.log(result)

            if (result.flag == 1){
                this.$message.success("删除成功");
            }

            // 获取教师下的学生信息
            var show_tea_stu_data = {
                'id': window.sessionStorage.getItem('id')
            }
            const{data: res} = await this.$http.post('/auth/teastulist', show_tea_stu_data);
            this.stuinfolist = res;
            console.log(this.stuinfolist);
        }
    }
}
</script>