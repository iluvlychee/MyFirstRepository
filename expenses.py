daily_items = {"phone":50, "toothbrush":5, "soap":3, "laptop":75, "hairbrush":5, "pencil":2, "notebook":5, "tablet":30, "kindle":30, "charger":25}
weekly_expense = {"Week 1":0, "Week 2":0, "Week 3":0, "Week 4":0}

for k1, v1 in weekly_expense.items(): # the outer for loop runs first. initial k1 = "Week 1"
    expense = 0
    for k2, v2 in daily_items.items(): 
        expense = expense + v2 * 1
    weekly_expense[k1] = expense

print(weekly_expense)