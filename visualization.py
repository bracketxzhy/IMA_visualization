import pydicom
from pathlib import Path
import matplotlib.pyplot as plt

file_path = Path('data/ANON_0001.IMA')             

ds = pydicom.dcmread(file_path)                 

plt.imshow(ds.pixel_array, cmap='gray')         
plt.axis('off')                                 
plt.show()