
def calculate_next_mark_for_desired_average(average, count_marks, addup_marks):
    if average > 5:
        desired_average = 5
        minimum_mark_for_desired_average = (desired_average * (count_marks + 1)) - addup_marks
        print(minimum_mark_for_desired_average)
        # if minimum_mark_for_desired_average < 0:
        #     return False
        # else:
        #     return