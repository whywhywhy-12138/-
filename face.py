import threading
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import ttk

import cv2
from PIL import Image, ImageTk

from reco import recognition
from colllect import collect

lk = threading.Lock()

def video_thread(self):
    self.th_run = True
    self.con = 1
    self.train_weight.configure(state='disable')
    self.recog_weight.configure(state='active')
    while self.con == 1:
        _, img_bgr = self.cam.read()  # 读取照片
        self.imgtk = self.get_imgtk(img_bgr)
        self.video_weight.configure(image=self.imgtk, width=600, height=480)

class Application(ttk.Frame):
    cam=None
    th_run = False
    th = None
    viewhigh = 600
    viewwide = 600
    con=0

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_weight()
        self.cam_init()
        self.video_display()

    def create_weight(self):
        self.video_weight = tk.Label(self,
                                     width=80,
                                     height=25,
                                     bg='gray')
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
                                      width='10',
                                      command=self.video_display)
        self.train_weight.grid(column=0, row=2, padx=8, pady=4)

        self.recog_weight = tk.Button(self.frame_weight,
                                      text='人脸识别',
                                      width='10',
                                      command=self.reco_th)
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
        self.input_win = tk.Toplevel(self)

        self.frame_left = tk.Frame(self.input_win)
        self.frame_left.grid(row=0, column=0, padx=5, pady=10)

        self.bt_right = tk.Button(self.input_win, text='提交数据', width='10', height='2',command=self.collect_th)
        self.bt_right.grid(row=0, column=1, padx=5, pady=10)

        self.bianhao = tk.Label(self.frame_left,
                                text='编号')
        self.bianhao.grid(row=0, column=0)

        self.input_bianhao = tk.Entry(self.frame_left)
        self.input_bianhao.grid(row=0, column=1)

        self.name = tk.Label(self.frame_left,
                             text='名字')
        self.name.grid(row=1, column=0)

        self.input_name = tk.Entry(self.frame_left)
        self.input_name.grid(row=1, column=1)

    def get_imgtk(self, img_bgr):
        self.img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(self.img)
        imgtk = ImageTk.PhotoImage(image=im)
        wide = imgtk.width()
        high = imgtk.height()
        if wide > self.viewwide or high > self.viewhigh:
            wide_factor = self.viewwide / wide
            high_factor = self.viewhigh / high
            factor = min(wide_factor, high_factor)
            wide = int(wide * factor)
            if wide <= 0: wide = 1
            high = int(high * factor)
            if high <= 0: high = 1
            im = im.resize((wide, high), Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=im)
        return imgtk

    def cam_init(self):
        if self.th_run:
            return
        if self.cam is None:
            self.cam = cv2.VideoCapture(0)
            if not self.cam.isOpened():
                mBox.showwarning('警告', '摄像头打开失败！')
                self.cam = None
                return

    def video_display(self):
        self.th = threading.Thread(target=video_thread, args=(self,))
        self.th.setDaemon(True)
        self.th.start()
        self.th_run = True

    def collect_th(self):
        self.co_th = threading.Thread(target=collect, args=(self,))
        self.co_th.setDaemon(True)
        self.co_th.start()
        self.th_run = True

    def reco_th(self):
        self.re_th = threading.Thread(target=recognition, args=(self,))
        self.re_th.setDaemon(True)
        self.re_th.start()
        self.th_run = True

def on_closing():
    print("destroy")
    '''if app.th_run:
        app.th_run = False
        app.th.join(1)'''
    window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    window.title("recognition")
    window.resizable(0, 0)
    app = Application(window)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
