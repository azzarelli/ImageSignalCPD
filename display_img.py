from signal import signal
from turtle import color
from unittest import signals
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def display_signal_from_row(signal:list=[], row:int=1, rollcall:str='None')->None:
    ''' Display a signal for a given row '''
    if signal != [] and type(row) == type(1): # check input types
        if row > 0: # ensure inputs can be handled
            signal_channels = [signal[signal_row,:,0], signal[signal_row,:,1], signal[signal_row,:,2]]
            print(signal_channels)
            
            fig, ax = plt.subplots(1, 2, constrained_layout=True, figsize=(20,5))
            
            if rollcall == 'None':
                ax[0].plot(signal_channels[0], color='red')
                ax[0].plot(signal_channels[1], color='green')
                ax[0].plot(signal_channels[2], color='blue')
                ax[1].imshow(img_mat)
                plt.show()
            elif rollcall == 'var': # Here we are displaying the rolling variance of each channel
                signals_ = get_rolling_signal(signal_channels)
                avg_signal = np.mean(signals_, axis=0)

                ax[0].plot(signals_[0], color='red')
                ax[0].plot(signals_[1], color='green')
                ax[0].plot(signals_[2], color='blue')
                ax[1].imshow(img_mat)

                plt.show()


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