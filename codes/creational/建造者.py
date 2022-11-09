from abc import ABCMeta, abstractmethod

# Product
class Phone:
    def __init__(self, shell=None, cpu=None, memory=None, os=None) -> None:
        self.shell = shell
        self.cpu = cpu
        self.memory = memory
        self.os = os
    
    def __str__(self) -> str:
        return f'{self.shell}, {self.cpu}, {self.memory}, {self.os}'

# Abstract Builder
class PhoneBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_shell(self):
        pass
    
    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_os(self):
        pass


# Concrete Builder
class MiPhoneBuilder(PhoneBuilder):
    def __init__(self) -> None:
        self.phone = Phone()

    def build_shell(self):
        self.phone.shell = 'mi shell'
        return self

    def build_cpu(self):
        self.phone.cpu = 'snap dragon'
        return self

    def build_memory(self):
        self.phone.memory = 'mi memory'
        return self
    
    def build_os(self):
        self.phone.os = 'android'
        return self

    def get_phone(self):
        return self.phone

# Director
class Director:
    def __init__(self, builder: PhoneBuilder) -> None:
        self.builder = builder

    def direct(self):
        builder = self.builder.build_shell().build_cpu().build_memory().build_os()
        phone = builder.get_phone()
        return phone

# client
if __name__ == '__main__':
    mi_builder = MiPhoneBuilder()
    mi_phone = Director(mi_builder).direct()
    print(mi_phone)