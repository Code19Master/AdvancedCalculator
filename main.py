from colorama import Fore
from time import sleep
from os import system

print(
    "*NOTE* When you do cube root of 64, you will get 3.9999999999999996. While this is also correct, round up and use 4. Also, the results for the last four operations may be a long decimal. It is preferable to round for this too. \n \n "
)
print(Fore.LIGHTYELLOW_EX + "Software downloaded." + Fore.LIGHTBLUE_EX +
      " System waking up.")
print(Fore.BLUE + "\nMade By Divik Babbar\n" + Fore.WHITE + " ")
sleep(2)
dddddd = 1
while dddddd < 100:

	print(
	    Fore.BLUE +
	    " \n\n 1. addition\n 2. subtraction\n 3. multiplication\n 4. division\n 5. square\n 6. square root\n 7. cube\n 8. cube root\n 9. diameter and radius\n 10.circumfrence\n 11.area and perimeter rectangles\n 12.area of circles\n 13.Area of Triangles\n 14.Area of Trapezoids\n 15.modulus\n 16.exponents\n 17.Volume of Spheres\n 18.Volume of triangular prisms\n 19.Volume of trapazoidal prisms\n 20.Volume of rectangular prisms\n 21.Celcius to Farenheit\n 22.Farenheight to celcius\n 23.Feet to meters\n 24.Meters to feet\n"
	)
	opt = input(Fore.GREEN + "\nChoose a number from the" + Fore.YELLOW +
	            " list" + Fore.GREEN + ": " + Fore.LIGHTMAGENTA_EX)
	if (opt == str):
		print("Hey, that isn't a number!")
	elif (opt == "1") or (opt == "1."):
		num1 = float(input(Fore.LIGHTGREEN_EX + "\nPick your  first number: "))
		num2 = float(input(Fore.LIGHTBLUE_EX +
		                   "\nPick your   second number: "))
		print(Fore.YELLOW + "\n", num1 + num2)


	elif (opt == "2") or (opt == "2."):
		num3 = float(input(Fore.LIGHTGREEN_EX +
		                   "\nSelect your first number: "))
		num4 = float(input(Fore.LIGHTBLUE_EX +
		                   "\nSelect your second number: "))
		print(Fore.YELLOW + "\n", num3 - num4)
  

	elif (opt == "3") or (opt == "3."):
		num5 = float(input(Fore.LIGHTGREEN_EX + "\nChoose a multiplicand: "))
		num6 = float(input(Fore.LIGHTBLUE_EX + "\nChoose a multiplier: "))
		print(Fore.YELLOW + "\n", num5 * num6)

	elif (opt == "4") or (opt == "4."):
		num7 = float(input(Fore.LIGHTGREEN_EX + "\nChoose a dividend: "))
		num8 = float(input(Fore.LIGHTBLUE_EX + "\nChoose a divisor: "))
		quote = (num7 / num8)
		print(Fore.YELLOW + "\n", quote)

	elif (opt == "5") or (opt == "5."):
		num9 = float(input(Fore.LIGHTGREEN_EX + "\nSelect a number: "))
		sq = num9 * num9
		print(Fore.YELLOW + "\nYour number squared is ", sq)

	elif (opt == "6") or (opt == "6."):
		num10 = float(input(Fore.LIGHTGREEN_EX + "\nenter a number: "))
		sqrt = num10**0.5
		print(Fore.YELLOW + "\nThe square root of your number is", sqrt)

	elif (opt == "7") or (opt == "7."):
		num11 = float(input(Fore.LIGHTGREEN_EX + "\nInput a number: "))
		cb = num11**3
		print(Fore.YELLOW + "\nYour number cubed is", cb)

	elif (opt == "8") or (opt == "8."):
		num12 = float(input(Fore.LIGHTGREEN_EX + "\nChoose a number: "))
		cbrt = num12**0.33333333333333334
		print(Fore.YELLOW + "\nThe cube root of your number is", cbrt)

	elif (opt == "9") or (opt == "9."):
		c = float(input(Fore.LIGHTGREEN_EX + "\nInput the circumfrence: "))
		d = c / 3.1415926535
		r = c / 6.283185307
		print(Fore.YELLOW + "\nYour diameter is: ", d)
		print(Fore.YELLOW + "\nYour radius is:", r)

	elif (opt == "10") or (opt == "10."):
		r2 = float(input(Fore.LIGHTGREEN_EX + "\nInput your radius: "))
		circfind = r2 * 6.283185307
		print(Fore.YELLOW + "\nThe circumfrence is ", circfind)

	elif (opt == "11") or (opt == "11."):
		arsq = float(input(Fore.LIGHTGREEN_EX + "\nWhat is the length? "))
		arsq2 = float(input(Fore.LIGHTBLUE_EX + "\nWhat is the width? "))
		mathfind = arsq * arsq2
		perm = arsq * 2
		perm2 = arsq2 * 2
		permfind = perm + perm2
		print(Fore.YELLOW + "\nThe area is", mathfind)
		print(Fore.YELLOW + "\nThe perimeter is", permfind)

	elif (opt == "12") or (opt == "12."):
		circar = float(input(Fore.LIGHTGREEN_EX + "\nWhat is the radius? "))
		step1 = circar**2
		step2 = step1 * 3.1415926535
		print(Fore.YELLOW + "\nThe circle's area is", step2)

	elif (opt == "13") or (opt == "13."):
		tng1 = float(input(Fore.LIGHTGREEN_EX + "\nInput the base: "))
		tng2 = float(input(Fore.LIGHTBLUE_EX + "\nInput the height: "))
		sap1 = tng1 * tng2
		sap2 = sap1 / 2
		print(Fore.YELLOW + "\nThe triangle's area is", sap2)

	elif (opt == "14") or (opt == "14."):
		trapb1 = float(
		    input(Fore.LIGHTGREEN_EX +
		          "\nWhat is the length of the first base? "))
		trapb2 = float(
		    input(Fore.LIGHTBLUE_EX +
		          "\nWhat is the length of the second base? "))
		traph1 = float(input(Fore.LIGHTRED_EX + "\nWhat is the height? "))
		findtrap1 = (trapb1 + trapb2) / 2
		findtrap2 = findtrap1 * traph1
		print(Fore.YELLOW + "\nThe area is", findtrap2)

	elif (opt == "15") or (opt == "15."):
		mod1 = float(input(Fore.LIGHTGREEN_EX + "\nSelect the dividend: "))
		mod2 = float(input(Fore.LIGHTBLUE_EX + "\nSelect your divisor: "))
		modulusend = mod1 % mod2
		print(Fore.YELLOW + "\n The modulus is", modulusend)

	elif (opt == "16") or (opt == "16."):
		exp = float(input(Fore.LIGHTGREEN_EX + "\nWhat will your number be? "))
		power = float(
		    input(Fore.LIGHTBLUE_EX + "\nWhat power are you putting it to? "))
		finalq = exp**power
		print(Fore.YELLOW + "\nThe result is", finalq)

	elif (opt == "17") or (opt == "17."):
		volr = float(
		    input(Fore.LIGHTGREEN_EX + "\nWhat is the sphere's radius? "))
		frthrds = (4 / 3) * 3.1415926535
		sphvol = frthrds * (volr**3)
		print(Fore.YELLOW + "\nThe sphere's volume is", sphvol)

	elif (opt == "18") or (opt == "18."):
		triv1 = float(
		    input(Fore.LIGHTGREEN_EX + "\nWhat is the length of the base? "))
		triv2 = float(input(Fore.LIGHTBLUE_EX + "\nWhat is the width? "))
		triv3 = float(input(Fore.LIGHTRED_EX + "\nWhat is the altitude? "))
		findtriv1 = (triv1 * triv2) * triv3
		findtriv2 = findtriv1 / 2
		print(Fore.YELLOW + "\nThe volume is", findtriv2)

	elif (opt == "19") or (opt == "19."):
		trap1 = float(
		    input(Fore.LIGHTGREEN_EX +
		          "\nWhat is the width of the 1st base? "))
		trap2 = float(
		    input(Fore.LIGHTBLUE_EX + "\nWhat is the width of the 2nd base? "))
		trap3 = float(input(Fore.LIGHTRED_EX + "\nWhat is the height? "))
		trap4 = float(input(Fore.WHITE +
		                    "\nWhat is the length of the prism? "))
		findtrapv1 = (trap1 + trap2) * trap3
		findtrapv2 = findtrapv1 / 2
		findtrapv3 = findtrapv2 * trap4
		print(Fore.YELLOW + "\nThe volume is ", findtrapv3)

	elif (opt == "20") or (opt == "20."):
		recp1 = float(input(Fore.LIGHTGREEN_EX + "\nWhat is the length? "))
		recp2 = float(input(Fore.LIGHTBLUE_EX + "\nWhat is the width? "))
		recp3 = float(input(Fore.LIGHTRED_EX + "\nWhat is the height? "))
		findrecp1 = (recp1 * recp2) * recp3
		print(Fore.YELLOW + "\nThe volume is ", findrecp1)

	elif (opt == "21") or (opt == "21."):
		ctf1 = float(
		    input(Fore.LIGHTGREEN_EX +
		          "\nWhat is the temperature in Celcius? "))
		ctf2 = 9 / 5
		ctf3 = ctf1 * ctf2
		ctf4 = ctf3 + 32
		print(Fore.YELLOW + "\nThe temperature in Farenheit is ", ctf4)

	elif (opt == "22") or (opt == "22."):
		ftc = float(
		    input(Fore.LIGHTGREEN_EX +
		          "\nWhat is the temperature in Farenheit? "))
		ftc2 = ftc - 32
		ftc3 = 5 / 9
		ftc4 = ftc2 * ftc3
		print(Fore.YELLOW + "\nThe temperature in Celcius is ", ftc4)

	elif (opt == "23") or (opt == "23."):
		ftm = float(
		    input(Fore.LIGHTGREEN_EX + "\nWhat is the length in feet? "))
		ftm2 = ftm / 3.28084
		print(Fore.YELLOW + "\nThe length in meters is", ftm2)

	elif (opt == "24") or (opt == "24."):
		mtf = float(
		    input(Fore.LIGHTGREEN_EX + "\nWhat is the length in meters? "))
		mtf2 = mtf * 3.28084
		print(Fore.YELLOW + "\nThe length in feet is", mtf2)

	else:
		print("There has been an error. Please try again.")

	sleep(5)
	system("clear")
dddddd += 1
sleep(1)
print(Fore.LIGHTMAGENTA_EX + "\n\nI hope you enjoyed! Rerun to use again.")
print(Fore.CYAN + "\nAN UPDATE WILL COME SOON!")