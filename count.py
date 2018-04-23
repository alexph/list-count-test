def count(lst): 
    """
    Count items in a list.

    Only accesses list by item index to find length.
    
    It can't match the speed of the builtin but it only marginally increases in 
    time for large lists.

    It works by stepping forward in large increments past the end of the list, 
    reducing the step to 1/10 then stepping back to the last known index before 
    incrementing forward again, repeating until stepping is single digits for 
    the final <= 10.

    """
    step = 100000
    read_forward = 0
    stopped = 0

    if not lst:
        return stopped

    while True:
        try:
            tmp = lst[read_forward]
            del tmp
            stopped = read_forward
            read_forward = stopped + step
        except IndexError:
            if step == 1:
                break
            step = int(step / 10)
            read_forward = stopped

    return stopped + 1

if __name__ == '__main__':
    import timeit
    print('making list')

    # I don't recommend the max size of list below.
    # (My Air doesn't recommend it either)
    # big_list = list(range(536870912))

    small_list = list(range(10))
    big_list = list(range(1234567))

    print('counting list')

    print(timeit.Timer('len(small_list)', globals=locals()).timeit(10))
    print(timeit.Timer('count(small_list)', globals=locals()).timeit(10))
    
    print(timeit.Timer('len(big_list)', globals=locals()).timeit(10))
    print(timeit.Timer('count(big_list)', globals=locals()).timeit(10))

    print('small lists:', count(small_list), 'should equal native', len(small_list))
    print('big lists:', count(big_list), 'should equal native', len(big_list))
