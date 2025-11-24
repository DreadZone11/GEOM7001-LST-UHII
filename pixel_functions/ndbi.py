import numpy as np
def ndbi(in_ar, out_ar, xoff, yoff, xsize, ysize, raster_xsize, raster_ysize, buf_radius, gt, **kwargs):
    nir = in_ar[0].astype('float32', copy=False)
    swir1 = in_ar[1].astype('float32', copy=False)

    # clamp to sensible SR range
    nir = np.where(np.isfinite(nir), np.clip(nir, 0, 1.0), np.nan)
    swir1 = np.where(np.isfinite(swir1), np.clip(swir1, 0, 1.0), np.nan)

    num = swir1 - nir
    den = swir1 + nir

    eps = 1e-6  # Guard against miniscule values ~0
    out = np.full_like(nir, np.nan, dtype='float32')
    good = np.isfinite(num) & np.isfinite(den) & (np.abs(den) > eps)
    out[good] = num[good] / den[good]
    out_ar[:] = out