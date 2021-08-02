# Section: Scientific Expedition
# Level: Elementary+
# Title: Remove Brackets



def remove_brackets(line: str) -> str:
    brackets = {'(':')', '[':']', '{':'}'}
    head, tail = '', ''

def func(line: str):
    if len(line) <= 1:
        return ''
    elif line[0] in ')]}':
        func(line[1:])

    for pos, ltr in enumerate(line):
        pass


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
