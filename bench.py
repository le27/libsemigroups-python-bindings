import time
def benchmark(func, args, trials = 1):
    if not isinstance(args, list) and isinstance(trials, int) and hasattr(func, '__call__'):

        raise TypeError

    if trials < 1:

        raise ValueError



    result = []

    # The list of times

    for n in range(trials):

        start = time.time()

    # Measure the time taken to

        func(*args)

    # by func(arg)

        end = time.time()

        result.append((end - start) * 1000)

    # Convert to milliseconds

    return result
