import numpy as np
import scipy.stats as sps

def ksi_criteria(values,left_value,right_value,interval_count):
    values_in_interval=[]
    intervals_edges = np.linspace(left_value,right_value,interval_count)
    sorted_values= sorted(values)
    values_index = 0
    for edge in intervals_edges[1:]:
        values_count= 0
        while values_index < len(values) and sorted_values[values_index]< edge:
            values_count+=1
            values_index+=1
        values_in_interval.append(values_count)
    freq = [val/len(values) for val in values_in_interval]
    return freq,intervals_edges

def check_if_equal_distributed(freq):
    return sps.chisquare(freq).p

def check_if_distributed_with(freq,cdf):
    return sps.kstest(freq,'uniform').p





