# Analysis
### First Option : Google Speech Recognizer.
This is the simplest method to do, just install speech_recognition module through pip and start using it the example is [[Here]](https://github.com/tu2-atmanand/Speech_Recognition/blob/main/Archived/google_speech_recognition.py).
The problems with this is:
1. Only 50 requests can be sent per day.
2. works very slow if slow internet connection.
3. Uses internet that is API, so not so anonymous.


## Second Option : PocketSphinx
This is best i found after above option. Overcomes the problem of limitation of API requests, because it is offline can work forever.
1. This is offline
2. Not able to detect as good as option 1 and option 2
3. Also to train your own model or use for development little difficult to understand.

To test it the sampel code is [[Here]](https://github.com/tu2-atmanand/Speech_Recognition/blob/main/Archived/pocketSphinxDemo.py).


## Third Option : Vosk-api
This is the winner of this test. This is working awesome thnan option 2, and also can come close to google. With just 40mb prebuilt model it is working fine.
1. Can detect speech continuously and donot miss the words.
2. lightweight than option 1.
3. Easier to understand than option 2.
4. Can be used for other languages also.

The original Vosk project is [[HERE]](https://github.com/alphacep/vosk-api).



## Conclusion:
So now since i got the  best, i am working on the option 3 and i have put both the other project option 1 and 2 in Archived folder. And now I am gonna work on the main option : VOSK.

I know in this project also i can train my model, but for option 2, good documentation is available, so if you couldnt able to do it in VOSK try the other.

