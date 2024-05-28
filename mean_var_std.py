import numpy as np 

def calculate(lst):

    if len(lst) != 9:
        raise valueError("List must contain nine numbers.")
    anp = np.array(lst).reshape(3,3)

    meanlist = [0] * 2
    varlist = [0] * 2
    stdlist = [0] * 2
    maxlist = [0] * 2
    minlist = [0] * 2
    sumlist = [0] * 2
    for i in range(2):
        meanlist[i] = anp.mean(axis=i).tolist()
        varlist[i] = anp.var(axis=i).tolist()
        stdlist[i]  = anp.std(axis=i).tolist()
        maxlist[i] = anp.max(axis=i).tolist()
        minlist[i] = anp.min(axis=i).tolist()
        sumlist[i] = anp.sum(axis=i).tolist()
        
    meanlist.append(anp.flatten().mean())
    varlist.append(anp.flatten().var())
    stdlist.append(anp.flatten().std())
    maxlist.append(anp.flatten().max())
    minlist.append(anp.flatten().min())
    sumlist.append(anp.flatten().sum())
    
    final_dict = {}
    final_dict['mean'] = meanlist
    final_dict['standard deviation'] = stdlist
    final_dict['variance'] = varlist
    final_dict['max'] = maxlist
    final_dict['min'] = minlist
    final_dict['sum'] = sumlist
    
    return final_dict