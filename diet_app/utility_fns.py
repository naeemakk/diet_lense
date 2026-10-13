
def calculate_bmr(age, weight, height, gender,activity_level="1.2"):
    bmr=0
    if gender=="male":
        bmr=(10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr=(10 * weight) + (6.25 * height) - (5 * age) - 161
    tdee=bmr*float(activity_level)
    # return round(bmr)
    return tdee

# res=calculate_bmr(28,80,180,"male")
# res=calculate_bmr(23,58,156,"female")
# print(res)