import random as r
try:
    quostion=int(input("Enter how many questions you want to answer?: "))
    if quostion<=0:
        print("Please enter a valid number")
        quostion=int(input("Enter how many quostion you want to answer?: "))
    elif quostion>16:
        print("The maximum number of quostion is 16")
        quostion=int(input("Enter how many quostion you want to answer?: "))
except:
    print("Please enter a valid number")
    quostion=int(input("Enter how many questions you want to answer?: "))
    if quostion<=0:
        print("Please enter a valid number")
        quostion=int(input("Enter how many quostions you want to answer?: "))
    elif quostion>16:
        print("The maximum number of quostion is 16")
        quostion=int(input("Enter how many quostions you want to answer?: "))

q1= {'Kazi Nazrul Islam':[1899,1976]}
q2= {'Golom Mustafa':[1897,1964]}
q3= {'Jashim Uddin':[1903,1976]}
q4= {'Farrukh Ahmad':[1918,1974]}
q5= {'Alauddin Al Azad':[1932,2009]}
q6= {'Ahsan Habib':[1917,1985]}
q7= {'Nirmalendu Goon':[1945,2010]}
q8= {'Robart Frost':[1874,1963]}
q9= {'Abul Hosain':[1922,2014]}
q10={'Rizia Rahman':[1939,2019]}
q11={'Selina Hossain':[1947,'Not yet']}
q12={'Bonoful':[1899,1979]}
q13={'Abul Fazal':[1903,1983]}
q14={'Kazi Abdul Wadud':[1894,1970]}
q15={'Ismail Hossain Sirazi':[1880,1931]}
q16={'Ahammad Sharif':[1922,1999]}

corret_ans=0
wrong_ans=[]
name=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16]
for i in range(quostion):
    q=r.choice(name)
    for key in q:
        print(key)
        try:
            year_of_birth=int(input("Enter the year of birth: "))
        except:
            print("Please enter a valid number")
            year_of_birth=int(input("Enter the year of birth: "))
        year_of_death=input("Enter the year of death and if not die enter 'Not yet': ")
        if year_of_death=='Not yet':
            year_of_death=year_of_death.capitalize()
        else:
            try:
                year_of_death=int(year_of_death)
            except:
                print("Please enter a valid number")
                year_of_death=int(input("Enter the year of death: "))
        if q[key]==[year_of_birth,year_of_death]:
            print("You are correct")
            corret_ans += 1
        else:
            print("You are wrong")
            print("The correct answer is: ",q[key])
            wrong_ans.append(q)
    name.remove(q)

print("You have answered ",corret_ans," correct answer!")
if len(wrong_ans) > 0:
    print("You have answered wrong for the following poet: ")
    for i in wrong_ans:
        for key in i:
            print(key)
            print("The correct answer is: ",i[key])
