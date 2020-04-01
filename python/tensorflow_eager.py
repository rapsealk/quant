#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import tensorflow as tf

gpu = tf.device('/GPU:0')
print(gpu)

print(tf.reduce_sum(tf.random.normal([1000, 1000])))
