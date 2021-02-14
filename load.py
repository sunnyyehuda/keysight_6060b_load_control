class load_const(Enum):
    def mode():
        CC = 'CURR'
        CV = 'VOLT'
        CR = 'RES'

class Load:
    """
    class for the keysight 6060b load control
    """
    def __init__(self, gpib_address):
        self.gpib_address = gpib_address
        rm = pyvisa.ResourceManager()
        self.load = rm.open_resource(f'GPIB0::{gpib_address}::INSTR')

    def __del__(self):
        self.load.close()

    def input_on_off(self, on_off):
        """

        :param on_off: ON or OFF
        :return:
        """
        self.load.write(f'INPUT {on_off}')

    def frequency(self, freq):
        """
        The Function sets frequency.
        :param freq:The frequency can be set from 0.25 to 10000 Hz
        :return:
        """
        self.load.write(f'TRAN:FREQ {freq}')

    def tran_operation(self):
        self.load.write('TRAN:MODE CONT')

    def duty_cycle(self,duty_cycle):
        """
        The Function sets duty cycle.
        :param percent: The duty cycle can be set from 3% to 97% (0.25 Hz to 1 kHz)
        or from 6% to 94% (above 1kHz) at the front pane
        """
        self.load.write(f'TRAN:DCYC {duty_cycle}')

    def meas(self, mode):
        self.load.write(f'MEAS:{mode}')

    def short_on_off(self, on_off):
        self.load.write(f'INPUT:SHORT {on_off}')

    def mode(self, mode):
        self.load.write(f'MODE {mode}')

    def range(self,mode, range):
        self.load.write(f'{mode}:RANG {range}')

    def trig_cc_level(self, mode):
        self.load.write(f'{mode}:TRIG')

    def tran_cc_level(self, mode, level):
        self.load.write(f'{mode}:TLEV {level}')

    def limit(self, mode, percent):
        self.load.write(f'{mode}:PORT {percent}')

    def slew_rate(self, mode, range):
        self.load.write(f'{mode}:SLEW {range}')
