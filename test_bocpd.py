import os

from signal import signal
from turtle import color
from unittest import signals
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def display_RGB_decomposed_image()->None:
    ''' Decompose the image into channels and display each channel '''
    fig, ax = plt.subplots(1, 3, constrained_layout=True, figsize=(20,10))

    ax[0].imshow(img_mat[:,:,0], cmap='Greys')

    ax[1].imshow(img_mat[:,:,1], cmap='Greys')

    ax[2].imshow(img_mat[:,:,2], cmap='Greys')

    xaxis_titles = ['Red', 'Green', 'Blue']
    for idx, a in enumerate(ax):
        a.set_xlabel(xaxis_titles[idx])

    plt.show()


def simple_trend_detector(signals):
    print('recieved')

def get_rolling_signal(signals):
    signals_ = []
    for idx, sig in enumerate(signals):
        ts = pd.Series(sig)
        ts_ = ts.rolling(window=20).std()
        signals_.append(ts_)
    return signals_


def img2signal(signal:list=[], row:int=1, rollcall:str='None'):
    ''' Display a signal for a given row '''
    if signal != [] and type(row) == type(1): # check input types
        if row > 0: # ensure inputs can be handled
            signal_channels = [signal[signal_row,:,0], signal[signal_row,:,1], signal[signal_row,:,2]]
          
            signals_ = get_rolling_signal(signal_channels)
            avg_signal = np.mean(signals_, axis=0)
            return signals_

signal_row = 3

def load_raw_data():
    img = Image.open('mountains.jpg')
    img = img.filter(ImageFilter.GaussianBlur(radius = 10))
    img_mat = np.asarray(img)
    signals = img2signal(img_mat, 10, 'var')
    return signals[0]


if __name__ == '__main__':
        
    df = load_raw_data()

    alg_ = Algorithm(
        CPD(),
        Simple_Analysis(),
        df
    )

    results = alg_.get_algorithm_results()
    for r in results:
        print(r.get_timespan(), r.get_score(), r.get_reason())






