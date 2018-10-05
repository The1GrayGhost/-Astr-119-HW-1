#string

s="I am a string"
print(type(s))       #will say str

yes=True			#Boolean True
print(type(yes))

no=False			#Boolean False
print(type(no))

#lists -- ordered and changeable

alpha_list=["a", "b", "c"]	#list initialization
print(type(alpha_list))		#will say tuple
print(type(alpha_list[0]))	#will say string
alpha_list.append("d")		#will add "d" to the list end
print(alpha_list)			#will print list

#tuple -- ordered and unchangeable

alpha_tuple=("a", "b", "c")	#tuple initialization	
print(type(alpha_tuple))	#will sau tuple

try: 						
	alpha_tuple[2]="d"		#attempt initialization
except TypeError:			#won't work and will raise TypeError
	print("We can't add elements to tuples!")	#print this message
print(alpha_tuple)			#will print tuple