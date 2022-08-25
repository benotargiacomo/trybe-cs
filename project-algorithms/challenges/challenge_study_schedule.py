def study_schedule(permanence_period, target_time):
    count = 0

    if target_time is None:
        return None

    for start, finish in permanence_period:
        if type(start) is not int or type(finish) is not int:
            return None
        if start <= target_time <= finish:
            count += 1

    return count
