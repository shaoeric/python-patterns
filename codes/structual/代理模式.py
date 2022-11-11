from abc import ABCMeta, abstractmethod

# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

# 具体实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print('读取文件内容！')
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

# 虚代理
class VirtualProxy(Subject):
    # 构造时不创建具体实体，节省内存开销
    def __init__(self, filename):
        self.filename = filename
        self.subj = None
    
    # 当访问具体实体时，可以通过权限控制实现具体的效果
    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


if __name__ == '__main__':
    subj = VirtualProxy('test.txt')
    print(subj.get_content())
    """
    读取文件内容！
    """