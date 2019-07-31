# No.1

# principal = (1000)
# interest = (0.05)
# tax = (0.18)
# desired = (1200)

# def calculate_years(principal,interest,tax,desired):
#     year = 0
#     for item in range(3): 
#         if principal <= desired:
#             principal_data = (principal + (principal * (int(interest))) + (int(tax)))
#             year += 1
#         else :
#             break
#         print=' 0 '
#     return year
# print(calculate_years(principal,interest,tax,desired))

# ##################################################################

# principal = (1200)
# interest = (0.17)
# tax = (0.05)
# desired = (2000)

# def calculate_years(principal,interest,tax,desired):
#     year = 0
#     for item in range(4): 
#         if principal <= desired:
#             principal_data = (principal + (principal * (int(interest))) + (int(tax)))
#             year += 1
#         else :
#             break
#         print=' 0 '
#     return year
# print(calculate_years(principal,interest,tax,desired))

# No.2
# def expandedForm(x,y):
#     print(x + ' + ' + y)

# expandedForm('10','2')

# def expandedForm1(x,y):
#     print(x + ' + ' + y)

# expandedForm1('40','2')

# def expandedForm2(x,y,z):
#     print(x + ' + ' + y + ' + ' + z)

# expandedForm2('7000','300','4')

#########################################################################
#No.3
# z = ''
# for i in range(0, 9):
#     if i <= 8:
#         for j in range(0, 9):
#             if j >= 6-i:
#                 z += '*'
#             elif j <= 4:
#                 z += ' '
#             else:
#                 z += ' '
#         z += '* \n'
# print(z)