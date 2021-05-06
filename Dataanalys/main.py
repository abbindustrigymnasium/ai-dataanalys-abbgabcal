import pandas as pd
import matplotlib.pyplot as plt

def processData(df, framesize=(2,3)):
    last_time = 0
    n_cycle = 1
    last_peak = 0
    res_dict = {'start_time': [], 'length': [], 'n_cycle': [], 'peak': []
    , 'type': []
    }
    for index, row in df.iterrows():
        var = df.iloc[index-framesize[0]:index+framesize[1]]
        try:
            if var['Avg2'].max() == var['Avg2'].iloc[2]:
                res_dict['start_time'].append(df.iloc[index]['unix_time'])
                res_dict['length'].append(df.iloc[index]['unix_time'] - last_time)
                res_dict['n_cycle'].append(n_cycle)
                res_dict['peak'].append(df.iloc[index]['Avg2'])


                peak_cycle = df.iloc[last_peak:index]
                if peak_cycle['y'].min() < 0:
                    res_dict['type'].append("runstride")
                else:
                    res_dict['type'].append("walkstride")

                last_time = df.iloc[index]['unix_time']
                n_cycle += 1
                last_peak = index
        except:
            break
    del res_dict['peak']
    return res_dict

raw_data = pd.read_csv("rawdata119870.csv", sep=",")
process_data = {'unix_time': raw_data['unix_time'].to_list(), 'y': raw_data["y"].to_list()}
process_data = pd.DataFrame(process_data)
process_data["Avg1"] = process_data["y"].rolling(window=7, center=True).mean()
process_data["Avg2"] = process_data["Avg1"].rolling(window=7, center=True).mean()
process_data = process_data.dropna()

res_dict = processData(process_data)

final_data = pd.DataFrame(res_dict)
final_data.to_csv("Final_data.csv", index=False)

graph = plt.gca()
process_data.plot(kind='line', x='unix_time', y='y', ax=graph)
process_data.plot(kind='line', x='unix_time', y='Avg2', ax=graph)

plt.show()
