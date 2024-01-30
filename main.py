from kivy.app import App
from kivy.uix.button import Button
from plyer import permission

class CameraApp(App):
    def build(self):
        button = Button(text='Request Camera Permission', on_press=self.request_camera_permission)
        return button

    def request_camera_permission(self, instance):
        if permission.check_permission('CAMERA') != 'granted':
            permission.request_permission('CAMERA')

if __name__ == '__main__':
    CameraApp().run()
