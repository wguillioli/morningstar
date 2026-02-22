import datetime
import mstarpy as ms
import pandas as pd

#funds_to_parse = ['VTSAX', 'VEMAX', 'CNDX']
funds_to_parse = ['VTSAX', 'VEMAX', 'LU0951559797', 'VTMGX', 'FXAIX', 'VFIAX']

results_list = []

for item in funds_to_parse:
    print(item)

    funds = ms.Funds(item)

    data_points = funds.dataPoint(field=["distributionYield", "alpha", "fundSize", "beta", "rSquared"])

    dat_fund = {
        "symbol" : item,
        "isin" : funds.isin,
        "name" : funds.name,
        "investmentStrategy" : funds.investmentStrategy()['investmentStrategy'],
        "distributionYield" : data_points['distributionYield']['value'],
        "alpha" : data_points['alpha']['value'],
        "beta" : data_points['beta']['value'],
        "rSquared" : data_points['rSquared']['value'],
        "fundSize" : data_points['fundSize']['value'],
    }
    results_list.append(dat_fund)

# convert list to df
df = pd.DataFrame(results_list)
print(df)

df.to_csv('C:\MisLocalFiles\Github\morningstar\data.csv', index=False)
