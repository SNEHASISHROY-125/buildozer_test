# from kivy.app import App
from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.uix.button import Button
# from plyer import permission
from kivy.utils import platform

class CameraApp(MDApp):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA])    
        button = Button(text='Request Camera Permission', on_press=self.show_toast)
        return button


    def show_toast(self, t):
        '''Displays a toast on the screen.'''

        toast('Test Kivy Toast', background= [0,0,0,1], duration=1.2)
        print('test', t)

    def request_camera_permission(self, instance):...

        # if permission.check_permission('CAMERA') != 'granted':
        #     permission.request_permission('CAMERA')

if __name__ == '__main__':
    CameraApp().run()
