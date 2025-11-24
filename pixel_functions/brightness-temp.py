import numpy as np
def bt_from_dn(in_ar, out_ar, xoff, yoff, xsize, ysize, *args, **kwargs):
    DN = in_ar[0].astype(np.float32)
    bad = (~np.isfinite(DN)) | (DN <= 0)
    good = ~bad
    L = ({{M_lambda}}) * DN + ({{A_lambda}})
    T = np.empty_like(DN, dtype=np.float32)
    T[good] = ({{K2}}) / np.log(({{K1}}) / L[good] + 1.0)
    T[~good] = np.nan
    out_ar[:] = T