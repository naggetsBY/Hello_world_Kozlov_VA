import pandas as pd
with open("C:/Users/vinde/task_6_0/percentiles.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/vinde/Downloads/wild_boars.csv")
    names = list(df.columns)
    for i in names[2:]:
        average =  df[i].mean()
        l = i.split('_')
        if len(l) == 2:
            param = l[0] 
        else:
            param = l[0] + ' ' + l[1]
        print(f'{param.capitalize()}:', file=f)
        print(f"Percentile 25 (Q1):\t{df[i].quantile(0.25):.1f} {l[-1]}", file=f)
        print(f"Median 50 (Q2):\t{df[i].quantile(0.50):.1f} {l[-1]}", file=f)
        print(f"Percentile 75 (Q3):\t{df[i].quantile(0.75):.1f} {l[-1]}", file=f)
        print(f"Percentile 90:\t{df[i].quantile(0.90):.1f} {l[-1]}", file=f)
        print(f"Percentile 95:\t{df[i].quantile(0.95):.1f} {l[-1]}", file=f)
        print(f"Max:\t{df[i].quantile(1.00):.1f} {l[-1]}\n", file=f)