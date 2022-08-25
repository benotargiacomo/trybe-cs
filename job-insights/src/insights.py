from . import jobs

# [{
#     'job_title': 'Marketing',
#     'company': 'Relief',
#     'state': 'NY',
#     'city': 'New York',
#     'min_salary': '',
#     'max_salary': '',
#     'job_desc': 'Marketing operations of the company.',
#     'industry': 'Finance',
#     'rating': '4.0',
#     'date_posted': '2020-05-08',
#     'valid_until': '2020-06-07',
#     'job_type': 'FULL_TIME',
#     'id': '0'
# }]


def get_unique_job_types(path):
    data = jobs.read(path)
    types = {job["job_type"] for job in data}

    return list(types)


def filter_by_job_type(jobs, job_type):
    filter = [job for job in jobs if job["job_type"] == job_type]

    return filter


def get_unique_industries(path):
    data = jobs.read(path)
    industries = {job["industry"] for job in data if job["industry"]}

    return list(industries)


def filter_by_industry(jobs, industry):
    filter = [job for job in jobs if job["industry"] == industry]

    return filter


def get_max_salary(path):
    data = jobs.read(path)

    salaries = [
        int(job["max_salary"]) for job in data if job["max_salary"].isnumeric()
    ]

    max_salary = salaries[0]

    for salary in salaries:
        if salary > max_salary:
            max_salary = salary

    return max_salary


def get_min_salary(path):
    data = jobs.read(path)

    salaries = [
        int(job["min_salary"]) for job in data if job["min_salary"].isnumeric()
    ]

    min_salary = salaries[0]

    for salary in salaries:
        if salary < min_salary:
            min_salary = salary

    return min_salary


def matches_salary_range(job, salary):
    # max, min = (job[k] for k in ("max_salary", 'min_salary'))

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('error')

    if type(
            job["min_salary"]
            ) is not int or type(
                job["max_salary"]
                    ) is not int:
        raise ValueError('error')

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError('error')

    if type(salary) is not int:
        raise ValueError('error')

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    try:
        data = [
            job for job in jobs if matches_salary_range(
                {
                    "min_salary": job["min_salary"],
                    "max_salary": job["max_salary"]
                }, salary)
            ]
        return data
    except ValueError:
        pass
