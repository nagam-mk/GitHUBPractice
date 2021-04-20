n=int(input("Enter a Number you want to convert to Words : Minimum =0 Maximum = 9900009999999.\n\n : "))#Take input in numerical

highers=["Lakh Crores","Lakh Crore","Hundred Crores","Hundred Crore","Crores","Crore","Lakhs","Lakh","Thousands","Thousand","Hundred","Hundred and"]
tens=[" "," ","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
units=[" ","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
lakhs=((n//100000)%100)
lakh=((n//100000)%100)
thousands=((n//1000)%100)
thousand=((n//1000)%100)
hundred=((n//100)%10)#Check Number of Hundreds
rest=(n%100)#Check for Tens
finalWord=""#To Store the result word

##if crores>=10 and crores <=99:
#	crore=0

if lakhs>=10 and lakhs<=99:
	lakh=0

#My Main Logic Starts Here
if lakhs>10:
    if lakhs>19:
        finalWord = finalWord + " " + tens[lakhs//10]+" "+units[lakhs%10]+" "+highers[6]
    else:
        finalWord = finalWord + " " + units[lakhs] + " " + highers[6]
if lakh>0:
    finalWord = finalWord + " " + units[lakh]+" "+highers[7]
if thousands>19 and thousands<99:
    finalWord = finalWord + " " + tens[thousands//10]+" "+units[thousands%10]+" "+highers[8]
elif thousands>9 and thousands<19:
    finalWord = finalWord + " " +units[thousands]+" "+highers[8]
else:
    finalWord = finalWord + " " + units[thousand]+" "+highers[9]
if hundred>0:
    if(hundred//100):
        finalWord=finalWord+" "+units[hundred]+" "+highers[10]
    else:
        finalWord = finalWord + " " + units[hundred] + " " + highers[11]
if rest>19:
    finalWord=finalWord+" "+tens[rest//10]+" "+units[rest%10]
else:
    finalWord = finalWord + " " + units[rest]

print(finalWord)





