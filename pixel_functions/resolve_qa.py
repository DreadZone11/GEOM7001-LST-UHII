# Options

import numpy as np

def bit_reader(arr, k, two_bit = False):
    if not two_bit:
        return (arr >> k) & 1
    return (arr >> k) & 0b11

def valid_mask(out_ar, in_ars, xoff, yoff, xsize, ysize, raster_xsize, raster_ysize, gt, **kwargs):
    qpix = in_ars[0].astype(np.uint16)
    qrad = in_ars[1].astype(np.uint16)

    fill = bit_reader(qpix, 0)
    dcloud = bit_reader(qpix, 1)
    cirrus = bit_reader(qpix, 2)
    cloud = bit_reader(qpix, 3)
    shadow = bit_reader(qpix, 4)
    snow = bit_reader(qpix, 5)

    terrain_occlusion = bit_reader(qrad, 11)

    cloud_conf = bit_reader(qpix, 8, two_bit=True)
    cloud_shadow_conf = bit_reader(qpix, 10, two_bit=True)
    snow_conf = bit_reader(qpix, 12, two_bit=True)
    cirrus_conf = bit_reader(qpix, 14, two_bit=True)

    valid = (
        (fill == 0) &
        (dcloud == 0) &
        (cloud == 0) &
        (shadow == 0) &
        (cirrus == 0) &
        (snow == 0) &
        (cloud_conf <= 1) &
        (cloud_shadow_conf <= 1) &
        (snow_conf <= 1) &
        (cirrus_conf <= 1) &
        (terrain_occlusion == 0)
    )

    out_ar[:] = np.where(valid, 255, 0).astype(np.uint8)
