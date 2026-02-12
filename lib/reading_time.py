def reading_time(string):
    print(string)
    word_count = len(string.split())
    calculated_reading_time = int(word_count / 200)
    if calculated_reading_time < 1:
        return 'Estimated reading time is less than a minute'
    return f'Estimated reading time is {calculated_reading_time} minute'