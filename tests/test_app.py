import pytest
import os
import sys

# --- ADD THESE THREE LINES TO FIX THE IMPORT ---
# Get the absolute path of the directory containing predict.py (the project root)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ---------------------------------------------

# Now the import will work:
from predict import predict

# ... rest of your test file ...

# Standard Iris example features (versicolor)
VERSICOLOR_FEATURES = [6.0, 2.9, 4.5, 1.5]


def test_prediction_output_is_string():
    """
    Test that the predict function returns a string (the class name).
    """
    prediction = predict(VERSICOLOR_FEATURES)

    # Assert that the output is a string class name
    assert isinstance(prediction, str)

    # Assert that the output is one of the valid class names
    valid_classes = ['setosa', 'versicolor', 'virginica']
    assert prediction in valid_classes