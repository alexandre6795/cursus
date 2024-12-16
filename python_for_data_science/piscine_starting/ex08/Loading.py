import time


def ft_tqdm(lst: range) -> None:
    """
    takes a range as an argument and displays
    the progress of the iteration
    max = maximum value of the iteration
    percent : percentage of the iteration
    progress_bar : progress bar
    bar_len : length of the progress bar
    space : space between progress bar and bar_len
    it : iteration per second
    start_time : start time of the iteration
    remaining_time : remaining time of the iteration
    """
    bar_len = 100
    prt = 1
    max = len(lst)
    clk = time.time()
    it = 0
    for i, item in enumerate(lst, 1):
        percent = i/max * 100
        progress_bar = "█" * int(percent)
        space = " " * int(bar_len - percent)
        # calculate iteration per second
        it = i / (time.time() - clk)
        # calculate start time
        minute = int((time.time() - clk) / 60)
        second = int((time.time() - clk) % 60)
        start_time = f"{minute:02d}:{second:02d}"
        # calculate remaining time
        remaining_time = (max - i) / it
        minute = int(remaining_time / 60)
        second = int(remaining_time % 60)
        remaining_time = f"{minute:02d}:{second:02d}"
        if (prt == 2 or i == max):
            tmp1 = "%|" + progress_bar + space + "|" + str(i) + "/" + str(max)
            tmp2 = f"{start_time}<{remaining_time}"
            print(f"{percent:.0f}{tmp1}[{tmp2}, {it:.02f}it/s] ", end="\r")
            prt = 1
        else:
            prt += 1
        yield (item)
    print()
