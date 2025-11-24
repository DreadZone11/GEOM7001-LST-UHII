import numpy as np
def ndwi(in_ar, out_ar, xoff, yoff, xsize, ysize, raster_xsize, raster_ysize, buf_radius, gt, **kwargs):
    nir = in_ar[0].astype('float32', copy=False)
    green = in_ar[1].astype('float32', copy=False)

    # clamp to sensible SR range
    nir = np.where(np.isfinite(nir), np.clip(nir, 0, 1.0), np.nan)
    green = np.where(np.isfinite(green), np.clip(green, 0, 1.0), np.nan)

    num = green - nir
    den = green + nir

    eps = 1e-6  # Guard against miniscule values ~0
    out = np.full_like(nir, np.nan, dtype='float32')
    good = np.isfinite(num) & np.isfinite(den) & (np.abs(den) > eps)
    out[good] = num[good] / den[good]
    out_ar[:] = out