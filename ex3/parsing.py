import pandas as pd


logfile = "ex3_1a_corrida_SHVM.log"
df = pd.read_csv(logfile,
            sep=';',
            encoding="utf-8-sig",
            engine='python',
#            index_col='Hora',
            parse_dates=[0,3],
            header=0,
            names=['Hora', 'Super-Heroi', 'Volta', 'Tempo', "Media"])
df[['Codigo','Heroi']] = df['Super-Heroi'].str.split("–",expand=True)
del df['Super-Heroi']
print(df.columns)
print(type(df['Volta'][0]))
print(type(df['Media'][0]))
print(type(df['Codigo'][0]))
print(type(df['Hora'][0]))
print(type(df['Tempo'][0]))
print(df)

