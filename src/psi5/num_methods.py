#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Mon Mar 24 17:12:17 2021

@author: florian

"""


import numpy as np
import pandas as pd


def dft(signal: pd.Series, times: pd.Series):
    """ Calculating the Direct Fourier Transform of a series
        and the corresponding frequencies from its time stamps

        Parameters:
            signal (pandas.Series): Signal
            times (pandas.Series): Time stamps of signal


		Returns:
			pandas.DataFrame: DFT
	"""
	freq = np.fft.fftfreq(times.size, times[1]-times[0])
	amp = np.fft.fft(signal)

	DFT= pd.DataFrame({ "freq": freq, "amp": amp })

	return DFT


def acf(signal: pd.Series):
    """ Calculating the (quasi) Autocorrelation Function of a series

		Returns:
			int, float, complex, ...: auto_corr
	"""
	auto_corr = 0

	for i in np.arange(0,signal.size,1):
		auto_corr += signal[i]*signal[0]

	return auto_corr

    return A
