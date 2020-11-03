from recognition import recognition
from training import training
from datasets import datasets

from delFile import del_file


def main():
    facedict = {}
    cur_path = r'./dataset/'
    while True:
        print('*' * 31)
        print('''
            opencv人脸识别
            --------------
            输入1,人脸采集
            输入2,人脸训练
            输入3,人脸识别
            输入d,删除数据
            输入q,退出程序      
        ''')
        print('*' * 31)
        num = input("请输入您的操作选择: ")
        if num == '1':
            mydict = datasets()
            facedict.update(mydict)
            print(facedict)
        elif num == '2':
            training()
        elif num == '3':
            recognition(facedict)
        elif num == 'd':
            del_file(cur_path)
        elif num == 'q':
            print("退出程序成功!")
            break
        else:
            print("您输入有误,请重新输入!")


if __name__ == '__main__':
    main()
