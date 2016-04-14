import traceback


class SimpleError(Exception):
    pass


class DoTrace(object):
    """
    正确的跟踪错误以及raise from的用法
    """
    def __init__(self):
        self.a = None

    def do_some_error(self):
        try:
            self.a = 1 / 0
        except ZeroDivisionError as e:
            raise SimpleError("Cannot Division Zero!") from e

    def call_error(self):
        try:
            self.do_some_error()
        except SimpleError as e:
            print(e)
            print('start print!')
            print(traceback.format_exc())
            print('trace end!')


if __name__ == '__main__':
    do = DoTrace()
    do.call_error()
