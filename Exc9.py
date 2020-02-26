# This is your main function
# This is where you declare your variables and use your functions
def main():
	distance = 10 
	speed = 1
	distance_covered = 0
	while(distance_covered < distance):
		print(distance_covered) 
		distance_covered= distance_covered + speed
	print("you are finished")

# Call your main function	
if __name__ == "__main__": 
	main()
