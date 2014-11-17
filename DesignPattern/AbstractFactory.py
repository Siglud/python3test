# coding=utf-8
__author__ = 'Siglud'
#抽象工厂模式


class IUser(object):
    def insert(self):
        raise SyntaxError

    def delete(self):
        raise SyntaxError


class SQLServerUser(IUser):
    def insert(self):
        print("插入SQLServer用户表")

    def delete(self):
        print("删除SQLServer对应数据")


class MySQLUser(IUser):
    def insert(self):
        print("插入MySQL用户表")

    def delete(self):
        print("删除MySQL对应数据")


class IFactory(object):
    def createUser(self):
        raise SyntaxError


class SQLServerFactory(IFactory):
    def createUser(self):
        return SQLServerUser()


class MySQLFactory(IFactory):
    def createUser(self):
        return MySQLUser()


class DataAccess(object):
    def __init__(self, dbType, dbUser):
        self.dbType = dbType
        self.dbUser = dbUser
        self.funName = dbType + dbUser

    def createUser(self):
        return eval(self.funName)()


if __name__ == "__main__":
    factory = DataAccess("MySQL", "User").createUser()
    factory.insert()