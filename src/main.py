from pathlib import Path
from regex_parser import get_parsed_json
from postfix_to_nfa import postfix_to_nfa, print_nfa


if __name__ == "__main__":
    testcases_path = Path(__file__).parent.parent / "tests" / "testcase.json"
    parsed_data = get_parsed_json(testcases_path)

    for name, test_info in parsed_data.items():
        print(f"\n=== Processing Test Case: {name} ===")
        print(f"Regex: {test_info['regex']}")
        print(f"Postfix: {test_info['postfix']}")

        nfa = postfix_to_nfa(test_info['postfix'])
        print(f"\nNFA for {name}:")
        print_nfa(nfa)
