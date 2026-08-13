from abc import ABC, abstractmethod
class LegacyPrinter:
    def legacy_print(self):
        print("printing from legacy printer")


class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


class AdapterPrinter(Printer):
    def __init__(self):
        self.printer = LegacyPrinter()

    def print(self):
        self.printer.legacy_print()

def client_code(printer: AdapterPrinter):
    printer.print()


adapter_printer = AdapterPrinter()
client_code(adapter_printer)