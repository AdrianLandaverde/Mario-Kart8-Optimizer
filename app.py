import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello_world():
    return {'message':'Hello World'}

@app.get("/combinations")
async def get_combiantion(WG: int= None, AC: int= None, ON: int= None, OF: int= None, MT: int= None, SL: int= None, SW: int= None, SA: int= None, SG: int= None, TL: int= None, TW: int= None, TA: int= None, TG: int= None, IV: int= None):
    def euclidean_distance(row_values, dictionary_values):
        common_columns = set(row_values.index) & set(dictionary_values.keys())
        
        row_array = np.array([row_values[column] for column in common_columns])
        dict_array = np.array([dictionary_values[column] for column in common_columns])
        
        return np.linalg.norm(row_array - dict_array)
    
    dictionary_values= {'WG': WG, 'AC': AC, 'ON': ON, 'OF': OF, 'MT': MT, 'SL': SL, 'SW': SW, 'SA': SA, 'SG': SG, 'TL': TL, 'TW': TW, 'TA': TA, 'TG': TG, 'IV': IV}
    dictionary_values= {k: v for k, v in dictionary_values.items() if v is not None}

    df_karts_id= pd.read_csv('data/kart_id.csv', index_col=0)
    df_drivers_id= pd.read_csv('data/driver_id.csv', index_col=0)
    df_tires_id= pd.read_csv('data/tire_id.csv', index_col=0)
    df_gliders_id= pd.read_csv('data/glider_id.csv', index_col=0)
    df_combinations= pd.read_csv('data/all_unique_combinations.csv', index_col=0)
    df_combinations[["driver", "kart", "tire", "glider"]]= df_combinations[["driver", "kart", "tire", "glider"]].astype(str)

    df_combinations['EuclideanDistance'] = df_combinations.apply(lambda row: euclidean_distance(row, dictionary_values), axis=1)
    df_combinations['Score']= 100- round((df_combinations['EuclideanDistance']**2/df_combinations['EuclideanDistance'].max()**2)*100,2)

    results= {}
    for i in range(1):
        best= df_combinations.sort_values(by=["EuclideanDistance", "Total"], ascending=[True, False]).iloc[i]
        best_driver= df_drivers_id.loc[int(best["driver"])]
        best_kart= df_karts_id.loc[int(best["kart"])]
        best_tires= df_tires_id.loc[int(best["tire"])]
        best_glider= df_gliders_id.loc[int(best["glider"])]
        results[i]= {
        'Driver Name': list(pd.Series(best_driver["Driver"])), 'Driver Image': list(pd.Series(best_driver["Image"])),
        'Kart Name': list(pd.Series(best_kart["Body"])), 'Kart Image': list(pd.Series(best_kart["Image"])),
        'Tires Name': list(pd.Series(best_tires["Tire"])), 'Tires Image': list(pd.Series(best_tires["Image"])),
        'Glider Name': list(pd.Series(best_glider["Glider"])), 'Glider Image': list(pd.Series(best_glider["Image"])),
        'WG': int(best["WG"]), 'AC': int(best["AC"]), 'ON': int(best["ON"]), 'OF': int(best["OF"]), 'MT': int(best["MT"]), 
        'SL': int(best["SL"]), 'SW': int(best["SW"]), 'SA': int(best["SA"]), 'SG': int(best["SG"]), 
        'TL': int(best["TL"]), 'TW': int(best["TW"]), 'TA': int(best["TA"]), 'TG': int(best["TG"]), 
        'IV': int(best["IV"]), 'Score': int(best["Score"])}

    return results

