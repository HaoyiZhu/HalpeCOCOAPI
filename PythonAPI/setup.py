from setuptools import setup, Extension
import numpy as np
import Cython.Build

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext && python -m pip install ./"

ext_modules = [
    Extension(
        'halpecocotools._mask',
        sources=['common/maskApi.c', 'halpecocotools/_mask.pyx'],
        include_dirs = [np.get_include(), 'common'],
        extra_compile_args=[],
    )
]

setup(
    packages = ['halpecocotools'],
    package_dir = {'halpecocotools': 'halpecocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0',
    ],
    description="COCO API for Halpe-Fullbody dataset",
    url="https://github.com/HaoyiZhu/HalpeCOCOAPI",
    ext_modules = Cython.Build.cythonize(ext_modules)
)
