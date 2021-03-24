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
			F: pandas.DataFrame
	"""
	freq = np.fft.fftfreq(times.size, times[1]-times[0])
	amp = np.fft.fft(signal)

	F = pd.DataFrame({ "freq": freq, "amp": amp })

	return F

