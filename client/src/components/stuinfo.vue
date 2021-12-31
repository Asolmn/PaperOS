<template>
    <div>
        <el-tabs type="border-card">

        <el-tab-pane label="导师申请">
            <el-form>
                <el-form-item label="选择导师" prop="region">
                    <el-select v-model="teachervalue" placeholder="请选择导师">
                        <el-option v-for="(i, index) in teacherform" :value="i.username" :key="index"></el-option>
                    </el-select>
                    &nbsp;
                    <el-button type="primary" @click="selectteacher">确定</el-button>
                </el-form-item>
            </el-form>
        </el-tab-pane>

        <el-tab-pane label="信息显示" >
            <el-descriptions title="用户信息">
                <el-descriptions-item label="用户ID">{{ stuinfodata.id }}</el-descriptions-item>
                <el-descriptions-item label="用户名">{{ stuinfodata.username }}</el-descriptions-item>
                <el-descriptions-item label="角色">{{ stuinfodata.role }}</el-descriptions-item>
                <el-descriptions-item label="导师">
                <el-tag size="small">{{ stuinfodata.teacher }}</el-tag>
                </el-descriptions-item>
                <el-descriptions-item label="学校">广州南方学院</el-descriptions-item>
            </el-descriptions>
        </el-tab-pane>
        
        </el-tabs>
    </div>
</template>

<script>
export default {
    name: 'stuinfo',
    data(){
        return {
            teacherform: [
            ],
            teachervalue: '',
            selectdata: {
                "role": "Teacher"
            },
            stuinfodata: {

            }
        }
    },
    async created(){
        const {data: result} = await this.$http.post('/auth/getrole', this.selectdata);
       
        console.log(result);
        var teacher = result['roleinfo'][0]['teacher'];

        for (var i=0; i<teacher.length; ++i){
            this.teacherform.push({'username': teacher[i]});
        }
        console.log(this.teacherform)

        // 加载页面后，首次请求用户数据
        var show_stu_data = {
            'id': window.sessionStorage.getItem('id'),
            'role': 'Student'
        }

        this.stuinfodata = (await this.$http.post('/auth/getuserid', show_stu_data)).data['studentinfo'][0];
        console.log(this.stuinfodata);

        
    },
    methods: {
        // 选择导师
        async selectteacher(){
            console.log(this.teachervalue);
            // 获取用户id
            var id = window.sessionStorage.getItem('id');
            // 构建请求数据
            var change_teacher_data = {
                'stuid': id,
                'teaname': this.teachervalue
            }
            const {data: result} = await this.$http.put('/auth/selectteacher', change_teacher_data);
            if (result.flag == 0 ){
                this.$message.error("选择失败");
            }
            if (result.flag == 1){
                this.$message.success("选择成功");
            }
            console.log(result);

            // 获取修改后的用户数据, 用于用户信息显示
            var show_stu_data = {
                'id': window.sessionStorage.getItem('id'),
                'role': 'Student'
            }

            this.stuinfodata = (await this.$http.post('/auth/getuserid', show_stu_data)).data['studentinfo'][0];
            console.log(this.stuinfodata);
        },
    }
}
</script>