import tensorflow as tf
import numpy as np



a = tf.constant(np.random.randint(0,100, size = (4,4)))
b = tf.constant(np.random.ranint(0,100, size = (4,8)))


c = tf.dot(a,b)
