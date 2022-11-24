import csv

count_months = 0
total_net = 0
l_p_list = []
net_change_list =[]
net_change = 0
test_count_month = 0
test_total_net = 0
with open('Resources/budget_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    test_count_month += 1
    first_row = next(reader)
    total_net += int(first_row[1])
    test_total_net += int(first_row[1]) 

    previous_profit = int(first_row[1])
    for row in reader:
        # question 1:
        test_count_month += 1
        # question 2
        test_total_net += int(row[1])
        # question 3 
        # steps: substract of print row - previous row/ make results into lst
        # (outside of for loop) average monthly change 
        # question 4 
        # question 5 
            # if statement for (both) 
            # if net change is greater than your gratest increase that's your ans
            # if net change is smaller than your smallest increase that's your ans
       
            
        
# calculating average net change
# average_monthly_change = sum(l_p_list) / len(l_p_list)
# print(average_monthly_change)



print(test_count_month)
print(test_total_net)