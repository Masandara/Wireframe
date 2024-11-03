from kivy.app import App
from kivy.uix.screenmanager import (
    SlideTransition,
    FadeTransition,
    ScreenManager,
    Screen,
)
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import re  # Untuk melakukan validasi menggunakan regular expression
from kivy.lang import Builder
import os
from Mempelajari.main_Alfabet import AlfabetScreen
from Mempelajari.main_Menyusunsk import MenyusunSKScreen
from Mempelajari.Mengenalbs.main_Buah import BuahScreen
from Mempelajari.Mengenalbs.main_Sayur import SayurScreen
from Permainan.main_Tebakwarna import TebakWarnaScreen
from Permainan.main_Cocokgambar import MencocokkanGambarScreen
from Permainan.main_Penjumlahan import PenjumlahanScreen

# == Aplikasi Ayo Belajar ==
# Mengatur ukuran window (lebar, tinggi)
Window.size = (900, 500)
Window.clearcolor = (0.65, 0.65, 0.65, 0.7)


class HomeScreen(Screen):
    def save_name(self):
        user_name = (
            self.ids.name_input.text.strip()
        )  # Menghapus spasi di awal dan akhir input

        # Regular expression untuk memeriksa apakah karakter pertama adalah huruf
        if not re.match(r"^[A-Za-z]", user_name):
            self.show_error_popup("Masukkan Nama Yang Valid!")
        else:
            # Menyimpan nama di screen manager dan berpindah ke layar LayarScreen
            self.manager.get_screen("layar").ids.welcome_label.text = (
                f"Hai, {user_name}!\nYuk, mulai petualangan belajar kamu!"
            )

            self.manager.transition = FadeTransition(duration=0.3)
            self.manager.current = "layar"

    def show_error_popup(self, message):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_label = Label(text=message, font_size="15sp")
        close_button = Button(text="Tutup", size_hint=(None, None), size=(100, 40))

        layout.add_widget(popup_label)
        layout.add_widget(close_button)

        popup = Popup(
            title="Kesalahan", content=layout, size_hint=(None, None), size=(300, 200)
        )

        close_button.bind(on_press=popup.dismiss)
        popup.open()


class LayarScreen(Screen):
    def show_logout_popup(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_label = Label(text="Apakah Kamu Ingin Selesai?", font_size="15sp")

        button_layout = BoxLayout(
            orientation="horizontal", size_hint=(1, 0.3), spacing=50
        )
        yes_button = Button(text="Ya", size_hint=(None, None), size=(100, 40))
        no_button = Button(text="Tidak", size_hint=(None, None), size=(100, 40))

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        layout.add_widget(popup_label)
        layout.add_widget(button_layout)

        popup = Popup(
            title="Konfirmasi Pesan",
            content=layout,
            size_hint=(None, None),
            size=(300, 200),
        )

        yes_button.bind(on_press=lambda *args: self.logout(popup))
        no_button.bind(on_press=popup.dismiss)

        popup.open()

    def logout(self, popup):
        popup.dismiss()
        self.manager.transition = FadeTransition(duration=0.3)
        self.manager.current = "home"

    def on_touch_down(self, touch):
        # Cek jika ikon Exit diklik
        if self.ids.exit_icon.collide_point(*touch.pos):
            self.show_logout_popup()
            return True
        # Cek jika ikon Gear diklik (Anda bisa menambahkan logika lain di sini)
        elif self.ids.gear_icon.collide_point(*touch.pos):
            self.open_settings_widget()
            return True
        elif self.ids.mempelajari_image.collide_point(*touch.pos):
            self.go_to_mempelajari()
            return True
        elif self.ids.permainan_image.collide_point(*touch.pos):
            self.go_to_permainan()
            return True
        return super().on_touch_down(touch)

    def open_settings_widget(self):
        self.ids.settings_widget.opacity = 1  # Menampilkan widget pengaturan

    def close_settings_widget(self):
        self.ids.settings_widget.opacity = 0  # Menyembunyikan widget pengaturan

    def update_volume_label(self, slider_type, value):
        if slider_type == "music":
            self.ids.music_volume_label.text = f"{int(value)}%"
        elif slider_type == "speaker":
            self.ids.speaker_volume_label.text = f"{int(value)}%"

    def go_to_mempelajari(self):
        # Navigate to MempelajariScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.3)
        self.manager.current = "mempelajari"

    def go_to_permainan(self):
        # Navigate to PermainanScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.3)
        self.manager.current = "permainan"


class MempelajariScreen(Screen):
    def go_to_layar(self):
        # Navigate to LayarScreen with a fade transition
        self.manager.transition = SlideTransition(direction="left", duration=0.2)
        self.manager.current = "layar"

    def on_touch_down(self, touch):
        if self.ids.alfabet_image.collide_point(*touch.pos):
            self.go_to_alfabet()
            return True
        elif self.ids.mengenalbuahsayur_image.collide_point(*touch.pos):
            self.go_to_mengenalbs()
            return True
        elif self.ids.menyusunsukukata_image.collide_point(*touch.pos):
            self.go_to_menyusunsk()
            return True
        return super().on_touch_down(touch)

    def go_to_alfabet(self):
        # Navigate to AlfabetScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "alfabet"

    def go_to_mengenalbs(self):
        # Navigate to MengenalbsScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "mengenalbs"

    def go_to_menyusunsk(self):
        # Navigate to MenyusunSKScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "menyusunsk"


class MengenalBSScreen(Screen):
    def go_to_mempelajari(self):
        # Navigate back to MempelajariScreen with a fade transition
        self.manager.transition = SlideTransition(direction="left", duration=0.2)
        self.manager.current = "mempelajari"

    def on_touch_down(self, touch):
        if self.ids.buah_image.collide_point(*touch.pos):
            self.go_to_buah()
            return True
        elif self.ids.sayur_image.collide_point(*touch.pos):
            self.go_to_sayur()
            return True
        return super().on_touch_down(touch)

    def go_to_buah(self):
        # Navigate to BuahScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "buah"

    def go_to_sayur(self):
        # Navigate to SayurScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "sayur"


class PermainanScreen(Screen):  # Menambahkan PermainanScreen
    def go_to_layar(self):
        # Navigate to LayarScreen with a fade transition
        self.manager.transition = SlideTransition(direction="left", duration=0.2)
        self.manager.current = "layar"

    def on_touch_down(self, touch):
        if self.ids.tebakwarna_image.collide_point(*touch.pos):
            self.go_to_tebakwarna()
            return True
        elif self.ids.mencocokkangambar_image.collide_point(*touch.pos):
            self.go_to_mencocokkangambar()
            return True
        elif self.ids.penjumlahan_image.collide_point(*touch.pos):
            self.go_to_penjumlahan()
            return True
        return super().on_touch_down(touch)

    def go_to_tebakwarna(self):
        # Navigate to TebakWarnaScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "tebakwarna"

    def go_to_mencocokkangambar(self):
        # Navigate to MencocokkanGambarScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "mencocokkangambar"

    def go_to_penjumlahan(self):
        # Navigate to PenjumlahanScreen with a fade transition
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = "penjumlahan"


class AyoBelajarApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LayarScreen(name="layar"))
        sm.add_widget(MempelajariScreen(name="mempelajari"))
        sm.add_widget(PermainanScreen(name="permainan"))
        sm.add_widget(AlfabetScreen(name="alfabet"))
        sm.add_widget(MengenalBSScreen(name="mengenalbs"))
        sm.add_widget(BuahScreen(name="buah"))
        sm.add_widget(SayurScreen(name="sayur"))
        sm.add_widget(MenyusunSKScreen(name="menyusunsk"))
        sm.add_widget(TebakWarnaScreen(name="tebakwarna"))
        sm.add_widget(MencocokkanGambarScreen(name="mencocokkangambar"))
        sm.add_widget(PenjumlahanScreen(name="penjumlahan"))

        return sm


if __name__ == "__main__":
    AyoBelajarApp().run()
