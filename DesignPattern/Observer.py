# coding=utf-8
__author__ = 'Siglud'
#观察者


class Observer(object):
    """观察者"""
    def __init__(self, subject):
        self.subject = subject
        self.subject.addObserver(self)
        self.integer = self.subject.integer
        self.double = self.subject.double
        self.string = self.subject.string

    def update(self, integer, double, string):
        self.integer = integer
        self.double = double
        self.string = string
        self.display()

    def display(self):
        print(self.integer, self.double, self.string)


class Subject(object):
    """主题类"""
    def __init__(self):
        self.observers = []

        self.integer = 1
        self.double = 1.2
        self.string = "hello"

    def addObserver(self, observer):
        """添加观察者"""
        self.observers.append(observer)

    def deleteObserver(self, observer):
        """删除观察者"""
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObserver(self):
        """通知观察者更新"""
        for observer in self.observers:
            observer.update(self.integer, self.double, self.string)

    def setValue(self, integer, double, string):
        self.integer = integer
        self.double = double
        self.string = string
        self.notifyObserver()

if __name__ == "__main__":
    subject = Subject()
    observer = Observer(subject)
    observer.display()
    subject.setValue(143, 238.90, "Good!")
    subject.setValue(45, 89.99, "Smile")