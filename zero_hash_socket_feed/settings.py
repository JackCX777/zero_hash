PRODUCTS = ['BTC-USD', 'ETH-USD', 'ETH-BTC']
WINDOW_SIZE = 200
CHANNELS = ['matches']
CALC_TYPE = 'VWAP'
CALC_VARIANT = 'last_points_vwap'
CALC_SETTINGS = {CALC_TYPE: {'calc_variant': CALC_VARIANT, 'calc_size': WINDOW_SIZE}}

SUBSCRIBE_MSG = {'type': 'subscribe', 'product_ids': PRODUCTS, 'channels': CHANNELS}
# HOST = 'wss://ws-feed.pro.coinbase.com'
HOST = 'wss://ws-feed.exchange.coinbase.com'
