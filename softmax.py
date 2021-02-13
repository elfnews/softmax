import numpy as np
import pandas as pd
from IPython.core.display import display


def softmax(L):
    print("Array:")
    display(L)
    expArray = np.exp(L)
    print("Exponentials of Array:")
    display(expArray)
    sum_exp = np.sum(expArray)
    print("Sum of exponentials:")
    display(sum_exp)
    result = []
    for e in expArray:
        display(e)
        sm = e / sum_exp
        result.append(sm)
    display(result)
    return result

if __name__ == '__main__':
    pd.options.display.max_columns = 200
    pd.options.display.max_colwidth = None
    pd.options.display.expand_frame_repr = False

    softmax([1,2,3,4,5,6])
