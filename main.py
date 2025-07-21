import sys
from stats import get_num_words
from stats import get_character_count
from stats import generate_report

def main():
    args = sys.argv
    print(args)
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    report = generate_report(args[1])
    print(report)

main()
