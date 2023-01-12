# برنامه ای بنویسید که یک جمله گرفته و تعداد تکرار هر کلمه را در یک دیکشنری ذخیره کند.

text = 'All Cats Are Beautiful'

res = {}

for i in text:
    res[i] = text.count(i)

print(res)

