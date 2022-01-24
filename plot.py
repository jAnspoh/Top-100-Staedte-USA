import matplotlib.pyplot as plt

COLOR = "cornflowerblue"

def to_float(string):
    nums = []
    for num in string:
        if type(num) is int: return string
        nums.append(float(num.replace("\xa0" ,"")))
    return nums

def count_bool(arr):
    true ,false = 0 ,0
    for b in arr:
        if b: true += 1
        else: false += 1
    return true ,false

def plot(X ,Y ,title ,num=5 ,top=False):
    X ,Y ,names = list(X) ,to_float(list(Y)) ,[]
    sorted_data = sorted(Y ,reverse=top)
    for n in sorted_data[:num]:
        names.append(X[Y.index(n)])
    plt.figure(figsize=(10,5))
    if top:
        plt.bar(names ,sorted_data[:num] ,color=COLOR)
    else:
        plt.bar(names ,sorted_data[:num] ,color=COLOR)
    plt.title(title ,fontsize=15)
    plt.show()

def plot_bool(X ,Y ,title):
    X ,Y = list(X) ,list(Y)
    true ,false = count_bool(Y)
    plt.figure(figsize=(10,5))
    plt.bar(X ,[true ,false] ,color=COLOR)
    plt.title(title ,fontsize=15)
    plt.show()


