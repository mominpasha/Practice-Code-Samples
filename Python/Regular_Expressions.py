#%%
import re
result = re.match("Momin","My name is Momin Pasha")
print(result)
#%%
result = re.search("Momin","My name is Momin Pasha")
print(result)
#%%
result.group()
result.start()
result.end()
result.span()
#%%
result = re.findall("the","The history of the great king of the kingdom of the apes lies in the east of the west of the world")
print(result)
#%%
result = re.search("\d","My name is Momin Pasha. My ID is 3301")
print(result.group(),result.span())
result = re.search("\D","My name is Momin Pasha")
print(result.group(),result.span())
result = re.search("\s","My name is Momin Pasha")
print(result.group(),result.span())
result = re.search("\S","My name is Momin Pasha")
print(result.group(),result.span())
result = re.search("\w"," My name is Momin Pasha")
print(result.group(),result.span())
result = re.search("\W","My name is Momin Pasha")
print(result.group(),result.span())
#%%
result = re.search(".","My name is Momin Pasha")#matches any charcter other than newline character
print(result.group(),result.span())
result = re.search(".","\nMy name is Momin Pasha")
print(result.group(),result.span())
#%%
#[] specifies a character class one wishes to match
result = re.search("[1$]","My name is Momin Pasha")
print(result.group(),result.span())
#%%
po = re.compile("momin") #returns a pattern object which can be used anywhere
print(re.search(po,"my name is momin pasha"))
#%%
po = re.compile("wipro")
string = "wipro wipro wipro wipro wipro"
re.split(po,string)