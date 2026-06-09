import pandas as pd
with open("C:/Users/vinde/task_6_0/percentiles_lenght.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/vinde/Downloads/wild_boars.csv")
    q1 = df.groupby('gender')['length_cm'].quantile(0.25)
    q3 = df.groupby('gender')['length_cm'].quantile(0.75)
    print("IQR:", file=f)
    print(q3-q1, file=f)