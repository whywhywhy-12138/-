import os

def del_file(path,self):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path,i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
    self.log("数据删除格式化完毕!!!")