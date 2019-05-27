def find_new_salary(current_salary,job_level):
    if job_level==3:
        incr=current_salary*0.15
        new_salary=current_salary+incr
    elif job_level==4:
        incr=current_salary*0.07
        new_salary=current_salary+incr
    elif job_level==5:
        incr=current_salary*0.05
        new_salary=current_salary+incr
    else:
        new_salary=current_salary
    return new_salary
new_salary=find_new_salary(10000,3)
print(new_salary)
