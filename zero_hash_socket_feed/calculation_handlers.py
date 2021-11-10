import typing
from time import strftime


class CalculationEngine:
    """
    This class provides the required calculations.
    """
    def __init__(self, products: list, calc_type: str, calc_settings: dict, generator: typing.Generator) -> None:
        """
        :param products: The list of trading pairs.
        :param calc_type: The required calculation type, VWAP e.g.
        :param calc_settings: The python dict that contains required calculation parameters,
        calculation window size e.g.
        :param generator: The python generator object that generates the data for the calculation.
        """
        self.calc_result = {}  # Define the result structure
        self.calc_type = calc_type
        try:
            self.calc_settings = calc_settings[self.calc_type]
        except KeyError as e:
            print(f'{str(e)}. Inappropriate calculation option!')

        # Define the calculation data structure
        self.temp_data = {}
        for prod in products:
            self.temp_data[prod] = {'price': [], 'size': [], 'time': []}
        self.generator = generator

    def collect_temp_data(self, max_size: int) -> None:
        """
        Collects data from generator to self.temp_data.
        :param max_size: The size of calculation window.
        :return: None
        """
        try:
            new_data = next(self.generator)

            product_id = new_data.get('product_id')

            price = self.temp_data[product_id]['price']
            price.append(new_data.get('price'))
            price = price[-max_size:]
            self.temp_data[product_id]['price'] = price

            size = self.temp_data[product_id]['size']
            size.append(new_data.get('size'))
            size = size[-max_size:]
            self.temp_data[product_id]['size'] = size

            time = self.temp_data[product_id]['time']
            time.append(new_data.get('time'))
            time = time[-max_size:]
            self.temp_data[product_id]['time'] = time
        except StopIteration as e:
            print(f'{str(e)}. Failed attempt to collect new data!')

    def last_points_vwap(self) -> dict:
        """
        Calls self.collect_temp_data method and do the required VWAP calculations.
        :return: Calculation result.
        """
        self.collect_temp_data(self.calc_settings.get('calc_size'))

        for key, value in self.temp_data.items():
            price = value.get('price')
            size = value.get('size')
            points_count = len(price)

            if price and size:
                price = [float(i) for i in price]
                size = [float(i) for i in size]
                total_price = 0
                for i in range(points_count):
                    total_price += float(price[i]) * float(size[i])
                vwap = total_price / sum(size)
                self.calc_result[key] = {self.calc_type: vwap}
            else:
                self.calc_result[key] = {self.calc_type: None}

            timestamp = strftime('%m-%d-%Y, %H:%M:%S')
            self.calc_result[key]['points_count'] = points_count
            self.calc_result[key]['timestamp'] = timestamp
        return self.calc_result

    def run_calc_loop(self) -> typing.Generator[dict, None, None]:
        """
        Calls required calculation type and provides continuity of calculation
        :return: Generator object.
        """
        calc_options = {'VWAP': {'last_points_vwap': self.last_points_vwap}}
        current_calc_option = calc_options.get(self.calc_type).get(self.calc_settings.get('calc_variant'))
        while True:
            yield current_calc_option()
