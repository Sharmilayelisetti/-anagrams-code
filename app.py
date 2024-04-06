string1=input("Enter a string:")
string2=input("Enter a second string:")
string1=string1.lower()
string2=string2.lower()
if len(string1)!=len(string2):
  print("Not a anagrams")
elif sorted(string1)==sorted(string2):
  print("strings are anagrams")
else:
  print("strings are not anagrams")
  