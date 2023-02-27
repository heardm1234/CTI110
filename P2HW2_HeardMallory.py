#CTI-110
#P2HW2-List
#Mallory Heard
#26 FEB 23
#
myList = []

for i in range(6):
    a = float(input('Enter grade for Module '+str(i+1)+': '))
    myList.append(a)
  
#print list
print('\n\n----------Results----------')
print('Lowest Grade:      '+str(min(myList)))
print('Highest Grade:     '+str(max(myList)))
print('Sum of Grades:     '+str(sum(myList)))
Average = sum(myList)/len(myList)
print(f'Average:           {Average:.2f} ')
print('---------------------------------')

