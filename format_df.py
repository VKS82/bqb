import pickle
import pandas as pd

df_fh = open('df_list.obj', 'rb')

df_list = pickle.load(df_fh)

for d in df_list:
    print(list(d))

#df = pd.concat(df_list, ignore_index=True)



