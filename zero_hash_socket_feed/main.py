from settings import *
from websocket_handlers import SocketClient
from calculation_handlers import CalculationEngine
from dispatch_handlers import ResultDispatcher


if __name__ == '__main__':
    client = SocketClient(HOST, SUBSCRIBE_MSG)  # Define the websocket client
    data_generator = client.subscription_generator()  # Define the received from websocket feed data generator object
    calc_engine = CalculationEngine(PRODUCTS, CALC_TYPE, CALC_SETTINGS, data_generator)  # Define the calculation engine
    calc_generator = calc_engine.run_calc_loop()  # Define the calculated data generator object
    result_dispatcher = ResultDispatcher(calc_generator, PRODUCTS, WINDOW_SIZE, CALC_TYPE)  # The results dispatcher
    result_dispatcher.to_stdout()  # Define the dispatch method
