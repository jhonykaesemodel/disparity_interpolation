import numpy as np
from numba import njit


# @njit
def nn_interpolation(disparity: np.ndarray) -> np.ndarray:
    height = disparity.shape[0]
    width = disparity.shape[1]

    for v in range(0, height):
        # init counter
        count = 0
        for u in range(0, width):
            # if disparity valid
            if disparity[v, u] >= 0:
                # at least one pixel requires interpolation
                if count >= 1:
                    # first and last value for interpolation
                    u1 = u - count
                    u2 = u - 1

                    # set pixel to min disparity
                    if u1 > 0 and u2 < width - 1:
                        d_ipol = min(disparity[v, u1 - 1], disparity[v, u2 + 1])
                        u_curr = u1
                        for u_curr in range(0, u2):
                            disparity[v, u_curr] = d_ipol
                        for u_curr in range(u1, u2):
                            disparity[v, u_curr] = d_ipol
                # reset counter
                count = 0
                # otherwise increment counter
            else:
                count += 1

        # extrapolate to the left
        for u in range(0, width):
            if disparity[v, u] >= 0:
                for u2 in range(0, u):
                    disparity[v, u2] = disparity[v, u]
                break

        # extrapolate to the right
        for u in range(width - 1, -1, -1):
            if disparity[v, u] >= 0:
                for u2 in range(u + 1, width):
                    disparity[v, u2] = disparity[v, u]
                break

    # for each column do
    for u in range(0, width):
        # extrapolate to the top
        for v in range(0, height):
            if disparity[v, u] >= 0:
                for v2 in range(0, v):
                    disparity[v2, u] = disparity[v, u]
                break

        # extrapolate to the bottom
        for v in range(height - 1, -1, -1):
            if disparity[v, u] >= 0:
                for v2 in range(v + 1, height):
                    disparity[v2, u] = disparity[v, u]
                break
    return disparity


if __name__ == "__main__":

    disparity = np.random.rand(4096, 4096)

    import time

    start = time.time()
    out = nn_interpolation(disparity)

    print(time.time() - start)
