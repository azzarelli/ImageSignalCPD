from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from cpd_functions import *

def get_rolling_signal(signals):
    signals_ = []
    for sig in signals:
        ts = pd.Series(sig)
        ts_ = ts.rolling(window=20).std()
        ts_ = ts_.fillna(0)
        signals_.append(ts_.to_numpy())
    #print()
    return signals_


def img2signal(signal:list=[], direction:str='hz', rollcall:str='None'):
    ''' Turn image into signal and Return matrix of hzntl dataframe signals 
    
    return:
        signals: list of pd.Series (Rows, Channels)
            ordered list of hzntl channel signals, taking rolling variance of signals 
    '''
    imgH, imgW, imgCh = signal.shape
        
    signals_ = []

    if direction == 'hz':
        for row in range(imgH):
            signal_channels = []
            for ch in range(imgCh):
                signal_channels.append(signal[row,:,ch])
            
            signals_channels_ = get_rolling_signal(signal_channels)
            signals_.append(signals_channels_)

    elif direction == 'vrt':
        for col in range(imgW):
            signal_channels = []
            for ch in range(imgCh):
                signal_channels.append(signal[:,col,ch])
            
            signals_channels_ = get_rolling_signal(signal_channels)
            signals_.append(signals_channels_)

    elif direction == 'hzvrt':
        signals_hz = []
        signals_vrt = []

        for col in range(imgW):
            signal_channels = []
            for ch in range(imgCh):
                signal_channels.append(signal[:,col,ch])
                
            signals_channels_ = get_rolling_signal(signal_channels)
            signals_hz.append(signals_channels_)

        for row in range(imgH):
            signal_channels = []
            for ch in range(imgCh):
                signal_channels.append(signal[row,:,ch])
            
            signals_channels_ = get_rolling_signal(signal_channels)
            signals_vrt.append(signals_channels_)
        return signals_hz, signals_vrt

    return signals_


def signal2img(signals, length):
    img_ = []

    for i, signal in enumerate(signals):
        _signal = [0 for i in range(length)]
        for channel in signal:
            _signal = get_simple_cpd(channel, _signal)
        img_.append(_signal)

        if (i % 10) ==0:
            print('signal...',i)

    return img_

if __name__ == '__main__':
    img = Image.open('fores_mountains_720p.jpg')
    #img = img.filter(ImageFilter.GaussianBlur(radius = 10))
    img_mat = np.asarray(img)
    print(img_mat.shape)
    imgH, imgW, imgCh = img_mat.shape
    signalshz, signalsvrt = img2signal(img_mat, 'hzvrt', 'var')

    img_hz = signal2img(signalshz, imgH)
    img_vrt = signal2img(signalsvrt, imgW)

    fig, ax = plt.subplots(1, 1, constrained_layout=True, figsize=(20,5))
    
    img_hz = np.asarray(img_hz).T
    img_vrt = np.asarray(img_vrt)
    
    img__ = [[[0,0,0] for i in range(imgW)] for j in range(imgH)]
    
    for h in range(imgH):
        for w in range(imgW):
            if img_vrt[h][w] == 1 and img_hz[h][w]==1:
                img__[h][w] = img_mat[h][w]
    #ax.imshow(img__)


    np.save('./mountain_pelt_filt.npy', img__)

    #plt.show()

 









