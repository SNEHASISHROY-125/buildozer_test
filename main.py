# from kivy.app import App
from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.uix.button import Button
# from plyer import permission
# from kivy.utils import platform

from kivy.clock import Clock


from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivy.utils import platform

kv = '''
Screen: 
    MDIconButton:
        icon: 'camera'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: app.show_toast('test')
    
    MDIconButton:
        icon: 'lamp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: app.on_start_update()
'''

        
class CameraApp(MDApp):

    def build(self):
        
        if platform == 'android':
            from android.permissions import Permission, request_permissions, check_permission

            # from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA])    
        button = MDIconButton(text='Request Camera Permission', on_press=self.show_toast)
        return Builder.load_string(kv)
    
    def on_start_update(self):
        # return super().on_start()
        print('on_start')
        if platform == 'android':
            def update_ui(dt):
                try:
                    from jnius import autoclass
                    from android.permissions import Permission, request_permissions, check_permission
                    PythonActivity = autoclass('org.kivy.android.PythonActivity')
                    View = autoclass('android.view.View')
                    Window = autoclass('android.view.Window')
                    WindowManager = autoclass('android.view.WindowManager')
                    LayoutParams = autoclass('android.view.WindowManager$LayoutParams')
                    WindowInsets = autoclass('android.view.WindowInsets')

                    activity = PythonActivity.mActivity
                    window = activity.getWindow()
                    window.getDecorView().setSystemUiVisibility(
                        View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
                        View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION |
                        View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                    )
                    window.setStatusBarColor(0x00000000)

                    params = window.getAttributes()
                    params.layoutInDisplayCutoutMode = LayoutParams.LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES
                    window.setAttributes(params)
                except Exception as e:
                    print(e)
                    toast('Error updating UI')

            Clock.schedule_once(update_ui)


    def show_toast(self, t):
        '''Displays a toast on the screen.'''

        toast('Test Kivy Toast', background= [0,0,0,1], duration=1.2)
        print('test', t)
        self.request_camera_permission(t)

    def request_camera_permission(self, instance):
        if platform == 'android':
            from android.permissions import Permission, request_permissions, check_permission
            if not check_permission(Permission.CAMERA):
                request_permissions([Permission.CAMERA])
            else:
                toast('Permission already granted', duration=1.2)
        else: toast('Platform not supported',duration=1.2)

if __name__ == '__main__':
    CameraApp().run()
