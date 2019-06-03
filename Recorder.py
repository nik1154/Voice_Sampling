"""
Recorder for wav format

Record one 30 sec audio
and one 5 sec, Change line number 30 to RECORD_SECONDS = 5

Author: Nikhil 
"""

import pyaudio
import wave 
import time

# Initialization
n = 1
m = 1

Name = [ 0 for i in range(10)]

# Training Part
while m != 0:
    Name[n-1] = input("Enter your name? ")

    print ("Hello, %s." % Name[n-1])

    BLOCKSIZE = 64  # Number of frames per block
    WIDTH = 2       # Number of bytes per sample
    CHANNELS = 1    # mono
    RATE = 16000    # Sampling rate (samples/second)
    RECORD_SECONDS = 30 # Time lasts for Recording ##Change this to 5 to record a 5 sec test audio
    ##Change the above to 5 to record a 5 sec test audio
    p1 = pyaudio.PyAudio()

    stream1 = p1.open(format = p1.get_format_from_width(WIDTH),
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    output = False)

    output_block = [0 for i in range(0, BLOCKSIZE)]

    output_wavefile = Name[n-1] + '.wav'
    output_wf = wave.open(output_wavefile, 'w')      # wave file
    output_wf.setframerate(RATE)
    output_wf.setsampwidth(WIDTH)
    output_wf.setnchannels(CHANNELS)

    num_blocks = int(RATE / BLOCKSIZE * RECORD_SECONDS)

    print('* Recording for {0:.3f} seconds '.format(RECORD_SECONDS))


# Start loop
    for i in range(0, num_blocks):

        input_string = stream1.read(BLOCKSIZE)   

        output_wf.writeframes(input_string)

    print('* Writing Done \n')

    stream1.stop_stream()
    stream1.close()
    p1.terminate()

    yn =input("Do you want to add another recorder? [Y/N] ")

    if yn == 'Y':
        n = n + 1
    elif yn == 'N':
        m = 0
