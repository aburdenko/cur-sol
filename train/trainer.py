
#%%
from deepchem.models.keras_model import KerasModel
import deepchem as dc
import tensorflow as tf
print(f'dc: {dc.__version__}')
print(f'tf: {tf.__version__}')

#%%
tasks, datasets, transformers = dc.molnet.load_bace_classification(featurizer='GraphConv')
train_dataset, valid_dataset, test_dataset = datasets

from deepchem.models.graph_models import GraphConvModel
model_dir = 'gs://cur-solubility/models/'
model = GraphConvModel(model_dir=model_dir, n_tasks=1, mode='regression', dropout=0.2)
model.fit(train_dataset, nb_epoch=15, deterministic=True)

#%%
metric = dc.metrics.Metric(dc.metrics.pearson_r2_score)
print('training set score:', model.evaluate(train_dataset, [metric]))
print('test set score:', model.evaluate(test_dataset, [metric]))



# %%
import os

import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)
model_dir = 'gs://cur-solubility/models/'
latest = tf.train.latest_checkpoint(model_dir)
latest


# Load the previously saved weights

# %%
# Re-evaluate the model
metric = dc.metrics.Metric(dc.metrics.pearson_r2_score)
print('training set score:', model.evaluate(train_dataset, [metric]))
print('test set score:', model.evaluate(test_dataset, [metric]))



# %%
# EXPERIMENTAL - try to convert KERAS Model to DEEPCHEM Model
# Create a new model Keras Model

def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])

  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=[tf.metrics.SparseCategoricalAccuracy()])

  return model

# Create a basic model instance
model = create_model()
model.load_weights(latest)

# Display the model's architecture
model.summary()

# %%
