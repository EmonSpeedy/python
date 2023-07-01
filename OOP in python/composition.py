# Inheritance provides "is a" relationships
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, memory) -> None:
        self.memory = memory

class SSD:
    def __init__(self, storage) -> None:
        self.storage = storage

# computer has a ram, storage, cpu 
# So, composition is a "has a" relationships
class Computer:
    def __init__(self, cores, ram, ssd) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram)
        self.ssd = SSD(ssd)

personal = Computer(4, 8, 256)
print(personal.cpu.cores)