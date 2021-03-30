#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:31:01 2021

@author: lindenb
"""
import pytest
import pandas as pd
import numpy as np
from psi5 import helper_functions


@pytest.fixture(scope="module")
def test_threshold():
    return 0.5


@pytest.fixture(scope="module")
def test_df(test_threshold):
    length = 10
    random_numbers_1 = np.random.randn(length)
    random_numbers_2 = np.random.randn(length)
    accepted = random_numbers_1 / random_numbers_1.var() * (2 * test_threshold)
    rejected = random_numbers_2 / random_numbers_2.var() * (0.5 * test_threshold)
    df = pd.DataFrame({"A": np.ones(length),
                       "B": np.zeros(length),
                       "C": np.arange(length),
                       "D": accepted,
                       "E": rejected,
                       })
    return df


@pytest.fixture()
def reference_df(test_df):
    df = test_df.copy()
    df.drop(["A", "B", "E"], axis=1, inplace=True)
    return df


def test_filter_data(test_df, test_threshold, reference_df):
    test_result = helper_functions.filter_data(test_df, test_threshold)
    pd.testing.assert_frame_equal(test_result, reference_df)
