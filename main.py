from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class EndStateWidget(BoxLayout):
	pass

class AndroidClient(App):
    def build(self):
		return EndStateWidget()

if __name__ == "__main__":
	AndroidClient().run()

