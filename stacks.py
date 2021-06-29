class StackArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, n):
        return self.data.append(n)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self.data[-1]

    def __str__(self):
        return str(self.data)


def matchedParenthesis(exp):
    lefty = '({['
    righty = ')}]'
    S = StackArray()
    for char in exp:
        if char in lefty:
            S.push(char)
        elif char in righty:
            if S.is_empty():
                return False
            elif righty.index(char) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def matchedHTML(raw):
    S = StackArray()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k + 1)
    return S.is_empty()


if __name__ == '__main__':
    '''Reversed'''
    stack = StackArray()
    a = [3, 4, 5, 2, 1, 8, 9]
    rev_a = []
    for i in a:
        stack.push(i)
    for j in range(len(stack)):
        rev_a.append(stack.pop())
    print(rev_a)

    exp = '[(5-x)+(4+y)]'
    matched = matchedParenthesis(exp)
    print(matched)
    isHTML = matchedHTML('<h1> Hello Dear Friends /h1>')
    print(isHTML)
