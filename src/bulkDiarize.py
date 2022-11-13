import os
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
from speakerDiarization import diarizeAudio
import gc
from pydub import AudioSegment
import time


def diarizeFromFolder(fromFolder,toFolder):
    INPUT_FOLDER_PATH = fromFolder
    OUTPUT_FOLDER_PATH = toFolder

    InputFiles = os.listdir(INPUT_FOLDER_PATH)
    print("All-Files:",InputFiles)
   
    Total_time = 0
    total_audio_seconds = 0
    for ifile in InputFiles:
        print("Processing File:",ifile)
        file_name = ifile
        TOTAL_PATH = INPUT_FOLDER_PATH + file_name
        TOTAL_OUTPUT_PATH = OUTPUT_FOLDER_PATH + file_name.split(".")[0]+"/"
        if not os.path.exists(TOTAL_OUTPUT_PATH):
            os.makedirs(TOTAL_OUTPUT_PATH)

        audioSeconds = AudioSegment.from_file(TOTAL_PATH).duration_seconds
        start = time.time()
        diarizeAudio(TOTAL_PATH,TOTAL_OUTPUT_PATH,expectedSpeakers=2)
        end = time.time()

        computeTime = end-start
        computeSpeed = audioSeconds/computeTime
        print("Processing File Complete:",ifile)
  

        Total_time += computeTime
        total_audio_seconds += audioSeconds
        
        collected = gc.collect()
       



if __name__=="__main__":
    INPUT_FOLDER_PATH = "wavs/"
    OUTPUT_FOLDER_PATH = "Output/"
    diarizeFromFolder(INPUT_FOLDER_PATH,OUTPUT_FOLDER_PATH)

