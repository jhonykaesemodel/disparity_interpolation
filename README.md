[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Linux CI](https://github.com/jhonykaesemodel/disparity_interpolation/actions/workflows/github-deploy.yml/badge.svg)

## Fast nearest-neighbor interpolation of disparity maps using Cython

Some stereo matching methods such as [Semi-Global Matching (SGM)](https://core.ac.uk/download/pdf/11134866.pdf) might provide sparse disparity maps, meaning that some pixels will not have valid disparity values. In those cases, an interpolation of the predicted disparity map might be needed for evaluation against semi-dense ground-truth, as in the [KITTI Stereo 2015 benchmark](http://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=stereo).

**Usage example:**
```python
import disparity_interpolation


def interpolate_disparity(disparity_map: np.array) -> np.array:
    """Intepolate disparity image to inpaint holes.
       The expected run time for a stereo image with 2056 × 2464 pixels is ~50 ms.
    """
    # Set the invalid disparity values defined as "0" to -1.
    disparity_map[disparity_map == 0] = -1
    disparity_map_interp = disparity_interpolation.disparity_interpolator(disparity_map)

    return disparity_map_interp
```
