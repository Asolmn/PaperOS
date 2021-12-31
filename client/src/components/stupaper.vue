<template>
    <div>
        <el-tabs type="border-card">
            <el-tab-pane label="上传论文">
                <el-upload
                class="upload-demo"
                drag
                ref="uploads"
                accept=".docx"
                action="http://127.0.0.1:5000/paper/receivefile"
                :auto-upload="true"
                :show-file-list="false"
                :http-request="uploadfile"
                :multiple="false">
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__tip" slot="tip">只能上传docx文件，且不超过20M</div>
                </el-upload>
            </el-tab-pane>
            <el-tab-pane label="下载论文">
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
    name: 'stupaper',
    data(){
        return {
            id: null,
            paperlist: []
        }
    },
    async created(){
        this.id = window.sessionStorage.getItem('id');
        
        var paper_info_data = {
            'id': this.id
        }
        const {data: result} = await this.$http.post('/paper/stupaperinfo', paper_info_data)

        // 判断状态
        for (var i=0; i<result['info'].length; ++i){
            if (result['info'][i].status){
                result['info'][i]["showstatus"] = "通过"
            }else {
                result['info'][i]["showstatus"] = "未通过"
            }
        }

        this.paperlist = result['info']
        console.log(this.paperlist)
    },
    methods: {
        async uploadfile(param){
            var fileobj = param.file;
            var form = new FormData();
            form.append('file', fileobj);
            form.append('id', this.id);
            const {data: result} = await this.$http.post('/paper/receivefile', form, {'Content-Type':'multipart/form-data'});
            console.log(result);
            if (result.flag == 1){
                this.$message.success("上传成功")
            }
        },
        async downfile(row){
            console.log(row.uuid);
            var down_info_data = {
                "uuid": row.uuid
            };
            // const {data: result} = await this.$http.post({url:'http://127.0.0.1:5000/paper/downloadfile',method: 'POST', data: down_info_data, responseType: 'blob'});
            const {data: result} = await this.$http.post('/paper/downloadfile',down_info_data, {responseType: 'blob'});
            console.log(result);
            
            var filename = row.filename;
            
            const blob = new Blob([result], { type:'application/msword'});

            if (navigator.msSaveBlob) {
                navigator.msSaveBlob(blob, filename)
            }else {
                const link = document.createElement('a');
                link.style.display = 'none'
                link.href = URL.createObjectURL(blob)
                link.download = filename
                document.body.appendChild(link)
                link.click() // 执行下载
                URL.revokeObjectURL(link.href) // 释放 bolb 对象
                document.body.removeChild(link); // 下载完成移除元素
            }

        }
    }
}
</script>