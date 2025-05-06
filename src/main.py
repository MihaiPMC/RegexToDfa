from pathlib import Path
from regex_parser import get_parsed_json
from postfix_to_nfa import postfix_to_nfa, print_nfa
from nfa_to_dfa import nfa_to_dfa, print_dfa, simulate_dfa

if __name__ == "__main__":
    testcases_path = Path(__file__).parent.parent / "tests" / "testcase.json"
    parsed_data = get_parsed_json(testcases_path)

    for name, test_info in parsed_data.items():
        print(f"\n=== Processing Test Case: {name} ===")
        print(f"Regex: {test_info['regex']}")
        print(f"Postfix: {test_info['postfix']}")

        nfa = postfix_to_nfa(test_info['postfix'])
        # print(f"\nNFA for {name}:")
        # print_nfa(nfa)

        dfa = nfa_to_dfa(nfa)
        # print(f"\nDFA for {name}:")
        # print_dfa(dfa)

        if test_info.get("test_strings"):
            print("\nTest Results:")
            total_tests = len(test_info["test_strings"])
            passed_tests = 0
            failed_tests = []

            print(f"Running {total_tests} tests for regex: '{test_info['regex']}'")

            for i, test in enumerate(test_info["test_strings"], 1):
                input_str = test["input"]
                expected = test["expected"]
                result = simulate_dfa(dfa, input_str)

                if result == expected:
                    passed_tests += 1
                    status = "\033[92mPASS\033[0m"
                else:
                    failed_tests.append((input_str, expected, result))
                    status = "\033[91mFAIL\033[0m"

                print(f"  Test {i}: Input: '{input_str}' Expected: {expected} Got: {result} [{status}]")

            if passed_tests == total_tests:
                print(f"\n\033[92m✓ All {total_tests} tests PASSED!\033[0m")
            else:
                print(f"\n\033[91m✗ {total_tests - passed_tests} of {total_tests} tests FAILED!\033[0m")

                if failed_tests:
                    print("\nFailed Tests Summary:")
                    for i, (input_str, expected, result) in enumerate(failed_tests, 1):
                        print(f"  {i}. Input: '{input_str}' Expected: {expected} Got: {result}")

            print("-" * 50)

