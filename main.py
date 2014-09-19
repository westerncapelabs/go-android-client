from kivy.app import App

from kivy.properties import NumericProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

#define a list of label strings
label_text = ['What is adf afkj af lj akj falj falfj aflj alfj alfj aflj aflj dfjalfj alfj jalfkj aflj aflkj falfj af your name afd af af fda fadsf adf adf af azf af af af?',
'Thank you for registering sdja fadskf akdsf adkf adfk adsf jadskf adf adsf adsf adf kadf adf adf adsf adsf ad fads fad fk!',
'Do you prefer tea or coffee adf  fakf kl fkal jkaflj aklf afd jakdfl jaflj f affkd jadf af dfaljf alfj af?']

#freetextstate screen
class FreeTextState(Screen):
	def set_label_text(self):
		return label_text[0]

#endstate screen
class EndState(Screen):
	def set_label_text(self):
		return label_text[1]

#choicestate screen
class ChoiceState(Screen):
	def set_label_text(self):
		return label_text[2]
	

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

