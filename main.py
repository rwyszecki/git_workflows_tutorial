from suprise.job import Job


if __name__ == '__main__':
    print("Now let's count a little")
    numbers = [1, 4]
    result = Job.addition(*numbers)
    print(f"We got {result=}")
