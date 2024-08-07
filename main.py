import os.path
import tkinter as tk
import cv2

import utils
import db
from PIL import Image, ImageTk
from deepface import DeepFace



class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")
        
        self.login_button_main_window = utils.get_button(self.main_window, 'Log in ', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)
        
        self.new_user_main_window = utils.get_button(self.main_window, 'New User Registration', 'yellow', self.register, fg='black')
        self.new_user_main_window.place(x=750, y=400)
        
        self.webcam_label = tk.Label(self.main_window)
        self.webcam_label.place(x=10, y=0, height=500, width=700)
        
        
        
        self.add_webcam(self.webcam_label)
          
        self.db = './db'
        if not os.path.exists(self.db):
            os.mkdir(self.db) 
        self.log_path = './log.txt'
        

    def add_webcam(self , label):
        if 'cap' not in self.__dict__:
         self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()


    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame
        cv2.waitKey(30)
        
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        self._label.after(20, self.process_webcam)
        
    
    
   

    def login(self):
        unknown_img_path= './.temp.jpg'
        cv2.imwrite(unknown_img_path , self.most_recent_capture_arr)
        dfs = str(DeepFace.find(img_path = ".temp.jpg", db_path = "C:\Desktop\project1\db"))
        print(dfs)
        
        
        

    def register(self):
        self.new_reg_window = tk.Toplevel(self.main_window)  #creates a new window for new user 
        self.new_reg_window.geometry("1200x520+374+122")
        
        self.accept_button_new_user_window = utils.get_button(self.new_reg_window, 'Accept ', 'blue', self.accept_new_user)
        self.accept_button_new_user_window.place(x=750, y=300)
        
        self.try_again_button = utils.get_button(self.new_reg_window, 'Try Again', 'red', self.try_again_new_user)
        self.try_again_button.place(x=750, y=400)
        
        self.capture_label = utils.get_img_label(self.new_reg_window)
        self.capture_label.place(x=10, y=0, height=500, width=700) 
        
        self.add_img_to_label(self.capture_label)
        
        self.input_text= utils.get_entry_text(self.new_reg_window)
        self.input_text.place(x=750, y=110)
        
        self.text_label_new_user = utils.get_text_label(self.new_reg_window, 'Enter Username Here!')
        self.text_label_new_user.place(x=750, y=70)
        
    
       
    def add_img_to_label(self, label):
     img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
     most_recent_capture_pil = Image.fromarray(img_)
     imgtk = ImageTk.PhotoImage(image=most_recent_capture_pil)
     label.imgtk = imgtk
     label.configure(image=imgtk)
     self.reg_new_user_capture = self.most_recent_capture_arr.copy()


    def start(self):
        self.main_window.mainloop()
        
    def accept_new_user(self):
        name = self.input_text.get()
        
        cv2.imwrite(os.path.join(self.db, '{}.jpg'.format(name)), self.reg_new_user_capture)
        utils.msg_box('Congratulations! ', 'You have successfully registered ')
        self.new_reg_window.destroy()
        
    def try_again_new_user(self):
        self.new_reg_window.destroy()

   
if __name__ == "__main__":
    app = App()
    app.start()
