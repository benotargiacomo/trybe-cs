from functools import lru_cache
import csv


@lru_cache
def read(path):
    # with open(path, encoding="utf-8") as file:
    #     data = csv.DictReader(file, delimiter=',', quotechar='"')

    #     return list(data)

    with open(path, encoding="utf-8") as file:
        keys, *values = csv.reader(file, delimiter=',', quotechar='"')

        jobs = list()

        for value in values:
            line = dict()
            for index, content in enumerate(value):
                line[keys[index]] = content

            line_cp = line.copy()
            jobs.append(line_cp)

        return jobs
