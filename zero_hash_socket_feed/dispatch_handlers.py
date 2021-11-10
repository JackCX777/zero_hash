import typing


class ResultDispatcher:
    """
    This man turns the completed results into the right format and provides a sending it to the receivers.
    """
    def __init__(self, generator: typing.Generator, products: list, data_range: int, calc_type: str) -> None:
        """
        :param generator: Python generator object that generates calculated data.
        :param products: The list of trading pairs.
        :param data_range: The size of calculation window.
        :param calc_type: The required calculation type, VWAP e.g.
        """
        self.generator = generator
        self.products = products
        self.range = data_range
        self.calc_type = calc_type
        self.points_count_key = 'points_count'
        self.timestamp_key = 'timestamp'

    def to_stdout(self) -> None:
        """
        Implements the data sending to stdout.
        :return: None
        """
        for item in self.generator:
            for product in self.products:
                result = item.get(product)
                stdout_str = f'Trading pair: {product},  ' \
                             f'Last {self.range} points VWAP: {result.get(self.calc_type)},  ' \
                             f'Points count: {result.get(self.points_count_key)},  ' \
                             f'Timestamp: {result.get(self.timestamp_key)}'
                print(stdout_str)
