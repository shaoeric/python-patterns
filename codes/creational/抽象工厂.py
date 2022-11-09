from abc import ABCMeta, abstractmethod

# 抽象产品
class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# 具体产品
class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")

class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")

class Android(OS):
    def show_os(self):
        print("安卓系统")

class IOS(OS):
    def show_os(self):
        print("IOS系统")



# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# 具体工厂
class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

class AppleFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

# 客户端
if __name__ == '__main__':
    class Phone:
        def __init__(self, cpu: CPU, os: OS):
            self.cpu = cpu
            self.os = os
        
        def show_info(self):
            self.cpu.show_cpu()
            self.os.show_os()

    def make_phone(factory: PhoneFactory):
        cpu = factory.make_cpu()
        os = factory.make_os()
        return Phone(cpu, os)

    phone = make_phone(AppleFactory())
    phone.show_info()