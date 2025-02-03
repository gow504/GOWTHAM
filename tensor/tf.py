import tensorflow as tf
hello = tf.constant("hello world")
with tf.compat.v1.session() as sess:
    result=sees.run(hello)
    print(result.decode())