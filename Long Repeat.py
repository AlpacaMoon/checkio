
def long_repeat(line: str) -> int:
    ch = ''
    max = 0
    count = 0
    for i in range(len(line)):
        if line[i] == ch:
            count+=1
        else:
            if count > max:
                max = count
            count = 1
            ch = line[i]
        if i == len(line)-1 and count > max:
            max = count
    return max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')