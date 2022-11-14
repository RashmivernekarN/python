input in [2], in ()
----> 1 import tensorflow as tf
      2 print(tf.__version__)

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\tensorflow\__init__.py:469, in 
    467 if hasattr(_current_module, "keras"):
    468   try:
--> 469     _keras._load()
    470   except ImportError:
    471     pass

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\tensorflow\python\util\lazy_loader.py:41, in LazyLoader._load(self)
     39 """Load the module and insert it into the parent's globals."""
     40 # Import the target module and insert it into the parent's namespace
---> 41 module = importlib.import_module(self.__name__)
     42 self._parent_module_globals[self._local_name] = module
     44 # Emit a warning if one was specified

File C:\ProgramData\Anaconda3\envs\tf\lib\importlib\__init__.py:127, in import_module(name, package)
    125             break
    126         level += 1
--> 127 return _bootstrap._gcd_import(name[level:], package, level)

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\keras\__init__.py:21, in 
     15 """Implementation of the Keras API, the high-level API of TensorFlow.
     16 
     17 Detailed documentation and user guides are available at
     18 [keras.io](https://keras.io).
     19 """
     20 from keras import distribute
---> 21 from keras import models
     22 from keras.engine.input_layer import Input
     23 from keras.engine.sequential import Sequential

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\keras\models\__init__.py:18, in 
      1 # Copyright 2022 The TensorFlow Authors. All Rights Reserved.
      2 #
      3 # Licensed under the Apache License, Version 2.0 (the "License");
   (...)
     13 # limitations under the License.
     14 # ==============================================================================
     15 """Keras models API."""
---> 18 from keras.engine.functional import Functional
     19 from keras.engine.sequential import Sequential
     20 from keras.engine.training import Model

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\keras\engine\functional.py:34, in 
     32 from keras.engine import input_spec
     33 from keras.engine import node as node_module
---> 34 from keras.engine import training as training_lib
     35 from keras.engine import training_utils
     36 from keras.saving.legacy import serialization

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\keras\engine\training.py:45, in 
     43 from keras.saving.experimental import saving_lib
     44 from keras.saving.legacy import hdf5_format
---> 45 from keras.saving.legacy import save
     46 from keras.saving.legacy import saving_utils
     47 from keras.saving.legacy import serialization

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\keras\saving\legacy\save.py:24, in 
     22 from keras.saving.legacy import serialization
     23 from keras.saving.legacy.saved_model import load as saved_model_load
---> 24 from keras.saving.legacy.saved_model import load_context
     25 from keras.saving.legacy.saved_model import save as saved_model_save
     26 from keras.utils import traceback_utils

File C:\ProgramData\Anaconda3\envs\tf\lib\site-packages\keras\saving\legacy\saved_model\load_context.py:68, in 
     64     """Returns whether under a load context."""
     65     return _load_context.in_load_context()
---> 68 tf.__internal__.register_load_context_function(in_load_context)

AttributeError: module 'tensorflow._api.v2.compat.v2.__internal__' has no attribute 'register_load_context_function'