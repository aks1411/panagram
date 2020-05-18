alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def contains_letter(line,letter):
    if (letter not in line):
        return 1;
    else:
        return 0;
result=0;    
for i in range(2):
    ipLine=input("Enter Line :");
    ipLineLow=ipLine.lower();
    for j in range(len(alp)):
        result=contains_letter(ipLineLow,alp[j]);
        if (result==1):
            print ("Not a panagram");
            break;
    if(result==0):    
        print("Is a panagram");        

    
        


