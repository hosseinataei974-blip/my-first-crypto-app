from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class AndroidPanel(MDApp):
    def build(self):
        # تنظیم رنگ تم (قرمز و تیره)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        
        screen = MDScreen()
        
        # نوار ابزار بالا
        toolbar = MDTopAppBar(title="FF VIP ANDROID", pos_hint={"top": 1})
        screen.add_widget(toolbar)
        
        # وضعیت فعال‌سازی
        self.status = MDLabel(
            text="READY TO INJECT", 
            halign="center", 
            pos_hint={"center_y": 0.6},
            theme_text_color="Secondary"
        )
        screen.add_widget(self.status)
        
        # دکمه بزرگ برای گوشی
        btn = MDRaisedButton(
            text="ACTIVATE VIP MOD",
            size_hint=(0.7, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.activate
        )
        screen.add_widget(btn)
        
        return screen

    def activate(self, instance):
        self.status.text = "VIP ACTIVATED ✅"
        self.status.theme_text_color = "Custom"
        self.status.text_color = (0, 1, 0, 1) # رنگ سبز

AndroidPanel().run()