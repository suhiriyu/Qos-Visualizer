
def compare_lines_with_dict(input_text, dictionary):
 lines = [line.strip().lower() for line in input_text.split('\n')]
 
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
       if dictionary[key] is None :
         matching_value += " "
         found_match=True
         break
       matching_value += dictionary[key]
       found_match=True
       break 
    if found_match==False:
       notfoundlines.append(lineno)
       matching_value += "NOT-FOUND"

    
    matching_values.append(matching_value)
    while (" " in matching_values):
     matching_values.remove(" ")
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
    
    if answer == "":
     answer+="NOTE: There are no equivalent commands. You can continue without including these in input config."
 return answer,temp
