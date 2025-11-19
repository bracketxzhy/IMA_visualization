
# DICOM (.IMA) 单张图像快速查看工具

## 功能描述
快速显示单个 `.IMA` 格式的 DICOM 医学图像（常用于 GE、Siemens 等设备导出的序列）。

## 数据存放要求
请确保项目目录结构如下：
```
当前项目目录/
└── data/
    ├── ANON_0001.IMA
    ├── ANON_0002.IMA
    └── ...（共 226 张）
```
- 文件必须位于 `data   数据` 文件夹内  
- 文件命名必须为 `ANON_XXXX.IMA`（XXXX 为 4 位数字）  
- `.IMA` 文件本身就是标准 DICOM 文件，仅扩展名不同

**默认显示文件**：`data/ANON_0001.IMA`  
若需查看其他编号，只需修改脚本第 5 行：
```python   ”“python
file_path = Path('data/ANON_0026.IMA')   # ← 修改这里即可
```

## 运行环境配置（强烈推荐以下任一方式）

### 方式一：使用 conda（最稳定，推荐）
```bash   ”“bash
conda create -n dicom python=3.11 -yConda create -n dicom python=3.11Conda create -n dicom python=3.11
conda activate dicom   Conda激活dicom   Conda激活dicom
conda install -c conda-forge pydicom matplotlib -y
```

### 方式二：使用 pip（确保安装正版 pydicom）
```bash   ”“bash
pip uninstall pydicom pydicom-seg -y
pip install --index-url https://pypi.python.org/simple pydicom matplotlibPIP安装——index-url https://pypi.python.org/simple pydicom matplotlib
```

## 脚本内容（保存为 view_dicom.py）
```python   ”“python
import pydicom   进口pydicom
from pathlib import Path   从pathlib导入路径
import matplotlib.pyplot as plt进口matplotlib。Pyplot为PLT

file_path = Path('data/ANON_0001.IMA')             file_path = Path（'data/ANON_0001. 0001. '）IMA”)

ds = pydicom.dcmread(file_path)                 Ds = pydicom.dcmread（file_path）

plt.imshow(ds.pixel_array, cmap='gray')         plt.imshow (ds。pixel_array提出=“灰色”)
plt.axis('off')                                    plt.axis(“了”)
plt.title(file_path.name)
plt.show()
```

## 使用方法
```bash   ”“bash
python view_dicom.py
```
运行后会弹出窗口显示灰度图像。

## 常见问题解决
- `AttributeError: module 'pydicom' has no attribute 'dcmread'` → 一定是装了假包，按上面 conda 或 pip 方式重新安装。
- 图像全黑/全白 → 快速预览未做窗宽窗位处理，属于正常现象。如需精确显示，请使用 RadiAnt、Weasis、Horos、3D Slicer 等专业查看器。

2025-11-19　仅供学习与科研使用
```
