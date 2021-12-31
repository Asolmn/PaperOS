<template>
    <div>
        <el-tabs type="border-card">

            <el-form>
                <el-form-item label="选择学生" prop="region">
                    <el-select v-model="studentvalue" placeholder="筛选学生课题">
                        <el-option v-for="(i, index) in studentform" :value="i.username" :key="index" @click.native="studentid=i.stuid"></el-option>
                    </el-select>
                    &nbsp;
                    <el-button type="primary" @click="showpaper">确定</el-button>
                </el-form-item>
            </el-form>

            <el-tab-pane label="论文批阅">
                <el-table
                :data="paperlist"
                style="width: 100%"
                >
                    <el-table-column 
                    prop="filename" 
                    label="文件名"></el-table-column>

                    <el-table-column
                    prop="showstatus"
                    label="状态"
                    ></el-table-column>

                    <el-table-column
                    prop="student"
                    label="所属学生"
                    ></el-table-column>

                    <el-table-column
                    prop="date"
                    label="上传时间"
                    ></el-table-column>

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

                    <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button type="primary"
                                icon="el-icon-download"
                                size="mini"
                                @click="downfile(scope.row)">下载</el-button>
                    </template>
                    </el-table-column>

                </el-table>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>
<script>
export default {
    name: "teapaper",
    data(){
        return {
            studentform: [],
            studentvalue: "",
            paperlist: [],
            value: true,
            studentid: null
        }
    },
    async created(){
        var id = window.sessionStorage.getItem("id");
        // 获取所有学生的论文信息
        var stu_paper_data = {
            "id": id
        };
        const {data: result} = await this.$http.post('/paper/allstupaper', stu_paper_data);
        // console.log(result);
        // 判断状态
        for (var i=0; i<result.length; ++i){
            if (result.status){
                result[i]["showstatus"] = "通过"
            }else {
                result[i]["showstatus"] = "未通过"
            }
        }
        this.paperlist = result;
        console.log(this.paperlist);

        // 获取学生列表
        const {data: stulist} = await this.$http.post('/auth/allstulist', {'id': id})
        this.studentform = stulist;
    }
    ,
    methods: {
        async downfile(row){
            console.log(row.uuid);
            var down_info_data = {
                "uuid": row.uuid
            };
            // const {data: result} = await this.$http.post({url:'http://127.0.0.1:5000/paper/downloadfile',method: 'POST', data: down_info_data, responseType: 'blob'});
            const {data: result} = await this.$http.post('/paper/downloadfile',down_info_data, {responseType: 'blob'});
            console.log(result);
            
            var filename = row.filename;
            // 将二进制流转换为blob
            const blob = new Blob([result], { type:'application/msword'});

            if (navigator.msSaveBlob) {
                navigator.msSaveBlob(blob, filename)
            }else {
                // 创建下载链接downURL
                const link = document.createElement('a');
                link.style.display = 'none'
                link.href = URL.createObjectURL(blob)
                link.download = filename
                document.body.appendChild(link)
                link.click() // 执行下载
                URL.revokeObjectURL(link.href) // 释放 bolb 对象
                document.body.removeChild(link); // 下载完成移除元素
            }
        },
        async changestatus(row){
            console.log(row);
            console.log(row.uuid);
            var change_status_data = {
                'uuid': row.uuid
            }
            // 修改状态, 改变后的状态为true,所以执行通过课题请求，依然则反之
            if (row.status){
                const {data: changestatusfalse} = await this.$http.put('/paper/truepaper', change_status_data);
                this.$message.success("课题通过");
                console.log(changestatusfalse);

            }else {
                const {data: changestatustrue} = await this.$http.put('/paper/falsepaper', change_status_data);
                this.$message.warning("课题不通过");
                console.log(changestatustrue);
            }
            // 重新加载修改后的数据
            // 获取所指导学生的所有课题
            var all_paper_data = {
                'id': window.sessionStorage.getItem('id')
            }
            const {data: result} = await this.$http.post('/paper/allstupaper', all_paper_data);

            // 判断状态, 修改状态显示
            for (var i=0; i<result.length; ++i){
                if (result[i].status){
                    result[i]["showstatus"] = "通过"
                }else {
                    result[i]["showstatus"] = "未通过"
                }
            }
            this.paperlist = result;
        },
        async showpaper(){
            console.log(this.studentid);
            var stu_paper_data ={
                'id': this.studentid
            }
            // 获取选择学生的所有论文信息
            const {data:stupaper} = await this.$http.post('/paper/stupaperinfo', stu_paper_data);
            this.$message.success("筛选成功");

            console.log(stupaper);

            // 重新加载修改后的数据
            // 判断状态, 修改状态显示
            for (var i=0; i<stupaper['info'].length; ++i){
                if (stupaper['info'][i].status){
                    stupaper['info'][i]["showstatus"] = "通过"
                }else {
                    stupaper['info'][i]["showstatus"] = "未通过"
                }
            }
            this.paperlist = stupaper['info'];
        }
    }
}
</script>