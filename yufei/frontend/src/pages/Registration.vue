<template>
<div class="container">
<form class="needs-validation" novalidate>
  <div class="form-row">
    <div class="col-md-12 mb-12">
      <label for="validationCustom01">您 的 姓 名 :</label>
      <input type="text" class="form-control" id="name" v-model="msg.name">
      <small id="HelpInline" class="text-muted">
      {{errmsg.msg_name}}
    </small>
    </div>
    <div class="col-md-12 mb-12">
      <label for="validationCustom02">手 机 号 码 :</label>
      <input type="text" class="form-control" id="tel" v-model="msg.tel">
      <small id="HelpInline" class="text-muted">
      {{errmsg.msg_tel}}
    </small>
    </div>
  </div>
  <div class="form-row">
    <div class="col-md-12 mb-12">
      <label for="validationCustom04">选 择 性 别 :</label>
      <select class="custom-select" id="sex" v-model="msg.sex">
        <option value="先生" >先生</option>
        <option value="女士">女士</option>
      </select>
      <small id="HelpInline" class="text-muted">
      {{errmsg.msg_sex}}
    </small>
    </div>
    <div class="col-md-12 mb-12">
      <label for="validationCustom03">咨 询 内 容 :</label>
      <input type="text" class="form-control" id="question" v-model="msg.question">
      <small id="HelpInline" class="text-muted">
      {{errmsg.msg_question}}
    </small>
    </div>
    
  </div>
  <hr>
  <button class="btn btn-primary col-md-12 mb-12" type="submit" @click="clto()">提&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;交</button>
  
</form>
</div>
</template>

<script>
var msg={name:'',tel:'',sex:'先生',question:'',}
var errmsg={msg_name:'',msg_tel:'',msg_sex:'',msg_question:'',}
export default {
  data(){
    return{msg,errmsg}
    },
  methods:{
    clto:function(){

      if(msg.name.trim().length==0)
      {
        errmsg.msg_name='请输入您的姓名'
      }
      else if(msg.tel.trim().length==0)
      {
        errmsg.msg_name=''
        errmsg.msg_tel='请输入您的手机号码'
      }
      else if(!(/^1[34578]\d{9}$/.test(msg.tel)))
      {
        errmsg.msg_tel='请输入(正确)的手机号码'
      }
      else{
        errmsg.msg_tel=''
        this.$https.postFormData('postuserinfo/',{name:msg.name,tel:msg.tel,sex:msg.sex,question:msg.question}).then((res) => {
          alert(res.message)
          // this.$router.go(-1)
        }).catch(err=>{console.log(err)});  
      }         
    }
  }
}

</script>

<style scoped>
.container{margin-top: 100px;}
</style>