import os
#store months as a dictionary
mths = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
print(mths)

#get all the filenames from a dictionary
fils = dir_list = os.listdir('./')

#prints number of files found
print("Number of files: ", len(fils))

#This is the character which separates name from date
und = '_'

#loop through a  files
for i in fils:
    f1 = i  # store filename in a new variable
    pos = f1.rfind(und)    # find position of _ (underscore character)
    spli = f1[pos+1:pos+12]  # Get the next 11 characters from _
    if spli[0:3] in mths:    # we make a change only if we find the months are valid
        # Below we make the necessary change to file names
        new_str=''                  
        new_str = '-'+mths[spli[0:3]]+'-'
        new_str+=spli[4:6]
        new_str = spli[7:]+new_str
        new_fnam = f1[:pos+1]+new_str+'.txt'
        #rename the file we want to change
        os.rename(f1,new_fnam)    
#fin
    
