<div align="center"><img src="assets/logo.png" width="350"></div>

# YOLOX for Windows

Partially based on the implementation done in: https://github.com/Kazuhito00/YOLOX-Colaboratory-Training-Sample

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
### YOLOX Installation

First, clone this repo:

```bash
git clone https://github.com/ainhoaarnaiz/YOLOX_for_Windows.git
cd YOLOX_for_Windows
```

Next, check environment.yml and make sure you use the correct URL index for your CUDA version. Then run:

```bash
conda env create -f environment.yml
conda activate yolox_env
```

Then, install yolox 0.3.0 but skip its (old) dependency pins:

```bash
pip install yolox==0.3.0 --no-deps
```

---

## Usage

Follow the steps on the **01_YOLOX_training_simplified.ipynb** to train (select yolox_env as kernel) and understand how YOLOX works with the given fish dataset. Then, modify the files to train with your custom dataset and your model choice.

**IMPORTANT**: Look for this line `local_cache = r"C:\Users\aarnaizl\AppData\Local\torch_extensions"` in all the .ipynb and change it with your local cache directory.