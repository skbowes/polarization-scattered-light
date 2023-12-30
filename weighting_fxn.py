def weighted_fxn(w1, w2, f1, f2):
    """Computes the weighted combined function given two of the same kind of function
    for two different compositions."""
    weighted = (w1*f1 + w2*f2)/(w1+w2)
    return(weighted)
