import scipy

def get_correlation_coeff(x,y):
    return  scipy.stats.pearsonr(x, y)