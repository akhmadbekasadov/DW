# Imports
import numpy as np
import scipy.fftpack
from drawnow import *
import Adafruit_ADS1x15
import datetime, threading, time
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, filtfilt, find_peaks

import dash
from dash.dependencies import Output #Event
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

# Create objets
#adc = Adafruit_ADS1x15.ADS1115()

# Create variables
y0 = []
y1 = []
y2 = []
y3 = []

fill = 1
counter = -100
y_fil_lo = []
y_fil_hi = []
temp_breath = []
timenow = time.time()
heartrate_median = 0
breathrate_median = 0
next_call = time.time()
next_call_calc = time.time()

#global next_call, fill, counter, fs, T, y0, y1, y2, y3

# Set timer of next interrupt:
next_call = next_call + 0.04
print(next_call)
threading.Timer(next_call - time.time(), read).start()
#print(time.time())
# Save the queried value:
f=open('live_data.csv','a')

