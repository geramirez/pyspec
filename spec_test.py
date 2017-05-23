def get_indentations(self):
    indentations = ''
    parent = self.parent
    while parent:
        indentations += '\t'
        parent = parent.parent
    return indentations


class Describe:
    def __init__(self, text, parent=None):
        self.text = text
        self.parent = parent

    def __enter__(self):
        self.print_description()
        return self

    def __exit__(self, *args):
        pass

    def print_description(self):
        print('Describe:', self.text)


class It:
    def __init__(self, text, parent=None):
        self.text = text
        self.parent = parent

    def __enter__(self):
        self.print_description()
        return ExpectWrapper(self)

    def __exit__(self, *args):
        pass

    def print_description(self):
        indentations = get_indentations(self)
        print(f'{indentations}It:', self.text)


class ExpectWrapper:

    def __init__(self, parent):
        self.parent = parent

    def __call__(self, comparable):
        return Expect(comparable, self.parent)

class Expect:

    def __init__(self, comperable, parent=None):
        self.comperable = comperable
        self.parent = parent

    def toEqual(self, other_comperable):
        if self.comperable != other_comperable:
            indentations = get_indentations(self)
            print(f'{indentations}FAIL:{self.comperable} is not equal to {other_comperable}')


if __name__ == '__main__':

    with Describe('Addition') as des:
        with It('correctly add 2 values', des) as expect:
            expect(1+1).toEqual(2)

        with It('correctly adds 3 values', des) as expect:
            expect(1+1+1).toEqual(2)


