# برنامه ای بنویسید که مقدار ماکزیمم و مینیمم value های دیکشنری را خروجی دهد.

data = {'a' : 20, 'd' : 11, 'v' : 4, 'y' : 32, 'p' : 10, 'k' : 5 }

min_ = 0
max_ = 0

b = []
for k, v in data.items() :
    data[k] = b.append(v)

for i in b:
    if i < min_:
        min_ = i
    elif i > max_:
        max_ = i


print('Min = ', min_, 'Max = ', max_)
