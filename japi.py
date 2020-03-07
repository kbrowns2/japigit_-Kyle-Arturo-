import urllib.request
import json





KEY = '&apikey=SL6R9AFDVWIEPKEC'
FUNCTION = 'function=GLOBAL_QUOTE&'
x = 0




def getStockData(func, stock_symbol, key):
    full_url = 'https://www.alphavantage.co/query?'

    connection = urllib.request.urlopen(full_url + func + stock_symbol + key)

    response = connection.read().decode()

    print(response)

    x = json.loads(response)

    return x['Global Quote']['05. price']







def main():
    f = open("japi", "w+")
    while x != 1:
     user_entry = input("Please enter the desired stock symbol to recieve quote")

     stock_symbol = 'stock_symbol=' + user_entry

     if stock_symbol == 'stock_symbol=quit':
         break
    else:
        f.write("Your selected stock {} has a price of: ${:.2f}\r\n".format(user_entry, float(getStockData(FUNCTION, stock_symbol, KEY))))

    f.close()
    f = open("japi.out", "r")
    contents = f.read()
    print(contents)


print("Sucess! Your Stock quote was acccessed.")
(main)
