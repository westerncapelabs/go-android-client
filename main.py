import json

from kivy.app import App
from kivy.lang import Builder

from kivy.properties import NumericProperty, StringProperty, ObjectProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

#freetextstate screen
class FreeTextState(Screen):
	label_text = StringProperty()

	def set_label_text(self):
		return self.label_text

#endstate screen
class EndState(Screen):
	label_text = StringProperty()

	def set_label_text(self):
		return self.label_text

#choicestate screen
class ChoiceState(Screen):
	label_text = StringProperty()
	choices = ObjectProperty()

	def set_label_text(self):
		return self.label_text
	

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

#main application
class AndroidClient(App):
    def build(self):
		#load sample data
		with open('data/fixtures/example.json') as data_file:
			data = json.load(data_file)

		self.root = Builder.load_file('androidclient.kv')

		for i in range(len(data)):
			if data[i]['type'] == 'FreeText':
				self.root.ids.sm.add_widget(FreeTextState(label_text=data[i]['question']))
			elif data[i]['type'] == 'ChoiceState':
				self.root.ids.sm.add_widget(ChoiceState(label_text=data[i]['question'], choices=data[i]['choices']))
			elif data[i]['type'] == 'EndState':
				self.root.ids.sm.add_widget(EndState(label_text=data[i]['text']))

		return self.root

if __name__ == "__main__":
	AndroidClient().run()

