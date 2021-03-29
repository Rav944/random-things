import argparse


def fibonacci(sequence: int, position=1, value_1=0, value_2=1) -> int:
    if position == sequence:
        return value_2
    return fibonacci(sequence, position + 1, value_2, value_1 + value_2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sequence", help="Show fibonacci sequence")
    args = parser.parse_args()
    if args.sequence:
        s = args.sequence
        try:
            s = int(s)
        except ValueError:
            print("Sequence number must be a number")
        else:
            if s <= 0:
                print('The sequence number must be greater than 0')
            else:
                print(fibonacci(int(args.sequence)))

