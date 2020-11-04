from recognition import recognition
from training import training
from datasets import datasets

from delFile import del_file

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.video_weight = tk.Label(self,
                                     bg='blue', width='80', height='25')
        self.video_weight.pack(side="left")

        self.frame_weight = tk.LabelFrame(self)
        self.frame_weight.pack()

        self.collect_weight = tk.Button(self.frame_weight,
                                        text='搜集人脸',
                                        width='10',
                                        command=self.create_input_win)
        self.collect_weight.grid(column=0, row=1, padx=8, pady=4)

        self.train_weight = tk.Button(self.frame_weight,
                                      text='人脸训练',
                                      width='10')
        self.train_weight.grid(column=0, row=2, padx=8, pady=4)

        self.recog_weight = tk.Button(self.frame_weight,
                                      text='人脸识别',
                                      width='10')
        self.recog_weight.grid(column=0, row=3, padx=8, pady=4)

        self.del_weight = tk.Button(self.frame_weight,
                                    text='删除数据',
                                    width='10')
        self.del_weight.grid(column=0, row=4, padx=8, pady=4)

        self.quit_weight = tk.Button(self.frame_weight,
                                     text='退出程序',
                                     width='10')
        self.quit_weight.grid(column=0, row=5, padx=8, pady=4)

        self.log_text = tk.Text(self.frame_weight, width='10', height='17')
        self.log_text.grid(column=0, row=6, ipadx=8, pady=4, ipady=4)

    def create_input_win(self):
        self.input_win=tk.Toplevel(self)

        self.frame_left=tk.Frame(self.input_win)
        self.frame_left.grid(row=0, column=0,padx=5,pady=10)

        self.bt_right=tk.Button(self.input_win,text='提交数据',width='10',height='2')
        self.bt_right.grid(row=0, column=1,padx=5,pady=10)

        self.bianhao=tk.Label(self.frame_left,
                              text='编号')
        self.bianhao.grid(row=0,column=0)

        self.input_bianhao = tk.Entry(self.frame_left)
        self.input_bianhao.grid(row=0, column=1)

        self.name = tk.Label(self.frame_left,
                                text='名字')
        self.name.grid(row=1,column=0)

        self.input_name = tk.Entry(self.frame_left)
        self.input_name.grid(row=1, column=1)


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


def mainui():
    window = tk.Tk()
    window.title("recognition")
    window.resizable(0, 0)
    app = Application(master=window)
    app.mainloop()


if __name__ == '__main__':
    main()
