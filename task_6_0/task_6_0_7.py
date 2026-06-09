import pandas as pd
with open("C:/Users/vinde/task_6_0/variations.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/vinde/Downloads/wild_boars.csv")
    names = list(df.columns)
    for i in names[2:]:
        variance =  df[i].var()
        std = df[i].std()
        cv = (std / df[i].mean()) * 100
        l = i.split('_')
        if len(l) == 2:
            param = l[0] 
        else:
            param = l[0] + ' ' + l[1]
        print(f'{param.capitalize()} variance is {variance:.2f} {l[-1]}²', file=f)
        print(f'{param.capitalize()} standart deviation is {std:.2f} {l[-1]}', file=f)
        print(f'{param.capitalize()} coefficient of variation is {cv:.2f}\n', file=f)