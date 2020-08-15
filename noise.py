import numpy as np


def noise(input):
    input = list(input)
    for i in range(len(input)):
        r = np.random.rand()
        if r < 0.1:
            if(input[i] == "1"):
                input[i] = "0"
            else:
                input[i] = "1"
    input = "".join(input)
    output = input
    return output
