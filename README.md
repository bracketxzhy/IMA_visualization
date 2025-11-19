
# DICOM (.IMA) Single Image Quick Viewer

## Description
Simple tool to quickly preview a single DICOM image with `.IMA` extension (commonly used by GE, Siemens, Philips scanners).

## Data Requirements
Your project folder must be structured as follows:
```
project_folder/
└── data/
    ├── ANON_0001.IMA
    ├── ANON_0002.IMA
    └── ... (226 images in total)
```

- All `.IMA` files must be placed in the `data` folder  
- File names must follow the pattern `ANON_XXXX.IMA` (XXXX = 4-digit number)  
- `.IMA` files are standard DICOM files (only the extension is different)

**Default displayed image**: `data/ANON_0001.IMA`  
To view a different slice, edit line 5 in `visualization.py`:
```python
file_path = Path('data/ANON_0123.IMA')   # change the number here
```

## Environment Setup

### Recommended: conda
```bash
conda create -n dicom python=3.11 -y
conda activate dicom
conda install -c conda-forge pydicom matplotlib -y
```

### Alternative: pip (ensures genuine pydicom)
```bash
pip uninstall pydicom pydicom-seg -y
pip install --index-url https://pypi.python.org/simple pydicom matplotlib
```

## How to Run
```bash
python visualization.py
```
A window will open displaying the selected grayscale image.

## Common Issues
- `AttributeError: module 'pydicom' has no attribute 'dcmread'` → fake pydicom package installed; reinstall using the commands above.  
- Image appears all black or all white → window/level is not applied in this simple viewer (normal behavior). For proper clinical display, use RadiAnt, Weasis, Horos, or 3D Slicer.

2025-11-19 For research and educational use only
```
