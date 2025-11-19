
# DICOM (.IMA) Single Image Quick Viewer

## Description
Simple tool to quickly preview a single DICOM image with `.IMA   。誓章` extension (commonly used by GE, Siemens, Philips scanners).

## Data Requirements
Your project folder must be structured as follows:项目文件夹的结构必须如下所示：
```
project_folder/
└── data/
    ├── ANON_0001.IMA
    ├── ANON_0002.IMA
```

- All `.IMA   。誓章` files must be placed in the `data   数据` folder  
- File names must follow the pattern `ANON_XXXX.IMA   ANON_XXXX。IMA` (XXXX = 4-digit number)  
- `.IMA   。誓章` files are standard DICOM files (only the extension is different)

**Default displayed image**: `data/ANON_0001.IMA   数据/ ANON_0001。IMA`  
To view a different slice, edit line 5 in `visualization.py`:
```python   ”“python
file_path = Path('data/ANON_0123.IMA')   # change the number here
```

## Environment Setup

### Recommended: conda
```bash   ”“bash
conda create -n dicom python=3.11 -yConda create -n dicom python=3.11
conda activate dicom   Conda激活dicom
conda install -c conda-forge pydicom matplotlib -y
```

### Alternative: pip (ensures genuine pydicom)
```bash   ”“bash
pip uninstall pydicom pydicom-seg -y
pip install --index-url https://pypi.python.org/simple pydicom matplotlibPIP安装——index-url https://pypi.python.org/simple pydicom matplotlib
```

## How to Run
```bash   ”“bash
python visualization.py
```
A window will open displaying the selected grayscale image.

## Common Issues
- `AttributeError: module 'pydicom' has no attribute 'dcmread'` → fake pydicom package installed; reinstall using the commands above.  
- Image appears all black or all white → window/level is not applied in this simple viewer (normal behavior). For proper clinical display, use RadiAnt, Weasis, Horos, or 3D Slicer.

2025-11-19 For research and educational use only
```
