
def compare_lines_with_dict(input_text, dictionary):
 lines = [line.strip() for line in input_text.split('\n')]
 
 matching_values = []
 lineno=0
 notfoundlines=[]
 for line in lines:
    if line=="":
     continue
    lineno+=1
    matching_value = ""
    found_match=False
    for key in dictionary:
     if key in line:
       matching_value += dictionary[key]
       found_match=True
       break 
    if found_match==False:
       notfoundlines.append(lineno)
       matching_value += "NOT-FOUND"
       
    matching_values.append(matching_value)
    ans=matching_values[0:]
    answer="\n".join(ans)
    temp=""
    if len(notfoundlines) == 0:
      temp += "COMPLETE CONFIGURATION FETCHED"
    else:
      temp +=" These lines couldn't be fetched : "
      for FaultLiineNumber in notfoundlines:
        temp+= str(FaultLiineNumber)
        temp+=","
    
    
 return answer,temp
