import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('te486-320300-bd96fb80ab4c.json', scope)
client = gspread.authorize(creds)
iQue_sheet = client.open("InventoryBackend").get_worksheet(2)


class InventoryWindow(Screen):
    pass


class AddPartWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.np = []


    
    
    part_name = ObjectProperty(None)
    serial_number = ObjectProperty(None)
    on_hand_cnt = ObjectProperty(None)
    min_needed = ObjectProperty(None)

    
    
    
    
    def new_part(self):
        self.part_name = self.ids.part_name.text
        self.serial_number = self.ids.serial_number.text
        self.on_hand_cnt = self.ids.on_hand_cnt.text
        self.min_needed = self.ids.min_needed.text

        self.np = [self.part_name, self.serial_number, self.on_hand_cnt, self.min_needed]
        iQue_sheet.append_row(self.np)

class OnOrderWindow(Screen):
    pass

class OrderFormWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#now creat class Student task_1
class StudentInfo(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.np=[]
    STUDENT_ID = ObjectProperty(None)
    STUDENT_NAME = ObjectProperty(None)
    STDUENT_DOB = ObjectProperty(None)
    
    def new_part(self):
        self.STUDENT_ID = self.ids.STUDENT_ID.text  
        self.STUDENT_NAME = self.ids.STUDENT_NAME.text 
        self.STDUENT_DOB = self.ids.STDUENT_DOB.text       
        

        self.np = [self.STUDENT_ID, self.STUDENT_NAME, self.STDUENT_DOB ]
        iQue_sheet.append_row(self.np)




class InventoryApp(App):
    def build(self):
        
        sm = ScreenManager()
        self.title = '19TE486 シトゥー'
        sm.add_widget(InventoryWindow(name='inv_window'))
        sm.add_widget(OnOrderWindow(name='on_order_window'))
        sm.add_widget(AddPartWindow(name='add_part_window'))
        sm.add_widget(OrderFormWindow(name='order_form_window'))
        #Make a link to Student Info window task_2
        sm.add_widget(StudentInfo(name="studentinfo_window"))
        return sm

if __name__ == "__main__":
    InventoryApp().run()
