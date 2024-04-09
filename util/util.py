import argparse
from typing import Any


def get_arguments() -> dict:
    """
    Get the arguments from the command line
    :return: dict with key|value arguments
    """
    parser = argparse.ArgumentParser(description='Predictive Maintenance tool based on Machine Learning')
    parser.add_argument('--input', type=str, help='Path to the raw data file', required=True)
    parser.add_argument('--output', type=str, help='Path to the processed output file', required=True)
    parser.add_argument('--action', type=str,
                        help='Action to be performed over the input file (mean)',
                        required=True)

    return vars(parser.parse_args())


def colored_print(text: Any, color: str):
    """
    Print a text with a color
    :param text: text to print
    :param color: color to use (red, green, yellow, blue, purple, cyan)
    """

    match color:
        case 'red':
            print(f'\033[91m{text}\033[0m')
        case 'green':
            print(f'\033[92m{text}\033[0m')
        case 'yellow':
            print(f'\033[93m{text}\033[0m')
        case 'blue':
            print(f'\033[94m{text}\033[0m')
        case 'purple':
            print(f'\033[95m{text}\033[0m')
        case 'cyan':
            print(f'\033[96m{text}\033[0m')
        case _:  # default
            print(f'\033[97m{text}\033[0m')
