

# YOLOX for Windows - simplied

<img src="https://user-images.githubusercontent.com/37477845/135489488-c55996d8-d32f-4612-8c99-8cdc37f7e7b2.gif" width="60%"><br>

Based on the repo: https://github.com/Kazuhito00/YOLOX-Colaboratory-Training-Sample

## Installation

### Install Visual Studio Build Tools 2019

If you are using CUDA 11.8, you will need to install **Visual Studio Build Tools 2019**. Follow the steps in this video tutorial:

👉 [Visual Studio Build Tools 2019 Installation Video](https://youtu.be/lW_xccf8uFA?si=MoGhn54JHjQYrTk2)

Make sure the **“Desktop development with C++"** workload is installed and that these components are selected:

- MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.29)
- Windows 10 SDK (10.0.19041.0)

Once the installation is complete, **restart your computer**.

**Note (not tested):** If you have the latest CUDA (as per May 2025), try installing **Visual Studio Build Tools 2022** and its **“Desktop development with C++"** workload (with MSVC v143 and Windows 11 SDK).

---

### Create Conda Environment

```bash
conda create -n yolox_env python=3.10
conda activate yolox_env
```

---
### YOLOX Installation

Clone this repo:

```bash
git clone https://github.com/ainhoaarnaiz/YOLOX_for_Windows.git
```

Clone YOLOX repo inside this repo:

```bash
cd YOLOX_for_Windows
git clone https://github.com/Megvii-BaseDetection/YOLOX
cd YOLOX
```

Install the dependencies (change the CUDA version to yours):

```bash
pip install torch==2.3.0+cu118 torchvision==0.18.0+cu118 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
python -m pip install -U pip
pip install -U pip setuptools wheel
pip install -U opencv-python cython
conda install -c conda-forge cmake
conda install -c conda-forge protobuf
```

In requirements.txt inside change from:
```bash
onnx==1.8.1
onnxruntime==1.8.0
```
to:
```bash
onnx==1.14.1
onnxruntime==1.12.0
```

And then, run it:
```bash
pip install -r requirements.txt
```

Install YOLOX:
```bash
pip install -v -e .  
```

### fast.ai Installation (Optional)

Install fast.ai using pip:
```bash
pip install fastai
```

Make sure to also install the correct Numpy version:
```bash
pip uninstall numpy -y
pip install numpy==1.26.4
```

Double check the correct torch is also still installed:
```bash
pip install torch==2.3.0+cu118 torchvision==0.18.0+cu118 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
```

**IMPORTANT**: This steps need revision.

---


## Usage

**INPORTANT:** Follow all the steps on the **YOLOX_traing.ipynb** to train (select yolox_env as kernel) and understand how YOLOX works. Then, modify the file(s) to train with your custom dataset and model choice.