<template>
    <div>
        <el-tabs type="border-card">

        <el-tab-pane label="课题列表">

            <el-form>
                <el-form-item label="选择学生" prop="region">
                    <el-select v-model="studentvalue" placeholder="筛选学生课题">
                        <el-option v-for="(i, index) in studentform" :value="i.username" :key="index" @click.native="studentid=i.stuid"></el-option>
                    </el-select>
                    &nbsp;
                    <el-button type="primary" @click="showtopic">确定</el-button>
                </el-form-item>
            </el-form>

            <el-table
            :data="topiclist"
            style="width: 100%">
                <el-table-column
                label="课题"
                prop="topicname">
                </el-table-column>
                <el-table-column
                label="学生"
                prop="student">
                </el-table-column>
                <el-table-column
                label="状态"
                prop="showstatus">
                </el-table-column>

                <el-table-column
                align="right">
                    <template slot-scope="scope">
                        <el-switch
                        v-model="scope.row.status"
                        active-color="#13ce66"
                        inactive-color="#ff4949"
                        @change="changestatus(scope.row)"
                        ></el-switch>
                    </template>

                </el-table-column>
            </el-table>

        </el-tab-pane>

        <el-tab-pane label="课题信息" >
            <el-descriptions title="课题信息" v-for="(i,j) in topiclist" :key="j">
                <el-descriptions-item label="课题名">{{ i.topicname }}</el-descriptions-item>
                <el-descriptions-item label="所属学生">{{ i.student }}</el-descriptions-item>
                <el-descriptions-item label="状态">{{ i.status }}</el-descriptions-item>
                <el-descriptions-item label="UUID号">
                <el-tag size="small">{{i.uuid}}</el-tag>
                </el-descriptions-item>
                <el-descriptions-item label="学校">广州南方学院</el-descriptions-item>
            </el-descriptions>
        </el-tab-pane>
        
        </el-tabs>
    </div>
</template>
<script>
export default {
    name: "teatopic",
    data(){
        return {
            studentform: [],
            studentvalue: "",
            topiclist: [],
            value: true,
            studentid: null
        }
    },
    async created(){
        var id = window.sessionStorage.getItem('id');
        var all_topic_data = {
            'id': id
        }
        // 获取所指导学生的所有课题
        const {data: teainfo} = await this.$http.post('/topic/alltopic', all_topic_data);
        // console.log(teainfo)

        // 判断状态
        for (var i=0; i<teainfo.length; ++i){
            if (teainfo[i].status){
                teainfo[i]["showstatus"] = "通过"
            }else {
                teainfo[i]["showstatus"] = "未通过"
            }
        }

        this.topiclist = teainfo;
        console.log(this.topiclist);
        // 获取学生列表
        const {data: stulist} = await this.$http.post('/auth/allstulist', {'id': id})
        this.studentform = stulist;

    },
    methods: {
        async changestatus(row){
            console.log(row.uuid);
            var change_status_data = {
                'uuids': row.uuid
            }
            // 修改状态, 改变后的状态为true,所以执行通过课题请求，依然则反之
            if (row.status){
                const {data: changestatusfalse} = await this.$http.put('/topic/truestatus', change_status_data);
                this.$message.success("课题通过");
                console.log(changestatusfalse);

            }else {
                const {data: changestatustrue} = await this.$http.put('/topic/falsestatus', change_status_data);
                this.$message.warning("课题不通过");
                console.log(changestatustrue);
            }
            // 重新加载修改后的数据
            // 获取所指导学生的所有课题
            var all_topic_data = {
                'id': window.sessionStorage.getItem('id')
            }
            const {data: teainfo} = await this.$http.post('/topic/alltopic', all_topic_data);

            // 判断状态, 修改状态显示
            for (var i=0; i<teainfo.length; ++i){
                if (teainfo[i].status){
                    teainfo[i]["showstatus"] = "通过"
                }else {
                    teainfo[i]["showstatus"] = "未通过"
                }
            }
            this.topiclist = teainfo;
        },
        async showtopic(){
            console.log(this.studentid);
            var stu_topic_data ={
                'id': this.studentid
            }
            const {data: stutopic} = await this.$http.post('/topic/stutopic', stu_topic_data);
            this.$message.success("筛选成功");
            // 判断状态, 修改状态显示
            for (var i=0; i<stutopic.length; ++i){
                if (stutopic[i].status){
                    stutopic[i]["showstatus"] = "通过"
                }else {
                    stutopic[i]["showstatus"] = "未通过"
                }
            }
            this.topiclist = stutopic;
        }
    }
}
</script>