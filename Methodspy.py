# Methodspy.py>
class Job:
    def __init__(self, title, company, location, description, qualifications, benefits):
        self.title= title 
        self.company = company
        self.location = location
        self.description = description
        self.qualifications = qualifications
        self.benefits = benefits
    def summary(self):
        print(f"{self.title}\n{self.company}\nLOCATION: {self.location}\n\nDESCRIPTION: {self.description}\n\nQUALIFICATIONS: {self.qualifications}\n\nBENEFITS: {self.benefits}.")
class Job1(Job):
    def _init_(self, title, company, location, description, qualifications, benefits):
        super()._init_(self, title, company, location, description, qualifications, benefits)

def accountingFinance():
    accountingFinanceCat = ["A. Audit & Taxation", "G. General / Cost Accounting", "B. Banking / Financial"]
    accountingFinanceCat.sort()
    print("\n\n"," "*4,"-",accountingFinanceCat[0],"\n"," "*4,"-",accountingFinanceCat[1],"\n"," "*4,"-",accountingFinanceCat[2])
    accountingFinanceAction = input("What category?: ")

    if accountingFinanceAction == 'A':
        print("\nA. Audit & Taxation\n", "_"*165)
        job1 = Job("1. INTERNAL AUDITOR", "Euro-Swiss Food Incorporated", "National Capital Region", "\nThe successful candidate must possess a thorough knowledge of accounting procedures and a sound judgement to improve risk management, control, and governance processes.", "\n1. Bachelor's degree in Accounting\n2. Must be a CPA or CIA\n3. Has knowledge in SAP\n4. Minimum of at least 3 years experience in auditing/controlling or closely related field is highly desirable.\n5. Experience with full audit cycle is an advantage.\n6. Working Conditions: Normal office environment", "\nMedical, Business (e.g. Shirts)\nMid-Year bonus\nDecember bonus\nFree meal")
        job1.summary()
        print (interested)
        exit()
    elif accountingFinanceAction == 'B':
        print("\nBanking / Financial\n", "_"*165)
        job7 = Job ("\n1. Management Trainee for Business Relationship Officer Development Program", "\nRizal Commercial Banking Corporation (RCBC)", "NCR, Bicol, C.A.R, Central Luzon, Western Visayas, Davao, Central Visayas, Eastern Visayas, Calabarzon & Mimaropa", "\nBe exposed to the best salespeople in the industry, development opportunities and training programs, and Competitive salary and benefits including guaranteed bonuses", "\n1. Fresh graduates with Honorable Mention/Latin Honors\n2. With propensity to do sales\n3. Innate leadership skills, high level of confidence\n4. Excellent oral and written communication skills\n5. Willing to be assigned in any RCBC Branches", "\n1. Dental, Medical & Education support\n2. Miscellaneous allowance\n3. Loans\n4. Parking\n5. Vision, ")
        job7.summary()
        print (interested)
        exit()
    elif accountingFinanceAction == 'G':
        print("\nGeneral / Cost Accounting\n", "_"*165)
        job4 = Job("\n1. ACCOUNTING OFFICER", "\nRADIO MINDANAO NETWORK, INC.", "Laguna", "\nOversee daily/monthly transactions, prepare financial statements, assist external auditors, review budget reports, coordinate tax returns, maintain and document\naccounting policies and procedures, and perform other related duties.", "\n1. Graduate of BS Accountancy\n2. Preferably Certified Public Accountant\n3. Have at least three years related work experience\n4. Possess excellent interpersonal skills, multi-tasking and can work under pressure\n5. Proficient in Windows/ MS Office application\n6. To be assigned at Head Office, Makati City\n7. Can start asap", "\n1. 13th month\n2. Year end bonus\n3. Sick leave\n4. Vacation leave\n5. HMO, Dental and Medical benefits\n6. Life insurance & Retirement plan")
        job4.summary()
        print (interested)
        exit()
    else:
        accountingFinance()

def adminHumanResources():
    adminHumanResourcesCat = ["C. CLERICAL / ADMINISTRATIVE SUPPORT", "H. HUMAN RESOURCES", "S. SECRETARIAL EXECUTIVE PERSONAL ASSISTANT"]
    adminHumanResourcesCat.sort()
    print("\n\n"," "*4,"-",adminHumanResourcesCat[0],"\n"," "*4,"-",adminHumanResourcesCat[1],"\n"," "*4,"-",adminHumanResourcesCat[2])
    adminHumanResourcesAction = input("What category?: ")
    if adminHumanResourcesAction == 'C':
        print("\nLERICAL / ADMINISTRATIVE SUPPORT\n", "_"*165)
        job10 = Job ("\n1. Administration & Asset Assistant", "\nMIESCOR Infrastructure Development Corp", "Batangas", "Admins, Maintain supplies, report expenses, secure files and filing systems.Asset management is essential for managing regional companies' assets and\npreparing reports.", "\n1. College graduate; additional qualifications in Office Administration are a plus.\n2. Interpersonal and strong analytical skills\n3. Computer knowledge\n4. Excellent written and verbal communication skills\n5. Attention to detail\n6. Ability to translate stakeholder requirements into reporting deliverables", "\n1. Medical and Miscellaneous allowance")
        job10.summary()
        print (interested)
        exit()
    elif adminHumanResourcesAction == 'H':
        print("\nHUMAN RESOURCES\n", "_"*165)
        job13 = Job("\n1. Human Resources Sr. Associate", "\nHonda Philippines, Inc.", "Batangas", "\nSuccessful candidate will be responsible for effective recruitment and manpower planning, facilitating the recruitment process, conducting interviews, and recommending\nthe best candidates.", "\n1. Bachelor's/College Degree in Psychology\n2. Preferably more than 1 year experience specialized in Human Resources or equivalent.\n3. Experience in recruitment/talent acquisition is a plus\n4. Proficient in using Microsoft Office\n5. Registered Psychometrician\n6. Basic knowledge in Labor laws and DOLE Rules and regulations\n7. Ability to maintain the highly confidential nature of human resources work", "\n1. Dental& Medical, Education support, Miscellaneous allowance\n2. Loans\n3. Sports\n4. Meal and rice subsidy\n5. Bonuses and incentive\n8. Travel opportunity")
        job13.summary()
        print (interested)
        exit()
    elif adminHumanResourcesAction == 'S':
        print("\nSECRETARIAL EXECUTIVE PERSONAL ASSISTANT\n", "_"*165)
        job16 = Job ("\n1. Executive Assistant","JT International (Philippines), Inc.","Batangas","\nManage the General Manager's calendar to schedule meetings and appointments and make sure they go as planned.Supports the creation of paperwork necessary to satisfy\nlegal requirements (POA, contracts, permissions). Consider the minutes from the meeting.Coordinate and interact with many departments and all levels of staff. Prepare\nand handle internal and external correspondence for Factory Lead signature.Respond to and facilitate requests from Head Quarters as needed. Make sure all necessary\napproval documents—such as leave application forms, trip approval forms, expense claim reports, etc. are ready for the Factory Lead and MT to sign and approve.Keep\norganized, current filing and tracing systems. Maintain the privacy of sensitive matters and/or issues.","\n1. Any secretarial or business management/administration course at the bachelor's level\n2. A top management position in an international company requiring at least one year of secretarial experience reporting to an expat is required.\n3. Microsoft Office (Excel, PowerPoint, Word, MS Teams) proficiency is a plus.\n4. Good command of English (written and oral)\n5. Must haves: experience working in a foreign setting, great time management abilities, ability to operate under pressure, and stress tolerance","\n1. possess health insurance, dependent coverage, and a medication allowance\n2. Get rewards and financial perks like a lunch and rice allowance.\n3. Programs for employee wellbeing\n4. Opportunities for you to advance your career")
        job16.summary()
        print (interested)
        exit()
    else:
        adminHumanResources( )


def artsMediaCommunication():
    artsMediaCommunicationCat = ["A. ADVERTISING", "C. CREATIVE ARTS DESIGN", "P. PUBLIC RELATIONS"]
    artsMediaCommunicationCat.sort()
    print("\n\n"," "*4,"-",artsMediaCommunicationCat[0],"\n"," "*4,"-",artsMediaCommunicationCat[1],"\n"," "*4,"-",artsMediaCommunicationCat[2])
    artsMediaCommunicationAction = input("What category?: ")
    if artsMediaCommunicationAction == 'A':
        print("\nADVERTISING\n", "_"*165)
        job19 = Job ("\n1. Social Media Associate", "\nAsian Vision Cable Holdings Inc", "Laguna", "\nMaintain a professional attitude in handling subscriber concerns and keep a record of reports handled in a day.", "\n1. Candidate must possess at least Bachelor's Degree in Business Management or related courses\n2. At least with less than a year of experience in Customer Service, Social Media Planning or related field\n3. Must be patient, customer oriented, accommodating and a team player\n4. Willing to be assigned in Binan City, Laguna", "\n1. Dental& Medical\n2. Miscellaneous allowance\n3. Loans\n4. Sports", )
        job19.summary()
        print (interested)
        exit()
    elif artsMediaCommunicationAction == 'C':
        print("\nCREATIVE ARTS DESIGN\n", "_"*165)
        job22 = Job ("\n1. Graphic Artist - permanent WFH", "\nConnectUs Marketing Solutions, Inc.", "Batangas", "\nCreate visual concepts to communicate ideas, develop layout and production design, edit raw material, incorporate changes, review designs for errors, and other duties as\nassigned.", "\n1. Proficient in Adobe Illustrator, Photoshop, and InDesign and other essential design tools\n2. Basic knowledge of HTML; coding experience is an advantage\n3. Basic Video Editing skills: Adobe Premiere Pro, Filmora, etc. is an advantage\n4. Handles suggestions, corrections, rejections positively\n5. Good organizational skills and understanding of design.", "\n1. Permanent work-from-home\n2. Full Time and Long Term Employment\n3. Basic Salary + Government Mandated Benefits\n4. Internet allowance, Bonuses, promotion and other incentives")
        job22.summary()
        print (interested)
        exit()
    elif artsMediaCommunicationAction == 'P':
        print("\nPUBLIC RELATIONS\n", "_"*165)
        job25 = Job ("Public Relation Supervisor", "Asia Link Finance Corporation", "Quezon", "\nThe PR Communications is responsible in developing Corporate Communications plans that include strategies, tactics and budget management including media relations/\nengagement, company branding, and content development and management.", "\n1. Graduate of Bachelor's degree in Journalism/Communications/Public Relations/Marketing or any related field.\n2. At least two (2) years of relevant working experience in Corporate Communications. (Public Relations, Corporate Social Responsibility, and Events Management)\n3. Excellent organizational and planning abilities\n4. Must be creative and excellent storyteller\n5. Experience in copywriting and editing\n6. Strong Communications Skills", "\nHMO, Leave Credits, Allowances, Birthday Cash Gift, Birthday Cash Gift, Life Insurance, Profit-Sharing, Retirement Benefits")
        job25.summary()
        print (interested)
        exit()
    else:
        artsMediaCommunication()


def services():
    servicesCat = ["P. PERSONAL", "C. CUSTOMER", "S. SOCIAL"]
    servicesCat.sort()
    print("\n\n"," "*4,"-",servicesCat[0],"\n"," "*4,"-",servicesCat[1],"\n"," "*4,"-",servicesCat[2])
    servicesAction = input("What category?: ")
    if servicesAction == 'C':
        print("\nCUSTOMER\n", "_"*165)
        job32 = Job ("1. Telecommunications Dayshift Call Center Agent","TTEC Customer Care Management Phils., Inc.","Batangas","\nBeing a site-based customer service representative in Lipa will allow you to #ExperienceTTEC, an award-winning work experience and business culture, while also helping\nto create and deliver great customer experiences.","\n1. Vocational Diploma/ short Course certificate / Bachelor's degree","\nDental, Education support, Miscellaneous allowance, Medical, Loans, Sports (e.g. Gym), Parking, Casual (e.g. T-shirts), Shifting Schedules")
        job32.summary()
        print (interested)
        exit()
    elif servicesAction == 'P':
        print("\nPERSONAL\n", "_"*165)
        job28 = Job ("1. Masseuse / Massage Therapist","Soleeluna Private Resort", "Batangas", "\nGather the annual child letters, photos, and progress reports for sponsored kids in the CDP. The CDP's oversight of sponsored children Coordination of the Sponsorship\ndeliverables with stakeholders, partners, and community volunteers Make sure you deliver high-quality output on time to the database that stores updates for sponsored\nchildren. Updating the child masterlist on a monthly basis ","\n1. At least one year of related job experience; working for an international NGO (INGO) is an advantage.\n2. Display the capacity to set and meet goals and deadlines\n3. Understand the fundamentals of Microsoft Office programs like PowerPoint, Word, Excel, and databases.\n4. Good communication skills both in writing and speaking, and flexible, flexible, and able to function well in a range of environments.\n5. Being understanding of the conduct of a variety of people.\n6. Highly organized, with an eye for detail and the capacity to prioritize a variety of tasks in order to fulfill deadlines","\nMiscellaneous allowance, Regular hours, Mondays - Fridays, Business (e.g. Shirts), HMO, Government Mandated Benefits")
        job28.summary()
        print (interested)
        exit()
    elif servicesAction == 'S':
        print("\nSOCIAL\n", "_"*165)
        job30 = Job ("\n1. Field Sponsorship Staff", "Good Neighbors International Phils. Branch Inc", "Batangas","\nGather the annual child letters, photos, and progress reports for sponsored kids in the CDP. The CDP's oversight of sponsored children Coordination of the Sponsorship\ndeliverables with stakeholders, partners, and community volunteers Make sure you deliver high-quality output on time to the database that stores updates for our\nsponsored children. Updating the child masterlist on a monthly basis ","\n1. At least one year of related job experience; working for an international NGO (INGO) is an advantage.\n2. Display the capacity to set and meet goals and deadlines\n3. Understand the fundamentals of Microsoft Office programs like PowerPoint, Word, Excel, and databases.\n4. Good communication skills both in writing and speaking, and flexible, flexible, and able to function well in a range of environments.\n5. Being understanding of the conduct of a variety of people.\n6. Highly organized, with an eye for detail and the capacity to prioritize a variety of tasks in order to fulfill deadlines","Miscellaneous allowance, Regular hours, Mondays - Fridays, Business (e.g. Shirts), HMO, Government Mandated Benefits")
        job30.summary()
        print (interested)
        exit()
    else:
        services()


def hotelAndRestaurant():
    hotelAndRestaurantCat = ["F. FOOD", "H. HOTEL"]
    hotelAndRestaurantCat.sort()
    print("\n\n"," "*4,"-",hotelAndRestaurantCat[0],"\n"," "*4,"-",hotelAndRestaurantCat[1])
    hotelAndRestaurantAction = input("What category?: ")
    if hotelAndRestaurantAction == 'F':
        print("\nFOOD\n", "_"*165)
        job34 = Job ("1. Management Trainee","JFC Affiliates and Subsidiaries","Batangas","\nImplementation and assurance of compliance on Food, Safety and Cleanliness Programs, day-to-day operations effectiveness of Dine-In and Take-Home Sales Services, sales\nbuilding initiatives, assessment of opportunities in operations and cost management, workforce management, and other store administrative activities.","\nMust have excellent leadership and customer service skills, communicate well, and be willing to work long hours.","\nDental, Education support, Miscellaneous allowance, Medical, Loans, Regular hours, Mondays - Fridays, Medical, Miscellaneous allowance, Education support, Loans, Dental, Meal Allowan, Company Uniform")
        job34.summary()
        print (interested)
        exit()
    elif hotelAndRestaurantAction == 'H':
        print("\nHOTEL\n", "_"*165)
        job37 = Job ("1. QA/QC Manager", "SUMOPAK INDUSTRIAL CORPORATION","Quezon","\nReports quality problems, submits monthly accomplishment report, supervises shift inspectors, monitors Department Objectives and Targets, checks/verifies quality\nproblems, receives and attends customer complaints, checks inspection items and standard specifications, and checks/reviews QTR and NCR submitters.","\n1. The candidate must hold a minimum of a Bachelor's or College Degree in Civil Engineering or an equivalent degree.\n2. Must have at least three (3) years of relevant work experience.\n3. Must have knowledge of QESH, ISO 9001, and other relevant models must be in-depth.","\nN/A")
        job37.summary()
        print (interested)
        exit()
    else:
        hotelAndRestaurant()


def educationAndTraining():
    educationAndTrainingCat = ["E. EDUCATION", "T. TRAINING"]
    educationAndTrainingCat.sort()
    print("\n\n"," "*4,"-",educationAndTrainingCat[0],"\n"," "*4,"-",educationAndTrainingCat[1])
    educationAndTrainingAction = input("What category?: ")
    if educationAndTrainingAction == 'E':
        print("\nEDUCATION\n", "_"*165)
        job40 = Job ("1. Teacher", "Lipa Montessori School of Learning Inc.", "Lipa Montessori School of Learning Inc.", "\nAttending parent-teacher meetings. Evaluating and documenting students’ progress. Allocating and grading homework, assignments, and tests.", "\n1. Bachelor’s degree in teaching or relevant field\n2. A minimum of 2 years experience as a teacher.\n3. Outstanding written and verbal communication skills.", "\nN/A")
        job40.summary()
        print (interested)
        exit()
    elif educationAndTrainingAction == 'T':
        print("\nTRAINING\n", "_"*165)
        job45 = Job ("English Communication Trainer", "Alorica Philippines", "Batangas", "\nFull Onsite-setup | ESL teachers are encouraged to apply.Create, Enhance, and Facilitate additional training courses or programs related to the Companys University for\nthe ongoing development and support of our existing employees. These training programs focus on leadership competencies and specific tools that will help develop future and current leaders in the organization.", "\n1. Call Center Agent and ESL Teachers are Welcome!\n2. College-level applicants are encouraged to apply.\n3. Relevant experience is not required, but experience as an ESL teacher or teaching English in the academe is an advantage\n4. Computer-literate with PPT, Word, Excel, Outlook, etc.\n5. Strong presentation skills.\n6. Solid research and instructional skills.\n7. Excellent English Communication Skills.\n8. Virtual assistants are encouraged to apply.","\nDental, Medical, Meal Allowance, Rice Allowance, Business Casual, Varies")
        job45.summary()
        print (interested)
        exit()
    else:
        educationAndTraining()


def computerAndIT():
    computerAndITCat = ["S. SOFTWARE", "H. HARDWARE", "N. NETWORK / SYS/ DB ADMIN"]
    computerAndITCat.sort()
    print("\n\n"," "*4,"-",computerAndITCat[0],"\n"," "*4,"-",computerAndITCat[1],"\n"," "*4,"-",computerAndITCat[2])
    computerAndITAction = input("What category?: ")
    if computerAndIT == 'H':
        print("\nHARDWARE\n", "_"*165)
        job49 =  Job("Field Service Specialist","SABPPTECH SERVICES INCORPORATED", "Batangas", "\nPerforms in house and onsite PLC programming ang troubleshooting, Performs in house and onsite PLC programming ang troubleshooting, Troubleshooting of instruments, Handles automation activities both on site and in house", "\n1. Vocational Diploma/Short Course Certificate, Bachelor's/College Degree\n2. With at least 2 years working experience as Field Service Specialist or PLC Programmer.", "Loans, Parking, Business (e.g. Shirts)")
        job49.summary()
        print (interested)
        exit()
    elif computerAndITAction == 'S':
        print("\nSOFTWARE\n", "_"*165)
        job47 =  Job("Business System Analyst","HR Network Inc.", "Batangas", "\nConsults, analyze and recommend improvements to business partners and coordinate with the programming and development teams to design effective functionalities to increase the productivity of the company's e-commerce sites.", "\n1. Consults, analyze and recommend improvements to business partners and coordinate with the programming and development teams to design effective functionalities to increase the productivity of the company's e-commerce sites.\n2. 1-4 Years Experienced Employee", "\nN/A")
        job47.summary()
        print (interested)
        exit()
    elif computerAndITAction == 'N':
        print("\n\nNETWORK / SYS/ DB ADMIN\n", "_"*165)
        job52 = Job("1. IT (Server & Support) Associate", "Honda Cars Philippines, Inc.", "Calabarzon & Mimaropa", "\nResponsible for providing service and technical assistance to all users in their network, email, device control use, and other activities that require IT supports", "\n1. Possess Bachelor’s Degree in Information Technology or a related course\n2. With at least 2 years of working experience in an IT multi-platform environment\n3. Has knowledge in OS Troubleshooting & Administration, Server Admin and Security\n4. Has knowledge in VM Ware, DNS, DHCP, SMTP, SNMP\n5. Proficient in the use of MS Office Applications (i.e., Excel, Word, PPT)\n6. Knowledgeable to drive a 4-wheel vehicle is an advantage", "\n1. Dental, Education support, Medical, Loans, Parking, Vision\n2. Meal Allowance, Shuttle Service, Gasoline Allowance, Rice Subsidy, Car Plan, Uniform")
        job52.summary()
        print (interested)
        exit()
    else:
        computerAndIT()


def engineering():
    engineeringCat = ["C. CHEMICAL", "L. ELECTRONICS / ELECTRICAL", "N. ENVIRONMENTAL", "P. PETROLEUM", "M. MECHANICAL", "I. INDUSTRIAL"]
    engineeringCat.sort()
    print("\n\n"," "*4,"-",engineeringCat[0],"\n"," "*4,"-",engineeringCat[1],"\n"," "*4,"-",engineeringCat[2],"\n"," "*4,"-",engineeringCat[3],"\n"," "*4,"-",engineeringCat[4],"\n"," "*4,"-",engineeringCat[5])
    engineeringAction = input("What category?: ")
    if engineeringAction == 'C':
        print("\nCHEMICAL\n", "_"*165)
        job54 = Job ("CHEMICAL ENGINEER", "ACS MANUFACTURING CORPORATION", "Laguna", "\nManage multiple tasks and priorities and related", "\n1. Candidate must possess at least a Bachelor's/College Degree ,Chemical Engineering or its equivalent.\n2. Must be analytic and has strong leadership skills\n3. Can work in shifting schedule\n", "\nMiscellaneous allowance, Business (e.g. Shirts,")
        job54.summary()
        print (interested)
        exit()
    elif engineeringAction == 'L':
        print("\nELECTRONICS / ELECTRICAL\n", "_"*165)
        job55 = Job ("Test and Systems Development Engineer", "Integrated Micro-Electronics, Inc", "Laguna", "\nConceptualizes, develops, integrates, tests, deploys, documents and supports customized function testers, handlers and semi & automated inspection systems.", "\nGraduate of Bachelor's Electronics Engineering (ECE) Course with at least 2 years of industry experience, knowledge of electronic test and measuring equipment, and\nanalytical skills.", "\nN/A")
        job55.summary()
        print("\nELECTRONICS / ELECTRICAL\n", "_"*165)
        job56 = Job ("ELECTRICAL ENGINEER", "Nitto Denko Philippines Corporation", "Laguna", "\nExperience in building facilities and electrical equipment repair and maintenance, ISO and PEZA documentation.", "\n1. Bachelor of Science in Electrical Engineer\n2. Strong analytical skills\n3. Basic electricity, MS Office and AutoCAD software.", "\nDental, Medical, Loans, Vision, Regular hours, Mondays - Fridays, Business (e.g. Shirts), Rice, Transportation")
        job56.summary()
        print (interested)
        exit()
    elif engineeringAction == 'N':
        print("\nENVIRONMENTAL\n", "_"*165)
        job57 = Job("Pollution Control Officer/ Engineer 3", "Pollution Control Officer/ Engineer 3", "Batangas", "\nIBIDEN PHILIPPINES, INC. is a 100% owned by IBIDEN JAPAN CO., LTD. IBIDEN is a manufacturing company producing plastic substrates and multi-layer printed circuit boards.", "\n1. Candidate must possess at least Bachelor's/College Degree in Engineering (Chemical), Engineering (Environmental/Health/Safety), Engineering (Mechanical) or equivalent.\n2. At least 5 Year(s) of working experience in the related field is required for this position.\n3. Preferably Supervisor/5 Yrs & Up Experienced Employee specialized in Engineering - Environmental/Health/Safety or equivalent.", "\nCompetitive salary merit increases company benefits and bonuses.")
        job57.summary()
        print (interested)
        exit()
    elif engineeringAction == 'P':
        print("\nPETROLEUM\n", "_"*165)
        job58 = Job("OUTPORT COORDINATOR - CALACA", "FILOIL GAS and ENERGY COMPANY, INC.", "Batangas", "\nManages lorry loading activities, coordinates with head office dispatch, coordinates with Calaca Terminal, monitors Inventory Management System software, conducts safety\nawareness, assists on Driver and Truck accreditation.", "\nBachelor's/College Degree, Professional License (Passed Board/Bar/Professional License Exam)", "\nDental, Miscellaneous allowance, Medical, Loans, Parking, Vision, Regular hours, Mondays - Fridays, Business (e.g. Shirts)")
        job58.summary()
        print (interested)
        exit()
    elif engineeringAction == 'M':
        print("\nMECHANICAL\n", "_"*165)
        job59 = Job("Facilities Engineer", "Company Confidential", "Facilities Engineer","\nThe most important idea is to ensure safety and optimal operation of machinery, systems, infrastructure, and equipment with minimal downtime.", "\nProfessional License (Passed Board/Bar/Professional License Exam)","\nN/A")
        job59.summary()
        print (interested)
        exit()
    elif engineeringAction == 'I':
        print("\nINDUSTRIAL\n", "_"*165)
        job60 = Job("Cadet Engineer", "OPTODEV, Inc.", "Batangas", "\nWill be working and leading continuous improvement projects.", "\n1. Candidate must possess at least Bachelor's/College Degree in Engineering (Chemical), Engineering (Electrical/Electronic), Engineering (Industrial), Engineering (Mechanical) or equivalent.\n2. Required Skill(s): Microsoft Office, Project Management, Process Mapping, People Management\n3. Wiling to Present Thesis/Project to the hiring managers\n4. With Less than 2 years' experience or more specialized in Engineering - Others or equivalent.", "\n1. Outstanding career growth & development opportunities\n2. Competitive salary & work benefit package\n3. Passionate, energetic & innovative work culture")
        job60.summary()
        print (interested)
        exit()
    else:
        engineering()



def manufacturing():
    manufacturingCat = ["M. MAINTENANCE", "P. PURCHASINNG & MANUFACTURING", "C. PROCESS CONTROL", "Q. QUALITY ASSURANCE"]
    manufacturingCat.sort()
    print("\n\n"," "*4,"-",manufacturingCat[0],"\n"," "*4,"-",manufacturingCat[1],"\n"," "*4,"-",manufacturingCat[2],"\n"," "*4,"-",manufacturingCat[3])
    manufacturingAction = input("What category?: ")
    if manufacturingAction == 'M':
        print("\nMAINTENANCE\n", "_"*165)
        job62 = Job("Maintenance Engineer","Yamaha Motor Philippines","Batangas","\nIn-charge of planning, setup, commissioning, trial, and completion of punch list for new equipment, lines, or facilities. Safe keeps all documents of maintenance section\nMaintenance work request, Contractor Work Permit", "\n1. Graduate of Engineering Course preferably Electrical, Electronics, Mechanical, Mechatronics or Instrumentation & Control.\n2. Fresh Graduate or at least-1 year experience in similar capacity gained from a manufacturing set-up.\n3. Could interpret some technical drawings: (AUTOCAD Drafting) Mechanical, electrical, motor control, pneumatic, hydraulic, PLC ladder.\n4. Proficient in MS Office Application.\4. Can use basic electrical and mechanical tools. Familiarity with ISO 9001, ISO 14001, & OHSAS 18001 standards.", "\nDental, Education support, Miscellaneous allowance, Medical, Loans, Sports (e.g. Gym), Parking, Business (e.g. Shirts), Insurance, Rice Subsidy, Shuttle/Transportation, Meal Allowance, Incentives")
        job62.summary()
        print (interested)
        exit()
    elif manufacturingAction == 'P':
        print("\nPURCHASINNG & MANUFACTURING\n", "_"*165)
        job64 = Job("Procurement Officer", "Knauf Gypsum Philippines, Inc.", "Batangas", "\n\n*On Importation*\nComputes for the projected raw material consumption based on plant operations’ actual consumption, historical data or sales’ projections.\n\n*On Local Purchases*\nPerforms the canvassing processes on all department’s requests and inquiries particularly on all non-trade items needed by Plant Operations.\n\n*On Purchasing Reports*\nProvides justification on each purchasing report in terms of cost or delay due to some unavoidable circumstances such as unavailability of trucks for stock delivery, stock unavailability, price difference / variance, quantity or quality related concerns and technical problems in SAP system, etc.","\nBachelor's/College Degree","\nN/A")
        job64.summary()
        print (interested)
        exit()
    elif manufacturingAction == 'C':
        print("\nPROCESS CONTROL\n", "_"*165)
        job68 = Job("Cadet Control Systems Engineer", "EXPONENT CONTROLS & ELECTRICAL CORP.","Rizal", "\nA Control Systems Engineer is responsible for designing, integrating, programming, developing, commissioning, and implementing solutions to control dynamic systems that\nconstantly change. They must have knowledge of discrete, continuous, or batch controls, networking, TCP/IP, and Windows.","\nBachelor's/College Degree", "\nHMO upon regularization")
        job68.summary()
        print (interested)
        exit()
    elif manufacturingAction == 'Q':
        print("\nQUALITY ASSURANCE\n", "_"*165)
        job70 = Job("Quality Assurance Analyst", "East-West Seed Company, Inc.", "Batangas", "\nThe QA Analyst monitors and ensures proper implementation of processes in sample preparation, seed treatment and seed testing activities including document preparation\nin accordance with Company, ISO, and ISTA standards.","\n1. Passionate to excel and grow in a company that serves small shareholder farmers\n2. Looking opportunity to work in a multinational organization\n3. Willing to work in the Batangas area","\nDental, Medical, Loans, Sports (e.g. Gym), Parking, Regular hours, Mondays - Fridays, Business (e.g. Shirts)")
        job70.summary()
        print (interested)
        exit()
    else:
        manufacturing()


    
def buildingAndConstruction():
    buildingAndConstructionCat = ["P. PROPERTY & REAL STATE", "A. ARCHITECT", "C. CIVIL"]
    buildingAndConstructionCat.sort()
    print("\n\n"," "*4,"-",buildingAndConstructionCat[0],"\n"," "*4,"-",buildingAndConstructionCat[1],"\n"," "*4,"-",buildingAndConstructionCat[2])
    buildingAndConstructionAction = input("What category?: ")
    if buildingAndConstructionAction == 'P':
        print("\nPROPERTY & REAL STATE\n", "_"*165)
        job72 = Job("Legal Documentation Associate","PTR (PETER THE ROCK) PROPERTIES, INC.", "Batangas", "\nResponsible for initial checking of Deed of Absolute Sale Clearance, preparing RFP's, assisting legal concerns, preparing Deed of Absolute Sale, Transfer of Rights and Deed of Reconveyance, following up real estate tax payments, updating clients on transfer of title status, and preparing canvass bids.","\n1. Fresh graduates with Bachelor's degrees in Business, Operations, Legal, Office Administration, Psychology.\n2. Energetic, multi-tasker, friendly, good communication skills, willing to be trained.", "\nAdditional leave, paid training, and pay raise\nCompany Christmas gift and events\nOpportunities for promotion and promotion to permanent employee")
        job72.summary()     
        print (interested) 
        exit()
    elif buildingAndConstructionAction == 'A':
        print("\nARCHITECT\n", "_"*165)
        job74 = Job("Project Architect","Delche", "Batangas", "\nDraft building plans, oversee design/construction process, prepare PRS/RFA, track progress, and submit weekly reports.", "\nBachelor's/College Degree", "n/a")
        job74.summary()   
        print (interested)  
        exit()
    elif buildingAndConstructionAction == 'C':
        print("\nCIVIL\n", "_"*165)
        job76 = Job("CIVIL ENGINEER","PACERS TRADING & SERVICES", "Batangas", "\nAn experienced civil engineer with industry knowledge is needed to develop detailed designs, do feasibility assessments,\nprepare project plans, research estimates, review regulations, monitor safety procedures, make recommendations, and manage projects.", "\n1. Bachelor's degree in civil engineering\n2. Registration/Licensure as a professional engineer is required.\n3. Having skills such as strong analytical and critical thinking, time management, leadership, and ability to coordinate with multiple projects.", "n/a")
        job76.summary()  
        print (interested) 
        exit()
    else:
        buildingAndConstruction()
 

def healthcare():
    healthcareCat = ["P. PRACTITIONER", "H. PHARMACY"]
    healthcareCat.sort()
    print("\n\n"," "*4,"-",healthcareCat[0],"\n"," "*4,"-",healthcareCat[1])
    healthcareAction = input("What category?: ")
    if healthcareAction == 'P':
        print("\nPRACTITIONER\n", "_"*165)
        job78 = Job("Company Nurse","Vacuumtech Philippines Inc. (Thermos)", "Batangas","\nCompany Doctor assists in physical examinations, monitors records, facilitates health and wellness programs, and facilitates enrolment and renewal of HMO and Group Life Insurance.", "\nCandidate must possess Nursing license and 1 year of experience.", "\nDental, Medical, Loans\nMiscellaneous allowance,Parking, Casual (e.g. T-shirts), HMO, Accident Insurance\nMeal Allowance, Uniform, Perfect Attendance Award")
        job78.summary()  
        print (interested) 
        exit()
    elif healthcareAction == 'H':
        print("\nPHARMACY\n", "_"*165)
        job79 = Job("Medical Representatives","Training and Marketing Professionals, Inc.","", "\nPromote well-known brands to health care professionals through demand-generating activities.", "\n1. Candidate must have a Bachelor's Degree\n2. 6 months of Sales experience\n3. Good communication and presentation skills.", "\nDental, Miscellaneous allowance, Medical and Loans\nRegular hours, Mondays - Fridays\nBusiness (e.g. Shirts)\nTransportation- HMO\nCommunication, Lodging, and Company Car")
        job79.summary()
        print (interested)   
        exit()
    else:
        healthcare()



def sciences():
    sciencesCat = ["A. AGRICULTURE", "S. STATISTICS", "F. FOOD TECH / NUTRITIONIST", "V. AVIATION"]
    sciencesCat.sort()
    print("\n\n"," "*4,"-",sciencesCat[0],"\n"," "*4,"-",sciencesCat[1],"\n"," "*4,"-",sciencesCat[2],"\n"," "*4,"-",sciencesCat[3])
    sciencesAction = input("What category?: ")
    if sciencesAction == 'A':
        print("\nAGRICULTURE\n", "_"*165)
        job80 = Job("Executive Driver","Merlo Agric-Vet Corporation", "", "\nExecutive Driver is responsible for transporting people and/or goods safely and on time, multitasking effectively, providing security, maintaining a vehicle inventory, driving executives to events, organizing their schedule, providing assistance with luggage, and coordinating with other staff members.", "\nCandidates must have 1 year of relevant work experience and working rights.", "\nCandidates must have 1 year of relevant work experience and working rights.")
        job80.summary()  
        print (interested)
        exit()
    elif sciencesAction == 'S':
        print("\nSTATISTICS\n", "_"*165)
        job82 = Job("R&D Analyst", "United Graphics Expression Corporation", "Cavite", "\nMust have 1 year of relevant work experience and working rights.", "\n1. BS Chemistry graduate or any allied Sciences\n2. One to three years job experiences in QA or R&D manufacturing set-up.\n3. Working experience in printing and packaging operation is advantage.\n4. Ability to make decisions with cognitive and problem solving skills.", "\nSSS, PagIbig and Philhealth\n13th month pay and Rice Subsidy every month")
        job82.summary()  
        print (interested)
        exit()
    elif sciencesAction == 'F':
        print("\nFOOD TECH / NUTRITIONIST\n", "_"*165)
        job84 = Job("R&D Food Technologist","Uni-President (Philippines) Corporation", "Batangas", "\nDesign and formulate new flavors for instant noodles, evaluate flavor submissions, design process parameters, conduct panel testing, monitor shelf-life studies, troubleshoot technical problems, coordinate with Marketing, familiarize with government regulations.", "\n1. Candidate must have BS Food Technology and R&D/QA experience.\n2. Possesses expertise in the chemistry, microbiology,a engineering, and sensory analysis of food.\n3. Talented, resourceful, innovative, creative and enthusiastic with R&D/QA experience.", "\nDental amd Medical")
        job84.summary() 
        print (interested)
        exit()
    elif sciencesAction == 'V':
        print("\nAVIATION\n", "_"*165)
        job86 = Job("Repairs Technician","Collins Aerospace PH", "Batangas", "\nThe most important details are to perform teardowns, overhauls, and functional testing of interior aircraft components, maintain appropriate documentation, respect contractual deadlines, obtain training, understand legal obligations, inform supervision, facilitate training, perform simple machining operations, interact with others, communicate effectively with management, maintain a clean and safe work area, use protective equipment.", "\n1. a two-year college or technical school associate's degree, or its equivalent\n2. Awareness of airline and aerospace maintenance procedures", "\nDental, Education support and Medical\nParking and Shuttle Transport Service\nFree Meals, Life Insurance and Retirement Benefit\nPolo Shirt (Provided)\nCombined Saturdays/Shifting and Regular Hours")
        job86.summary()
        print (interested)
        exit()
    else:
        sciences()

interested = "\nIf interested, email your resume here <futurejob@gmail.com> with subject of job position\n"
print (interested)