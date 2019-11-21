import pickle

import pandas as pd

file = open('ayodhya_verdict_speech_transcript.txt', 'r')

speech_txt = ["Speech", file.read()]

data = pd.DataFrame(speech_txt)

with open('speech_data.pkl', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)