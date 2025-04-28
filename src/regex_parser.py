import json
from pathlib import Path


def load_testcases(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File {path} does not exist.")
    with p.open('r', encoding='utf-8') as f:
        return json.load(f)


def add_concatenation(regex):
    result = []
    prev = None
    for c in regex:
        if prev is not None:
            if prev not in ['|', '('] and c not in ['|', ')', '*', '+', '?']:
                result.append('.')
        result.append(c)
        prev = c
    return ''.join(result)


def regex_to_postfix(regex):

    regex = add_concatenation(regex)
    oppOrder = {'|': 1, '.': 2, '*': 3, '+': 3, '?': 3}
    postfix = []
    stack = []

    for c in regex:
        if c.isalnum():
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and oppOrder[c] <= oppOrder[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


def get_parsed_json(testcases_path):
    testcases = load_testcases(testcases_path)
    parsedJson = {}
    for test in testcases:
        name = test.get("name")
        regex = test.get("regex")
        postfix = regex_to_postfix(regex)
        case_info = {
            "regex": regex,
            "postfix": postfix,
            "test_strings": test.get("test_strings", [])
        }
        parsedJson[name] = case_info
    return parsedJson

if __name__ == "__main__":
    testcases_path = Path(__file__).parent.parent / "tests" / "testcase.json"
    parsedJson = get_parsed_json(testcases_path)
    print(parsedJson)

