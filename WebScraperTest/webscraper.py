from get_all_tickers.get_tickers as
# tickers of all exchanges
tickers = gt()
print(tickers[:5])

# tickers from NYSE and NASDAQ only
tickers = get_tickers(AMEX=False)

# default filename is tickers.csv, to specify, add argument filename='yourfilename.csv'
save_tickers()

# save tickers from NYSE and AMEX only
save_tickers(NASDAQ=False)

# get tickers from Asia
tickers_asia = get_tickers_by_region(Region.ASIA)
print(tickers_asia[:5])

# save tickers from Europe
save_tickers_by_region(Region.EUROPE, filename='EU_tickers.csv')

# get tickers filtered by market cap (in millions)
filtered_tickers = get_tickers_filtered(mktcap_min=500, mktcap_max=2000)
print(filtered_tickers[:5])

# not setting max will get stocks with $2000 million market cap and up.
filtered_tickers = get_tickers_filtered(mktcap_min=2000)
print(filtered_tickers[:5])

# get tickers filtered by sector
filtered_by_sector = get_tickers_filtered(mktcap_min=200e3, sectors=SectorConstants.FINANCE)
print(filtered_by_sector[:5])

# get tickers of 5 largest companies by market cap (specify sectors=SECTOR)
top_5 = get_biggest_n_tickers(5)
print(top_5)