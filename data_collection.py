#pip install yfinance
import yfinance as yf

#starting_confirmation = input("Type 1 if you want to scrape till date and Type 2 if you want to scrape selective dates before the last 30 days :")

def num_check():
    starting_confirmation = input("Type 1 if you want to scrape till date or Type 2 if you want to scrape selective dates within the last 30 days :")
    if starting_confirmation == '1' or starting_confirmation == '2':
        if starting_confirmation == '1':
            stock_name = input ("Enter stock name :")
            period_select = input ("Enter the period to scrape. (Supported : 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max) : ")
            data = yf.download([stock_name], period = period_select) 
            data = data.reset_index()
            print(data)

        elif starting_confirmation == '2':
            stock_name = input ("Enter stock name :").upper()
            start = input ("Enter start date (YYYY-MM-DD):")
            end = input("Enter end date (YYYY-MM-DD): ")
            data = yf.download(stock_name, start, end)
            data = data.reset_index()
            print(data)
    else:
        num_check()   

num_check()



