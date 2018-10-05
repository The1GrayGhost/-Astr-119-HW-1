#def a func
def flow_control(k):

	#def a string based on the vakue of k
	if(k==0):
		s="Variable k = %d equals 0." % k
	elif(k==1):
		s="Variable k = %d equals 1." % k
	else:
		s="Variable k = %d does not equal 0 or 1" % k

	#print the variable
	print(s)
	
#def a main func	
def main():

	#declare an integer
	i=0
	
	#try flow_control for 0,1,2
	flow_control(i)
	i=1
	flow_control(i)
	i=2
	flow_control(i)
	
#run the program	
if __name__=="__main__":
	main()			