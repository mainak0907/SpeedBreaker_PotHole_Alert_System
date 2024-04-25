import numpy as np
import os

from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

from tflite_support import metadata

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)



train_data = object_detector.DataLoader.from_pascal_voc(
    'iot_project/train',
    'iot_project/train',
    ['pothole', 'speed-breaker', 'obstruction']
)

val_data = object_detector.DataLoader.from_pascal_voc(
    'iot_project/validate',
    'iot_project/validate',
    ['pothole', 'speed-breaker', 'obstruction']
)





spec = model_spec.get('efficientdet_lite0')




model = object_detector.create(train_data, model_spec=spec, batch_size=4, train_whole_model=True, epochs=200, validation_data=val_data)



model.evaluate(val_data)


model.export(export_dir='.', tflite_filename='best.tflite')