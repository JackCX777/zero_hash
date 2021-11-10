#  Zero#

The goal of this project is to create a real-time VWAP (volume-weighted average price) calculation engine
using he coinbase websocket feed to stream in trade executions and update the VWAP for each trading pair 
as updates become available.

The following technologies are used to implement the service:
- Python 3.9.7
- websocket-client 1.2.1

#### Note: 
I use websocket-client library because I couldn't figure out how to specify the wss protocol 
using the built-in python socket library


### Usage

#### Using docker-compose

- $ git clone https://github.com/JackCX777/zero_hash
- $ docker-compose -f docker-compose-dev.yml up --build -d
- Please wait about two minutes

#### As an alternative, you can use the console:

- $ git clone https://github.com/JackCX777/zero_hash
- Run the console from the root project folder
- Execute the following command: python ./zero_hash_socket_feed/main.py

### Additional

You can change the trading pairs in the PRODUCTS list and the size of the calculation window 
in the WINDOW_SIZE from /zero_hash_socket_feed/settings.py file if you wish.