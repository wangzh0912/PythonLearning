# python3

from collections import deque

def find_mismatch(text):
    stack = deque()
    for i, next in enumerate(text):

        if next in "([{":
            stack.append((i, next))

        if next in ")]}":
            if not stack:
                return i + 1
            _, top = stack.pop()
            if (top == '(' and next != ')') or (top == '[' and next != ']') or (top == '{' and next != '}'):
                return i + 1

    if not stack:
        return 'Success'
    else:
        # get the first index of opening bracket
        first_idx, _ = stack[0]
        return first_idx + 1
def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

