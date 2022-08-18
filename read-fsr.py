# Imports
import numpy as np
import scipy.fft
from drawnow import *
#import Adafruit_ADS1x15

import board
# from adafruit_extended_bus import ExtendedI2C as I2C
import busio
i2c = busio.I2C(board.SCL, board.SDA)
# i2c = busio.I2C(GPIO.3, GPIO.2)
import adafruit_ads1x15.ads1115 as ADS

import datetime, threading, time
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, filtfilt, find_peaks

import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
#import dash_html_components as html

import plotly
import random
import plotly.graph_objs as go
from collections import deque


# Create objects
adc = ADS.ADS1115(i2c)

# Create variables
y0 = []
y1 = []
y2 = []
y3 = []

item_index = 1
counter = -100
y_fil_lo = []
y_fil_hi = []
temp_breath = []
timenow = time.time()
heartrate_median = 0
breathrate_median = 0
next_call = time.time()
next_call_calc = time.time()
T = 0
fs = 0

f = open('live_data.csv', 'a')

def current_milli():
    print (time.time()*1000)
    return time.time()*1000

def read_fer_ADC():
    global item_index
    # print(time.time())
    # Save the queried value:
    

    temp_read0 = adc.read(0)
    temp_read1 = adc.read(1)
    temp_read2 = adc.read(2)
    temp_read3 = adc.read(3)

    y0.append(temp_read0)
    y1.append(temp_read1)
    y2.append(temp_read2)
    y3.append(temp_read3)

    f.write(str(item_index) + "; " + str(current_milli()) + "; " + str(temp_read0) + "; " + str(temp_read1) + "; " + str(
        temp_read2) + "; " + str(temp_read3) + "\n")
    

    # print (datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

    # Delete old values if they exist:
    if (item_index >= ((T * fs) + 1)):
        y0.pop(0)
        y1.pop(0)
        y2.pop(0)
        y3.pop(0)
    item_index += 1



def main():
    print("Hello Prgram Started")

    while True:
        read_fer_ADC()
    f.close()

    
if __name__ == "__main__":
    main()
