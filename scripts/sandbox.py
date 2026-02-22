



# TESTING
funds = ms.Funds("VTSAX")

print(funds.name)

holdings = funds.holdings()

holdings

end_date = datetime.datetime.today()
start_date = end_date - datetime.timedelta(days=10)
funds.nav(start_date,end_date)

funds.isin

funds.allocationWeighting()

funds.allocationMap()

funds.analystRating()

funds.dataPoint(field=["distributionYield"])

funds.equityStyle()

funds.investmentFee()

funds.investmentStrategy()

funds.marketCapitalization()



    





