import os
import os.path as osp

import numpy as np
from Cython.Build import cythonize
from setuptools import find_packages, setup
from setuptools.extension import Extension
import platform


include_dirs = [np.get_include()]
library_dirs = []

conda_fpath = os.environ.get("CONDA")
if platform.system() == "Windows":
    library_dirs += [osp.join(conda_fpath, "Library", "lib")]
    libraries = ["opencv_core452", "opencv_imgproc452"]
    opencv_fpath = osp.join(conda_fpath, "Library", "include")
elif platform.system() == "Linux":
    library_dirs += ["/usr/local/include/lib"]
    libraries = ["opencv_core", "opencv_imgproc"]
    opencv_fpath = "/usr/local/include/opencv4"
else:  # macos
    library_dirs += [osp.join(conda_fpath, "lib")]
    libraries = ["opencv_core", "opencv_imgproc"]
    opencv_fpath = osp.join(conda_fpath, "envs", "foo", "include", "opencv4")
include_dirs += [opencv_fpath]


def ext_modules():
    extensions = [
        Extension(
            name="disparity_interpolation",
            sources=["disparity_interpolation/disparity_interpolation.pyx"],
            include_dirs=include_dirs,
            libraries=libraries,
            library_dirs=library_dirs,
            language="c++",
            extra_compile_args=["-w", "-O3", "-std=c++11"],
        )
    ]
    return cythonize(extensions)


if __name__ == "__main__":
    with open("README.md", "r") as f:
        long_description = f.read()
    setup(
        name="disparity_interpolation",
        version="1.0.3",
        packages=find_packages(),
        author="Jhony Kaesemodel Pontes",
        description="Nearest neighbor interpolation for disparity images with missing parts.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jhonykaesemodel/disparity_interpolation",
        ext_modules=ext_modules(),
    )
