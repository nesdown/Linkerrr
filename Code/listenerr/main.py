import eel

from tkinter.filedialog import askopenfilename
from tkinter import Tk

import time
from time import sleep
from random import random, randint

# Import own modules
import noise_reduction as nr
import speech_recognize as sprec
import coincidence_counter as cc
import formatter as ft

# Initialize the web folder
eel.init('web')
# Define the functions to work with web interface
# eel.expose is a wrapper linking to the web functions - just like Electron

start_time = time.time()

@eel.expose
def select_audio_file():
    root = Tk()

    filename = askopenfilename()
    root.withdraw()

    return filename

@eel.expose
def select_audio_template():
    root = Tk()

    filename = askopenfilename()
    root.withdraw()

    return filename

@eel.expose
def start_analysis(audio_name, audio_template, result_filename, interference):
    eel.updateConsole("ANALYSIS HAS BEEN STARTED...")
    sleep(random()*2)

    # That's sorta system value
    AUDIO_TO_PROCESS = audio_name
    AUDIO_TEMPLATE = audio_template

    print("\n ================== \n")
    print ("Audio to check: "        + audio_name)
    print ("Audio Template: "        + audio_template)
    print ("Result Filename: "       + result_filename)
    print ("Interference Enabled: "  + interference)
    print("\n ================== \n")

    eel.updateConsole("Audio to check: "        + audio_name)
    sleep(random()*2)
    eel.updateConsole("Audio Template: "        + audio_template)
    sleep(random()*2)
    eel.updateConsole("Result Filename: "       + result_filename)
    sleep(random()*2)
    eel.updateConsole("Interference Enabled: "  + interference)

    if (interference == "True"):
        new_audio_name = nr.noise_reduction(audio_name, "interferred.wav")
        AUDIO_TO_PROCESS = new_audio_name

    else:
        print("You have selected NO INTERFERENCE MODE. That file has not been changed.")
        print("\n ================== \n")
        eel.updateConsole("NO INTERFERENCE MODE Selected")

    sleep(random()*2)
    eel.updateConsole("<br>=============<br>STARTING ANALYSIS...<br>=============<br>")

    # AUDIO FILE PROCESSOR
    percentage = 0
    for i in range(10):
        sleep(random()*2)
        percentage += randint(1, 7)

        if percentage >= 50:
            break

        eel.updateConsole(str(percentage) + "%")

    result_audio = sprec.cloud_recognition(AUDIO_TO_PROCESS)

    for i in range(10):
        sleep(random()*2)
        percentage += randint(1, 7)

        if percentage >= 100:
            break

    eel.updateConsole("<br>First Part of Common-Based Analysis Done.")

    percentage = 0
    for i in range(10):
        sleep(random()*2)
        percentage += randint(1, 7)

        if percentage >= 50:
            break

        eel.updateConsole(str(percentage) + "%")

    sleep(random()*2)
    eel.updateConsole("Word Recognition Accuracy: " + result_audio['accuracy'])
    sleep(random()*2)

    # AUDIO TEMPLATE PROCESSOR
    eel.updateConsole("Processing the template file...")
    for i in range(10):
        sleep(random()*2)
        percentage += randint(1, 7)

        if percentage >= 100:
            break

        eel.updateConsole(str(percentage) + "%")

    result_audio_template = sprec.cloud_recognition(AUDIO_TEMPLATE)

    for i in range(10):
        sleep(random()*2)
        percentage += randint(1, 7)

        if percentage >= 100:
            break

        eel.updateConsole(str(percentage) + "%")

    sleep(random()*2)
    eel.updateConsole("Template Recognition Accuracy: " + result_audio_template['accuracy'])
    sleep(random()*2)

    eel.updateConsole("Countining concidences...")

    sleep(random()*3)

    coincidence_counts = cc.count_coincidence(result_audio['google_speech'], result_audio_template['houndify'])

    eel.updateConsole("Counting completed. Redirecting...")

    current_time = time.time() - start_time

    sleep(random()*2)

    eel.showResults()

    analyze_results = ft.format_output(coincidence_counts, result_audio['accuracy'], result_audio_template['accuracy'], current_time)

    print(analyze_results)
    eel.showCircles(analyze_results[0], analyze_results[1], analyze_results[2])

@eel.expose
def rebuild_schema():
    pass

@eel.expose
def return_back():
    pass

eel.start('loading.html', size=(1040, 730))
