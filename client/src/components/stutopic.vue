<template>
    <div>
        <el-tabs type="border-card">
        <el-tab-pane label="创建课题">
            <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
            创建课题
            </el-button>

            <el-drawer
            title="创建课题"
            :visible.sync="drawer"
            :direction="direction"
            :before-close="handleClose">
                <el-form
                :model="topicForm"
                ref="topicFormRef"
                label-width="auto"
                >
                    <el-form-item label="课题名称" prop="topicname" style="width: 60%; margin-left: 5px">
                        <el-input v-model="topicForm.topicname"></el-input>
                    </el-form-item>
                    <el-form-item label="所属学生" prop="username" style="width: 60%; margin-left: 5px">
                        <el-input v-model="topicForm.username"></el-input>
                    </el-form-item>
                    <el-form-item>
                <el-button type="primary" @click="createtopic">创建</el-button>
                <el-button type="info" @click="resetLoginForm">重置</el-button>
                    </el-form-item>
                </el-form>
            </el-drawer>

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
                prop="status">
                </el-table-column>
                <el-table-column
                align="right">
                <template slot-scope="scope">
                    <el-button
                    size="mini"
                    type="primary"
                    @click="dialogFormVisible = true; tempuuid=scope.row.uuid; tempname=scope.row.topicname">Edit</el-button>

                    <el-dialog title="修改课题" :visible.sync="dialogFormVisible">
                    <el-form :model="changeform">
                        <el-form-item label="课题名称" :label-width="formLabelWidth">
                        <el-input v-model="changeform.topicname" autocomplete="off"></el-input>
                        </el-form-item>
                    </el-form>
                    <div slot="footer" class="dialog-footer">
                        <el-button @click="dialogFormVisible = false">取 消</el-button>
                        <el-button type="primary" @click="changetopic()">确 定</el-button>
                    </div>
                    </el-dialog>
                    &nbsp;
                    <el-button
                    size="mini"
                    type="danger"
                    @click="deletetopic(scope.row)">Delete</el-button>
                </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="课题信息">
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
    name: 'stutopic',
    data(){
        return {
            // 创建课题表单内容
            topicForm: {
                topicname: "",
                username: "",
                uuids: ""
            },
            drawer: false,
            direction: 'rtl',
            topiclist: [], // 课题列表
            dialogFormVisible: false,
            formLabelWidth: '120px',
            changeform: {
                uuids: "",
                topicname: ""
            },
            tempuuid: "", // 用于存入获取当前行课题的uuid
            tempname: ""

        }
    },
    async created(){
        // 构建请求数据
        var stu_topic_data = {
            'id': window.sessionStorage.getItem('id')
        }
        const {data: result} = await this.$http.post('/topic/stutopic', stu_topic_data);
        console.log(result);
        this.topiclist = result;
        // 判断状态
        for (var i=0; i<this.topiclist.length; ++i){
            if (this.topiclist[i].status){
                this.topiclist[i].status = "通过";
            }else {
                this.topiclist[i].status = "未通过";
            }
        }
    },
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
      async createtopic(){
          // 创建课题
          const {data: result} = await this.$http.post('/topic/createtopic', this.topicForm);
          console.log(result)
          if (result.flag == 0){
              this.$message.error("创建失败");
          }
          if (result.flag == 1){
              this.$message.success("创建成功");
          }
        var stu_topic_data = {
            'id': window.sessionStorage.getItem('id')
        }
        // 获取所属学生的课题
        const {data: topicres} = await this.$http.post('/topic/stutopic', stu_topic_data);
        console.log(topicres);
        this.topiclist = topicres;

        // 判断状态
        for (var i=0; i<this.topiclist.length; ++i){
            if (this.topiclist[i].status){
                this.topiclist[i].status = "通过";
            }else {
                this.topiclist[i].status = "未通过";
            }
        }

      },

      async changetopic(){
        console.log(this.tempuuid)
        var uuid = this.tempuuid;
        // 请求参数
        var change_topic_data = {
            'uuids': uuid,
            'topicname': this.changeform.topicname,
        }
        // 更改课题
        const {data: result} = await this.$http.put('/topic/changetopicname', change_topic_data);
        console.log(result);
        if (result.flag == 1){
            this.$message.success("修改成功");
        }

        // 重新获取新的课题列表
        var stu_topic_data = {
            'id': window.sessionStorage.getItem('id')
        }
        const {data: res} = await this.$http.post('/topic/stutopic', stu_topic_data);
        console.log(res);
        this.topiclist = res;

        // 重新判断状态
        for (var i=0; i<this.topiclist.length; ++i){
            if (this.topiclist[i].status){
                this.topiclist[i].status = "通过";
            }else {
                this.topiclist[i].status = "未通过";
            }
        }
        
        // 修改成功后，关闭提示框
        this.dialogFormVisible = false;

      },

      async deletetopic(row){
        // console.log(row);
        console.log(row.uuid);
        var delete_topic_data = {
            'uuids': row.uuid
        }
        // 删除课题
        const {data: result} = await this.$http.delete('/topic/deletetopic', {data:delete_topic_data});
        if (result.flag == 1){
            this.$message.success("删除成功");
        }
        // 重新获取新的课题列表
        var stu_topic_data = {
            'id': window.sessionStorage.getItem('id')
        }
        const {data: res} = await this.$http.post('/topic/stutopic', stu_topic_data);
        console.log(res);
        this.topiclist = res;

        // 重新判断状态
        for (var i=0; i<this.topiclist.length; ++i){
            if (this.topiclist[i].status){
                this.topiclist[i].status = "通过";
            }else {
                this.topiclist[i].status = "未通过";
            }
        }
      },
      resetLoginForm(){
        // 重置方法
        this.$refs.topicFormRef.resetFields();
      },
    }
}
</script>