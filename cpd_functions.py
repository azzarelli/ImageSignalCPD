import ruptures as rpt
import matplotlib.pyplot as plt
def get_neighbour_change(signal, _signal):
    ''' Take a univariate signal and find changes over average change between neigbouring pixels
    '''
    avg = signal.mean()

    signal_ = [1 if (s > avg or _signal[idx]==1)  else 0  for idx, s in enumerate(signal)] # 1 if var>v_avg or if prior channel determined thiss
    return signal_


def get_simple_cpd(signal, _signal):
    '''
    inputs
        signal : list
            univariate heteroscedastic non-timeseries list
        _signal : list
            prior-constucted filter (builds on each channel)
    '''
    
    # change point detection
    model = "l1"  # "l2", "rbf"
    algo = rpt.Pelt(model=model, min_size=3, jump=5).fit(signal)
    my_bkps = algo.predict(pen=10)



    for b in my_bkps:
        _signal[b-1] = 1

    return _signal