import pandas as pd


logfile = "ex3_1a_corrida_SHVM.log"
df = pd.read_csv(logfile,
                 sep=';',
                 encoding="utf-8-sig",
                 engine='python',
                 parse_dates=[0, 3],
                 header=0,
                 names=['Hora', 'Super-Heroi', 'Volta', 'Tempo', "Media"])
df[['Codigo', 'Heroi']] = df['Super-Heroi'].str.split("–", expand=True)
del df['Super-Heroi']
