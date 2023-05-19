print("\n*Your Future*\n","\n","\t" * 4,"Welcome to Your Future!!! Choose the career that matters to you\n","_"*122)
print("\n"," "*3,"Job Specialization")
job = ["AF *   Accounting / Finance", "AHR *  Admin / Human Resources",  "AMC *  Arts / Media /  Communcation", "HR *   Hotel / Restaurant", "E *    Education", "CI *   Computer / IT", "ENGR * Engineering", "MC *   Manufacturing / Construction", "SC *   Sciences", "H *    Healthcare"]
job.sort()
print(" "*5,"-",job[0],"\n"," "*4,"-",job[1],"\n"," "*4,"-",job[2],"\n"," "*4,"-",job[3],"\n"," "*4,"-",job[4],"\n"," "*4,"-",job[5],"\n"," "*4,"-",job[6],"\n"," "*4,"-",job[7],"\n"," "*4,"-",job[8],"\n"," "*4,"-",job[9]), 
print("_"*122)
while True:
    spec = input("SPECIALIZATION INITIALS: ").upper()
    from Methodspy import *
    if spec == 'AF':
        accountingFinance()
        break
    elif spec == 'AHR':
        adminHumanResources()
        break
    elif spec == 'AMC':
        artsMediaCommunication()
        break
    elif spec == 'CI':
        computerAndIT()
        break
    elif spec == 'E':
        educationAndTraining()
        break
    elif spec == 'ENGR':
        engineering()
        break
    elif spec == 'H':
        healthcare()
        break
    elif spec == 'HR':
        hotelAndRestaurant()
        break
    elif spec == 'MC':
        manufacturing()
        break
    elif spec == 'SC':
        sciences()
        break
    elif spec == 'SE':
        services()
        break
    else:
        print(spec)
        

