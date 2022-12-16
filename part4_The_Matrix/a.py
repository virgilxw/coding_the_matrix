from image_mat_util import file2mat,mat2display
from geometry_lab import *
a = translation(0, 0) * file2mat("part4_The_Matrix/a.png")[0]

# translation(-x,-y) + rotation(theta) * translation(x, y)
mat2display(a[0], a[1])