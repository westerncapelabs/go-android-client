from kivy.app import App
from kivy.lang import Builder

from kivy.properties import NumericProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
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

#function to load dynamic choicestate buttons
class AddChoiceButton(BoxLayout):
	def __init__(self, *args, **kwargs):
		super(AddChoiceButton, self).__init__(*args, **kwargs)
		for i in range (3):
			btn = Button(text=str(i) +'. ' + 'Option '+ str(i),  font_size=18)
			self.add_widget(btn)

#function restricts textinput to 160 chars
class CustomTextInput(TextInput):
	max_chars = NumericProperty(160)

	def insert_text(self, substring, from_undo=False):
		if not from_undo and (len(self.text)+len(substring) > self.max_chars):
			return
		super(CustomTextInput, self).insert_text(substring, from_undo)

class AndroidClient(App):
    def build(self):

	root = Builder.load_file('androidclient.kv')
	root.current = 'freetextstate'
	return root

if __name__ == "__main__":
	AndroidClient().run()

