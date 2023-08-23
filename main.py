def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78
    hours = 0
    overtime_wage = 0

    if(workhours > reg_hours):
        overtime = workhours - reg_hours
        overtime_wage = overtime * ov_rate
        hours = workhours - overtime
        
        print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    else:
        hours = workhours

    regular_wage = hours * reg_rate
    total_wage = regular_wage + overtime_wage
    print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
