import easyweb.core


class Numbers(object):
    def __init__(self):
        self.n = 0

    def add(self, a):
        self.n += a
        return self.n


if __name__ == "__main__":
    num = Numbers()
    print(easyweb.core.classmethods(num))
