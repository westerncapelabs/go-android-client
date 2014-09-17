from kivy.app import App

from kivy.properties import NumericProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

class FreeTextState(Screen):
	pass

class EndState(Screen):
	pass

class ChoiceState(Screen):
	pass

class MyScreenManager(ScreenManager):
	pass

class CustomTextInput(TextInput):
	max_chars = NumericProperty(160)

	def insert_text(self, substring, from_undo=False):
		if not from_undo and (len(self.text)+len(substring) > self.max_chars):
			return
		super(CustomTextInput, self).insert_text(substring, from_undo)

class AndroidClient(App):
    def build(self):
	self.endstate = EndState()
	root = MyScreenManager()
	root.add_widget(self.endstate)
	return root

if __name__ == "__main__":
	AndroidClient().run()

