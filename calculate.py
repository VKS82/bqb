import pickle
import pandas as pd

df_fh = open('df_list.obj', 'rb')

df_list = pickle.load(df_fh)

print(df_list.to_string())



#df = pd.concat(df_list, ignore_index=True)



