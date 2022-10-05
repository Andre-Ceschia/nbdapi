# nbdapi
nbdapi is an open source python library that acts as a API wrapper for National Bank Dirtect Brokerage.

## Installation
    pip install nbdapi

## Functions
nbdapi can be used to place both limit and market orders, cancel orders, retrieve account balance, order information, position information (including unrealized gains and losses), real-time quotes and more.

## Example Usage
    from nbapi import NationalBank
    
    ticker = 'SU'
    market = 'USA'
    account_currency = 'USD'
    account_type = 'cash'
    phone = '000-000-0000'
    
    nb = NationalBank('username', 'password')
    
    account_id = nb.get_account_id(account_currency, account_type)
    
    buying_power = nb.get_account_balance(account_id)
    
    ask_price = nb.get_quote(ticker, market)['ask']
    
    if ask_price < 30:
        shares = buying_power // ask_price
        nb.place_market_order(ticker, account_id, account_currency, 'BUY', shares, phone)
        
        print(nb.get_positions(account_id)
    else:
        print('Price too high')
