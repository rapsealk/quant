#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np


def std(data, sample_variance=True):
    if not sample_variance:     # population variance
        return np.std(data)
    mean = np.mean(data)
    total = np.sum([(x - mean) ** 2 for x in data])
    variance = total / (len(data) - 1)
    return np.sqrt(variance)
