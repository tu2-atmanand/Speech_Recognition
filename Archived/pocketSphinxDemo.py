from pocketsphinx import LiveSpeech

try:
    # remember = open('output.txt', 'a')
    for phrase in LiveSpeech():
        print(phrase)
        # remember.write(str(phrase) + '\n')
except KeyboardInterrupt:
    print("\nDone")
except Exception as e:
    print(e)
# remember.close()