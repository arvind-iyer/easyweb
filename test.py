import easyweb


class Numbers(object):
    def __init__(self):
        self.a = 5

    def add(self, n=1):
        self.a += n
        return self.a


if __name__ == "__main__":
    easyweb.run(Numbers())
