import tensorflow as tf


def psnr(hr, sr):
    return tf.image.psnr(hr, sr, max_val=255)
