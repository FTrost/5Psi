#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:30:11 2021

@author: patrizia
"""


import pandas as pd


def filter_data(data: pd.DataFrame, min_variance: float):
    """
    Filter data by variance.

    All columns of the data which have a variance smaller than a defined
    minimum variance will be discarded.

    Parameters
    ----------
    data (DataFrame): data to be filterd
    min_variance: condition for filtering the data

    Returns
    -------
    DataFrame: filterd_data
    """
    data_var = data.var()
    drop_cols = data.columns[data_var < min_variance]
    filterd_data = data.drop(drop_cols, axis=1)
    return filterd_data
