import re


str1 = "HE SAID HE'S RICH, but that's not to be believed."
# newStr = re.sub('[A-Z]','',str1)
newStr = re.sub('[A-Za-z," ",.,\']','',str1)
print(newStr)