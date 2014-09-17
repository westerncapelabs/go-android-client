from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen

class EndState(Screen):
	pass

class MyScreenManager(ScreenManager):
	pass

class AndroidClient(App):
    def build(self):
	self.endstate = EndState()
	root = MyScreenManager()
	root.add_widget(self.endstate)
	return root

if __name__ == "__main__":
	AndroidClient().run()

