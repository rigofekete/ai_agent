
import sys

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install it using: pip install numpy")
    sys.exit()

def visualize_3d_array(array):
  """Prints a 3D NumPy array as a series of 2D slices."""
  if len(array.shape) != 3:
    print("Error: Input array must be 3-dimensional.")
    return

  depth = array.shape[0]
  for i in range(depth):
    print(f"Slice {i}:")
    print(array[i, :, :])
    print("-" * 20)

if __name__ == '__main__':
  # Example usage:
  array_3d = np.arange(24).reshape((2, 3, 4))
  visualize_3d_array(array_3d)
