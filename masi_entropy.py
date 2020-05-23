import numpy as np
def masi_entropy(thresholds,prob):
    r=-1
    thresholds.sort()
    classes = len(thresholds) + 1
    count = 0
    w = {}
    output = {}

    for threshold in thresholds:
        w0 = np.sum(prob[:threshold])
        w["w"+str(count)] = w0
        out = 0
        if w0 > 0:
            for j in range(1,threshold):
                if prob[j]> 0:
                    out+= (prob[j]/w["w"+str(count)]) * np.log(prob[i]/w["w"+str(count)])
            output["out"+str(count)] = out
        count+=1


    src = {}
    for i in range(0,classes):
        src["class"+str(i)] = (1/(1-r))* np.log(1-(1-r)) * output["out"+str(i)])/(1-r)

    src_classes = src.values()
    src_total = 0
    for src_values in src_classes:
        src_total+= src_values
