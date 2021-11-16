from TK_1 import array_crt
from TK_2 import tuple_crt
from TK_3 import average_divide_list
from TK-4 import average_multiply_list
from TK-5 import sqrt_my_list


def main():
    size = int(input())
    scroll = array_crt(size)
    print(scroll)
    print(tuple_crt(scroll))
    print(average_divide_list(scroll))
    print(average_multiply_list(scroll))
    print(sqrt_my_list(scroll))
    return 0


if __name__ == "__main__":
    sys.exit(main())