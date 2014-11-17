# coding=utf-8
__author__ = 'Siglud'
#模板方法模式


class ExaminationPaper(object):
    def question1(self):
        print("question 1's answer is: %s" % self.answer1())

    def question2(self):
        print("question 2's answer is: %s" % self.answer2())

    def question3(self):
        print("question 3's answer is: %s" % self.answer3())

    def answer1(self):
        return ""

    def answer2(self):
        return ""

    def answer3(self):
        return ""


class AnswerCard(ExaminationPaper):
    def answer1(self):
        return "A"

    def answer2(self):
        return "B"

    def answer3(self):
        return "C"


if __name__ == "__main__":
    a = AnswerCard()
    a.question1()
    a.question2()
    a.question3()