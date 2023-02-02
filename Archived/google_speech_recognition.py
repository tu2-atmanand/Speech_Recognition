from time import sleep

import pyttsx3
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

	

if __name__ == '__main__':
	remember = open('../TempTest/output.txt', 'a')
	r = sr.Recognizer()
	text=''
	while text != 'exit' :
		audio=''
		while sleep(1)==1:
			with sr.Microphone() as source:
				print('say something!')
				audio = r.listen(source)
			text = r.recognize_google(audio)
			remember.write(text)
			print('>>>>>>' + text)
			print("\ndone")
	try:
		text = r.recognize_google(audio)
		print('google think you said:\n' +text)
	except Exception as e:
		print(e)
	finally:
		remember.close()


	# with sr.Microphone() as source:
	# 	print('say something!')
	# 	audio = r.listen(source)
	# 	text = r.recognize_google(audio)
	# 	print('>>>>>>' + text)
	# 	print("done")




