"""Defines the default intrinsic camera matrix (K) using a configurable focal length.

This module exports a single function, `K`, which returns a 3x3 NumPy array
representing the camera's intrinsic matrix based on `Config.FOCAL_LENGTH`.
"""

import numpy as np

from .core import Config


__all__ = ("K",)


def K(cfg: Config) -> np.ndarray:
    """Return the default intrinsic parameter matrix, derived from `cfg.FOCAL_LENGTH`.

    Args:
        cfg: The configuration object, which includes `FOCAL_LENGTH`.

    Returns:
        A 3x3 NumPy array representing the intrinsic camera matrix.
    """
    # Preallocate the 3x3 matrix with zeros for efficiency
    result = np.zeros((3, 3), dtype=np.float32)
    
    # Set the diagonal elements
    result[0, 0] = cfg.FOCAL_LENGTH
    result[1, 1] = cfg.FOCAL_LENGTH
    result[2, 2] = 1.0  # Since this is a constant, it's not necessary to cast to float32 again
    
    return result
