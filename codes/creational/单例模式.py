class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

import threading
class SingletonMultiThread:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonMultiThread,cls).__new__(cls)
        return cls._instance

class MyClassMultiThread(SingletonMultiThread):
    def __init__(self, name):
        self.name = name
    
    def do(self):
        print(self, self.name)
    
if __name__ == '__main__':
    a = MyClass('aa')
    print(a)  # aa
    b = MyClass('bb')
    print(a, b)  ## bb bb

    obj1 = MyClassMultiThread("thread1")
    obj2 = MyClassMultiThread("thread2")
    print(obj1,obj2)

    def task(name):
        obj = MyClassMultiThread(name)
        obj.do()

    for i in range(10):
        t = threading.Thread(target=task,args=[str(i),])
        t.start()

