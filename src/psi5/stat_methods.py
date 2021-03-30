#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:23:41 2021

@author: patrizia
"""


import numpy as np
import pandas as pd


def calc_pairwise_corr(data: pd.DataFrame):
    """ Calculating the correlation between each columns

        Parameters:
            data (DataFrame): Data

        Returns:
            DataFrame: corr_list
    """
    corr = data.corr()
    for i in range(len(corr)):
        for j in range(len(corr)):
            if i >= j:
                corr.iloc[i, j] = np.nan
    corr_list = corr.stack().sort_values(ascending=False).reset_index()
    return corr_list
