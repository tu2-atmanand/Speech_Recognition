# Speech Recognition
This project is an analysis test to find a better Speech Recognition Engine to integrate in other projects.

My Analysis is in the [[Analysis]](https://github.com/tu2-atmanand/Speech_Recognition/blob/main/Analysis.md) file.

> The Winner of this Analysis test is **Vosk**.

The original Vosk project is [[HERE]](https://github.com/alphacep/vosk-api). You can use Vosk for other languages such as C++, Android, etc.

So this Repo will be a kind of tutorial as well as development to to train a Speech Recongnition model for you environment.

The Archived directory contains demo files for  the other two options i found for this analysis which are : Google Speech recognizer API and Pocketsphinx.

The directory Vosk contains just the main file and the model which you can easily use in you project directly to integrate this feature.

The other directory Vosk_Dev, contains all the original file from the original project, which demeonstrate how the engine works and how to train your own model.

To use Vosk directly into your project without going into much into the framework:
1. Download the Vosk folder into you project and run the VoskDemo.py.
2. Whenever you going to speak it will be stored in to the text variable which you can send in your project file.
