def average_divide_list(scroll):
    average = sum(scroll) / len(scroll)

    return [i / average for i in scroll]
