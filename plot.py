import matplotlib.pyplot as plt

def to_float(string):
    nums = []
    for num in string:
        if type(num) is int: return string
        nums.append(float(num.replace("\xa0" ,"")))
    return nums

def plot(X ,Y ,title ,num=5 ,top=False):
    X ,Y ,names = list(X) ,to_float(list(Y)) ,[]
    sorted_data = sorted(Y ,reverse=top)
    for n in sorted_data[:num]:
        names.append(X[Y.index(n)])
    plt.figure(figsize=(10,5))
    if top: 
        plt.bar(names ,sorted_data[:num] ,color="green")
    else: 
        plt.bar(names ,sorted_data[:num] ,color="green")
    plt.title(title ,fontsize=15)
    plt.show()
