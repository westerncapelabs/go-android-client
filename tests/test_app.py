"""
Tests for go-android-client.
"""

import json
import os.path
import unittest

from kivy.app import App
from kivy.clock import Clock

from main import AndroidClient, FreeTextState

class AppTest(unittest.TestCase):

	#test starting app using kivy
	def test_start_app_with_kv(self):
		class AndroidClient(App):
			pass
		a = AndroidClient()
		Clock.schedule_once(a.stop, .1)
		a.run()


	#test setting screen label
	def test_set_screen_label_text(self):
		freetextstate = FreeTextState(label_text='label name')
		label_name = freetextstate.set_label_text()
		if not label_name == 'label name':
			raise Exception("screen label text not set")

