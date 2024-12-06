
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.webview import WebView

class WebApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        webview = WebView()
        webview.url = "https://testgpt-6u1q.onrender.com/"  # Replace with your desired URL
        layout.add_widget(webview)
        return layout

if __name__ == '__main__':
    WebApp().run()
