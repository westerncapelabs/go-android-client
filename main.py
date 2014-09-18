from kivy.app import App

from kivy.properties import NumericProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

#freetextstate screen
class FreeTextState(Screen):
	pass

#endstate screen
class EndState(Screen):
	pass

#choicestate screen
class ChoiceState(Screen):
	pass

#custom screenmanager
class MyScreenManager(ScreenManager):
	pass

#function restricts textinput to 160 chars
class CustomTextInput(TextInput):
	max_chars = NumericProperty(160)

	def insert_text(self, substring, from_undo=False):
		if not from_undo and (len(self.text)+len(substring) > self.max_chars):
			return
		super(CustomTextInput, self).insert_text(substring, from_undo)

class AndroidClient(App):
    def build(self):
	#create screen instances
	self.freetextstate = FreeTextState()
	self.endstate = EndState()
	self.choicestate = ChoiceState()

	#load screen instances to screenManager & set current/active screen
	root = MyScreenManager()
	root.add_widget(self.freetextstate)
	root.add_widget(self.endstate)
	root.add_widget(self.choicestate)
	root.current = 'freetextstate'
	return root

if __name__ == "__main__":
	AndroidClient().run()

