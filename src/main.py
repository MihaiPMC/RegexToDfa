from pathlib import Path
from regex_parser import get_parsed_json


if __name__ == "__main__":
    testcases_path = Path(__file__).parent.parent / "tests" / "testcase.json"
    parsed_data = get_parsed_json(testcases_path)
