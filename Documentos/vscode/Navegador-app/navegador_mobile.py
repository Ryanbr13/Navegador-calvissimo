from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import platform

if platform == "android":
    from android.webview import WebView

class Navegador(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.url_input = TextInput(hint_text="Digite a URL...", size_hint_y=None, height=50)
        self.url_input.bind(on_text_validate=self.load_url)
        self.add_widget(self.url_input)

        self.webview = WebView()
        self.add_widget(self.webview)

        self.button_layout = BoxLayout(size_hint_y=None, height=50)

        self.back_btn = Button(text="◀️ Voltar", on_press=lambda x: self.webview.go_back())
        self.forward_btn = Button(text="▶️ Avançar", on_press=lambda x: self.webview.go_forward())
        self.reload_btn = Button(text="🔄 Recarregar", on_press=lambda x: self.webview.reload())

        self.button_layout.add_widget(self.back_btn)
        self.button_layout.add_widget(self.forward_btn)
        self.button_layout.add_widget(self.reload_btn)

        self.add_widget(self.button_layout)

    def load_url(self, instance):
        url = self.url_input.text.strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.webview.load_url(url)

class NavegadorApp(App):
    def build(self):
        return Navegador()

if __name__ == "__main__":
    NavegadorApp().run()
