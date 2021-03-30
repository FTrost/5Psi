#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:39:21 2021

@author: patrizia
"""


import pandas as pd
from psi5 import stat_methods as sm


test_df = pd.DataFrame(
    {'a': [1, 2, 1.5],
     'b': [1, 2, 3],
     'c': [3, 2, 1]},
    index=[1, 2, 3])

answer_df = pd.DataFrame(
    {'level_0': ['a', 'a', 'b'],
     'level_1': ['b', 'c', 'c'],
     0: [0.5, -0.5, -1.0]},
    index=[0, 1, 2])


def test_calc_pairwise_corr():
    pd.testing.assert_frame_equal(sm.calc_pairwise_corr(test_df, answer_df))
