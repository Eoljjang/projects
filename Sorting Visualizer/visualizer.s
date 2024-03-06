#
# CMPUT 229 Student Submission License
# Version 1.0
#
# Copyright 2023 <student name>
#
# Redistribution is forbidden in all circumstances. Use of this
# software without explicit authorization from the author or CMPUT 229
# Teaching Staff is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 229 - Computer Organization and Architecture I at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          cmput229@ualberta.ca
#
#---------------------------------------------------------------
# CCID:                 
# Lecture Section:      
# Instructor:           
# Lab Section:          
# Teaching Assistant:   
#---------------------------------------------------------------
# 

#---------------------------------------------------------------
# GLOBAL VARIABLES FOR TESTING
# 
# IMPORTANT: 
# 	- You may not define any additional global variables
# 	- You may change the initial values of the global variables
# 	  below only to test your program
# 	- You may not, at any point in your code, load the address
# 	  or value of any global variable, for example, using the
# 	  la or lw instructions on any of the global variables
# 	- For example, do not do `la t0, numArray` or 
# 	  `lw t0, lenArray` 
#---------------------------------------------------------------
.data
.align 2
numArray:	.word 11, -1, -9, 13, 56, 29, -66, 10, 99, -37, 25, 32, -84, -81, 83, -55, 45, -65, -24, -44, -92, -96, -5, -52, 97, 49, 76, -31, 63, -12, 14, -85, 59, -19, -18, -100, 19, 61, 47, -34, 54, -57, -41, -69, -95, 23, 4, -51, -60, 71	# This is the array of numbers to sort
lenArray:	.word 50	# This is the number of elements in the array


.include "./common.s"


.text
#---------------------------------------------------------------------------------------------
# visualize_sort
#
# Description:
# 	Sorts the array of numbers and draws the sorting process on the terminal
#
# Arguments:
# 	a0: the address of the array to sort
# 	a1: the number of elements in the array
#
# Return Value:
# 	none
#
# Register Usage: See below "save registers comment"
#---------------------------------------------------------------------------------------------
visualize_sort:
	# Save registers
	addi sp, sp, -32
	sw ra, 0(sp)
	sw s0, 4(sp) # To save a0
	sw s1, 8(sp) # To save a1
	sw s2, 12(sp) # Iterator 'i'
	sw s3, 16(sp) # Iterator 'j'
	sw s4, 20(sp) # "key" element (X)
	sw s5, 24(sp) # 'j' element (array[j])
	sw s6, 28(sp) # "next" element (array[j+1])

	# Save relevant argument registers.
	mv s0, a0
	mv s1, a1

	# 1) Mark first element as sorted.
	li s2, 1 # si = 1

	# 2) Start insertion sort.
	sortStart:
		bge s2, s1, sortDone # if (i >= size) done.

		# Call draw, restore registers afterwards.
		# Note: Since I don't use rely on a2 anywhere, I don't bother saving / restoring it. All that matters is that I pass in the correct a2 value.
		mv a2, s2
		jal ra, draw

		# For slowing down program
		# li a7, 32
		# li a0, 500
		# ecall

		mv a0, s0
		mv a1, s1

		slli t0, s2, 2 # 4i
		add t0, t0, a0 # t0 = &array[i]
		lw s4, 0(t0) # s4 (key) = array[i]
		addi s3, s2, -1 # j = i - 1 (Set the 0th element is "sorted").

		comparisonStart:
			# 3.1) Comparison condition 1
			slli t1, s3, 2 # 4j
			add t1, t1, a0 # t0 = &array[j]
			lw s5, 0(t1) # s5 (j-element) = array[j]
			blt s5, s4, comparisonDone # OR if (array[j] <= key) move to next element.
			
			# 3.2) Comparison condition 2
			blt s3, zero, comparisonDone # if (j < 0) move to next element.

			# 3.3) Checks pass, compute swap & iterate.
			sw s5, 4(t1) # array[j+1] = array[j] => Check here if no work.
			addi s3, s3, -1 # j = j - 1
			jal zero, comparisonStart
		
		comparisonDone:
			sw s4, 4(t1) # array[j+1] = key => Check here if no work.

			# 4) Call draw & restore arguments afterwards. 
			# Note: Since I don't use rely on a2 anywhere, I don't bother saving / restoring it.
			addi s3, s3, 1 # Since we're inserting at array[j+1] => j+1 is the index to be highlighted.
			mv a2, s3
			jal ra, draw

			# # For slowing down program
			# li a7, 32
			# li a0, 500
			# ecall

			mv a0, s0
			mv a1, s1

			addi s2, s2, 1 # i += 1
			jal zero, sortStart
	
	sortDone:
		# NOTE: At the end, the highlighted element is the last element and the position it gets put in.
		# As a result, you SHOULDN'T expect the blue bar to be at the very end UNLESS the last value is the largest in the array.
		# Restore registers
		lw ra, 0(sp)
		lw s0, 4(sp) # To save a0
		lw s1, 8(sp) # To save a1
		lw s2, 12(sp) # Iterator 'i'
		lw s3, 16(sp) # Iterator 'j'
		lw s4, 20(sp) # "key" element (X)
		lw s5, 24(sp) # 'j' element (array[j])
		lw s6, 28(sp) # "next" element (array[j+1])
		addi sp, sp, 32

		jalr	zero, ra, 0	# return

#---------------------------------------------------------------------------------------------
# max
#
# Description:
# 	Returns the maximum value in the array
#
# Arguments:
# 	a0: the address of the array
# 	a1: the number of elements in the array
#
# Return Value:
# 	a0: the maximum value in the array
#
# Register Usage: See below the "save registers" comment.
#---------------------------------------------------------------------------------------------
max:
	# Save registers
	addi sp, sp, -20
	sw t0, 0(sp) # t0 = i = iterator
	sw t1, 4(sp) # t1 = offset
	sw s0, 8(sp) # s0 = largest
	sw s1, 12(sp) # s1 = < compare largest to >
	sw ra, 16(sp)

	li t0, 0 # i = 0
	lw s0, 0(a0) # largest = array[0]

	maxLoop:
		beq t0, a1, maxLoopDone # if (i = size of array), stop.
		
		slli t1, t0, 2 # 4i
		add t1, t1, a0 # t1 = &array[i]
		lw s1, 0(t1) # s1 = array[i]

		bgt s1, s0, newMax # if (array[i] > largest) 

		addi t0, t0, 1 # increment i
		jal zero, maxLoop 

		newMax:
			mv s0, s1 # largest = array[i] (new)
			addi t0, t0, 1 # increment i
			jal zero, maxLoop

	maxLoopDone:
		mv a0, s0 # a0 = largest 
		
		lw t0, 0(sp) # Restore registers
		lw t1, 4(sp)
		lw s0, 8(sp)
		lw s1, 12(sp)
		lw ra, 16(sp)
		addi sp, sp, 20

		jalr zero, ra, 0	# return

#---------------------------------------------------------------------------------------------
# min
#
# Description:
# 	Returns the minimum value in the array
#
# Arguments:
# 	a0: the address of the array
# 	a1: the number of elements in the array
#
# Return Value:
# 	a0: the minimum value in the array
#
# Register Usage: See below the "save registers" comment.
#---------------------------------------------------------------------------------------------
min: 
	# Save registers: Functions exactly same way as max, just change the branch condition to be less than instead of greater.
	addi sp, sp, -20
	sw t0, 0(sp) # t0 = i = iterator
	sw t1, 4(sp) # t1 = offset
	sw s0, 8(sp) # smallest
	sw s1, 12(sp) # value to check against smallest.
	sw ra, 16(sp)

	li t0, 0 # i = 0
	lw s0, 0(a0) # smallest = array[0]

	minLoop:
		beq t0, a1, minLoopDone # if (i == size of array), stop.

		slli t1, t0, 2 # 4i
		add t1, t1, a0 # &array[i]
		lw s1, 0(t1) # s1 = array[i]

		blt s1, s0, newMin # if (array[i] < smallest)

		addi t0, t0, 1 # iterate
		jal zero, minLoop # Loop

		newMin:
			addi t0, t0, 1 # iterate
			mv s0, s1 # new smallest
			jal zero, minLoop # Loop
		
	minLoopDone:
		mv a0, s0 # a0 = smallest

		lw t0, 0(sp) # Restore Registers
		lw t1, 4(sp)
		lw s0, 8(sp)
		lw s1, 12(sp)
		lw ra, 16(sp)
		addi sp, sp, 20
		jalr zero, ra, 0 # return

#---------------------------------------------------------------------------------------------
# max_range
#
# Description:
# 	Finds the maximum range possible for the array of numbers with zero bounds
# 	max_range = max(range(a), max(a)-0, 0-min(a)), where a is the array of numbers
#
# Arguments:
# 	a0: the address of the array
# 	a1: the number of elements in the array
#
# Return Value:
# 	a0: the maximum range for the array
#
# Register Usage: See below the "save registers" comment.
#---------------------------------------------------------------------------------------------
max_range:
	# Save registers
	addi sp, sp, -24
	sw ra, 0(sp) # Return address since we're calling max/min.
	sw s0, 4(sp) # s0 = save argument a0
	sw s1, 8(sp) # s1 = save argument a1
	sw s2, 12(sp) # s2 = max
	sw s3, 16(sp) # s3 = min
	sw t0, 20(sp) # t0 = use to store arithmetic && store "range" return value.

	# Call max => Save arguments in s0, s1 respectively.
	mv s0, a0
	mv s1, a1
	jal ra, max
	mv s2, a0 # s2 = max

	# Restore arguments
	mv a0, s0
	mv a1, s1

	# Call min => Arguments are already saved when we called max.
	jal ra, min
	mv s3, a0 # s3 = min

	# Restore arguments
	mv a0, s0
	mv a1, s1

	# Situation 1) Mixed Pos & Neg
	mul t0, s2, s3 # t0 = max * min
	blt t0, zero, rangeMixed # t0 < 0 = 1 is pos, 1 is neg.

	# Situation 2) All pos
	add t0, s2, s3 # t0 = max + min
	bgt t0, zero, rangePos # t0 > 0 = both are pos.

	# Situation 3) All neg
	add t0, s2, s3 # t0 = max + min
	blt t0, zero, rangeNeg # if t0 < 0 = both are neg. This works because we checked the mix condition first already.

	rangeMixed:
		sub t0, s2, s3 # range = max - min.
		jal zero, max_range_done
	rangePos:
		mv t0, s2 # range = max
		jal zero, max_range_done

	rangeNeg:
		neg s3, s3 # min * (-1) = abs(min)
		mv t0, s3 # range = abs(min)
		jal zero, max_range_done

	max_range_done:
		mv a0, t0 # a0 = range

		# restore registers
		lw ra, 0(sp)
		lw s0, 4(sp)
		lw s1, 8(sp)
		lw s2, 12(sp)
		lw s3, 16(sp)
		lw t0, 20(sp)
		addi sp, sp, 24
	
		jalr zero, ra, 0	# return

#---------------------------------------------------------------------------------------------
# separator_pos
#
# Description:
# 	Computes where the separator should be placed on the screen
#
# Arguments:
# 	a0: the address of the array
# 	a1: the number of elements in the array
#
# Return Value:
# 	a0: the position of the separator
#
# Register Usage: See under the "save registers" comment.
#---------------------------------------------------------------------------------------------
separator_pos:
	# Save registers
	addi sp, sp, -40
	sw ra, 0(sp)
	sw s0, 4(sp) # Save a0
	sw s1, 8(sp) # Save a1
	sw s2, 12(sp) # max
	sw s3, 16(sp) # min
	sw s4, 20(sp) # Max-range
	sw s5, 24(sp) # separator pos
	sw t0, 28(sp) # r (will be = 42 for this lab)
	sw t1, 32(sp) # larger_between(0, max)
	sw t2, 36(sp) # arithmetic holder

	# Save arguments & call max.
	mv s0, a0
	mv s1, a1
	jal ra, max
	mv s2, a0 # s2 = max

	# Restore arguments => arguments were already saved when we called max.
	mv a0, s0
	mv a1, s1
	jal ra, min
	mv s3, a0 # s3 = min

	# Restore arguments & call range.
	mv a0, s0
	mv a1, s1
	jal ra, max_range
	mv s4, a0 # s4 = range

	# Find max(0, max(a))
	bgt s2, zero, max_bigger # Situation 1) max > 0 ... t1 = max

	li t1, 0 # Situation 2) 0 > max ... t1 = 0
	jal zero, compute_separator

	max_bigger:
		mv t1, s2 # t1 = max
		jal zero, compute_separator

	
	compute_separator: # t1 = max(0, max(a))
		li t0, 42
		addi t0, t0, -2 # 1) t0 = (42 rows - 2)

		mul t2, t1, t0 # 2) t3 = max(0, max(a)) x (r-2)
		divu s5, t2, s4 # 3) separator_pos = t2 / range => I used "divu" cuz all of the values in the formula > 0.
		jal zero, separator_pos_done

	separator_pos_done:
		mv a0, s5 # a0 = separator_pos

		# Restore registers
		lw ra, 0(sp)
		lw s0, 4(sp) # Save a0
		lw s1, 8(sp) # Save a1
		lw s2, 12(sp) # max
		lw s3, 16(sp) # min
		lw s4, 20(sp) # Max-range
		lw s5, 24(sp) # separator pos
		lw t0, 28(sp) # r (will be = 42 for this lab)
		lw t1, 32(sp) # larger_between(0, max)
		lw t2, 36(sp) # arithmetic holder
		addi sp, sp, 40

		jalr	zero, ra, 0	# return

#---------------------------------------------------------------------------------------------
# bar_height
#
# Description:
# 	Computes the height of the bar for the given number
#
# Arguments:
# 	a0: the address of the array
# 	a1: the number of elements in the array
# 	a2: the number to compute the bar height for
#
# Return Value:
# 	a0: the height of the bar
#
# Register Usage: See under the "save registers" comment.
#---------------------------------------------------------------------------------------------
bar_height:
	# Save registers
	addi sp, sp, -32
	sw ra, 0(sp)
	sw s0, 4(sp) # save a0 here
	sw s1, 8(sp) # save a1 here
	sw s2, 12(sp) # save a2 here
	sw s3, 16(sp) # max_range
	sw s4, 20(sp) # bar_height
	sw t0, 24(sp) # Arithmetic holder 1
	sw t1, 28(sp) # Arithmetic holder 2

	# Call max_range => Save arguments
	mv s0, a0
	mv s1, a1
	mv s2, a2
	jal ra, max_range
	mv s3, a0 # s3 = max_range

	# Restore argument registers after calling max_range
	mv a0, s0
	mv a1, s1
	mv a2, s2

	# Set up arithmetic values.
	li t0, 42
	addi t0, t0, -2 # t0 = 42 - 2
	mul t1, a2, t0 # t3 = x * (r - 2) => numerator

	# Calculate bar_height. I used 'div' instead of 'divu' cuz 'x' (a2) can be pos or negative.
	div s4, t1, s3 # bar_height = (x * (r-2)) / max_range

	bar_height_done:
		mv a0, s4 # a0 = bar_height

		lw ra, 0(sp)
		lw s0, 4(sp) # save a0 here
		lw s1, 8(sp) # save a1 here
		lw s2, 12(sp) # save a2 here
		lw s3, 16(sp) # max_range
		lw s4, 20(sp) # bar_height
		lw t0, 24(sp) # Arithmetic holder 1
		lw t1, 28(sp) # Arithmetic holder 2
		addi sp, sp, 32

		jalr	zero, ra, 0	# return

#---------------------------------------------------------------------------------------------
# draw
#
# Description:
# 	Draws the array of numbers onto the terminal, 
# 	taking into account the separator and relative bar heights
#
# Arguments:
# 	a0: the address of the array to draw
# 	a1: the number of elements in the array
# 	a2: the index of element to be highlighted
#
# Return Value:
# 	none
#
# Register Usage: Please see under the "save registers" comment.
#
#---------------------------------------------------------------------------------------------
draw:
	# Save registers
	addi sp, sp, -44
	sw s0, 0(sp) # s0 = to save a0 into.
	sw s1, 4(sp) # s1 = to save a1 into.
	sw s2, 8(sp) # s2 = to save a2 into.

	sw s3, 12(sp) # s3 = row_start. (1) if positive = separator (2) if negative = separator - 1
	sw s4, 16(sp) # s4 = separator = find_separator(a0, a1)
	sw s5, 20(sp) # s5 = bar_height
	sw s6, 24(sp) # s6 = current_element being checked.
	
	sw t0, 28(sp) # t0 = offseter for array indexing.
	sw s7, 32(sp) # t1 = iterator 'i'
	sw s8, 36(sp) # t2 = color of the bar to be printed.

	sw ra, 40(sp) # save 'ra' cuz we call other functions.

	li s7, 0 # i = 0

	# Save all our argument-registers since we're gonna be calling a few functions.
	# This way we don't have to save them every time we call a function, just restore after.
	# Note: I don't save 'a3' cuz the only time we ever use it is in GLIR_PrintOVLine, and I'm not dependent on it anywhere else. + each time I call GLIR, I load my desired value into a3.
	mv s0, a0
	mv s1, a1
	mv s2, a2

	# Call s4 = separator_pos(a0, a1). 
	jal ra, separator_pos # a0 = separator
	mv s4, a0 # s4 = separator

	# Restore arg. registers
	mv a0, s0
	mv a1, s1
	mv a2, s2

	drawLoop:
		bge s7, a1, drawLoopDone # if(i = a.length)

		slli t0, s7, 2 # 4i
		add t0, t0, a0 # t0 = &array[i]
		lw s6, 0(t0) # s6 = array[i] => current_element being checked.

		# 1) Call bar_height(a0, a1, a2 = current_element). Recall we saved arg. regsiters already.
		mv a2, s6 # a2 = current_element
		jal ra, bar_height # returns a0 = bar_height
		mv s5, a0 # s5 = bar_height
		sub s5, s4, s5 # bar_height = separator - bar_height

		# Restore arg. registers.
		mv a0, s0 
		mv a1, s1 
		mv a2, s2 

		# 2) Determine the color for the element, by checking if its pos/neg.
		# 2.1) At the same time, if its pos / neg, set the row_start => CHECK THIS IF PROGRAM DOESN'T WORK AS EXPECTED.
		bgt s6, zero, posColor

		# otherwise, it's negative.
		li s8, 9 # color = 9 (green)
		addi s3, s4, 1 # row_start = separator + 1
		jal zero, isCurrent

		posColor:
			li s8, 10 # color = 10 (red)
			mv s3, s4 # row_start = separator
			jal zero, isCurrent

		# 2.2) After determining the color & row_start. Check if (current-element index = index of element to be highlighted)
		isCurrent:
			beq s7, a2, colorHighlight # if (i = a2)
			jal zero, callGLIR

		
		colorHighlight:
			li s8, 12 # overwrite color = 12 (blue)
			jal zero, callGLIR

		# 3) Finally, we draw the bar by calling GLIR_PrintOVLine
		callGLIR:
			mv a0, s7 # a0 = line_col pos = i
			mv a1, s3 # a1 = s3 = row_start
			mv a2, s5 # a2 = s5 = bar_height
			mv a3, s8 # a3 = t2 = color of line

			jal ra, GLIR_PrintOVLine 
			# temporaries change after I call GLIR_PrintOVLine. If I don't call it, t1 is as expected: 0,1,2,3... Thus, GLIR is changing temporaries.
			# as such, I converted all relevant temporaries to be saved registers

			# restore
			mv a0, s0
			mv a1, s1
			mv a2, s2

			# 4) Increment i & loop.
			addi s7, s7, 1 
			jal zero, drawLoop 

	drawLoopDone:
		# Restore registers
		lw s0, 0(sp) # s0 = to save a0 into.
		lw s1, 4(sp) # s1 = to save a1 into.
		lw s2, 8(sp) # s2 = to save a2 into.

		lw s3, 12(sp) # s3 = row_start. (1) if positive = separator (2) if negative = separator - 1
		lw s4, 16(sp) # s4 = separator = find_separator(a0, a1)
		lw s5, 20(sp) # s5 = bar_height
		lw s6, 24(sp) # s6 = current_element being checked.
		
		lw t0, 28(sp) # t0 = offseter for array indexing.
		lw s7, 32(sp) # t1 = iterator 'i'
		lw s8, 36(sp) # t2 = color of the bar to be printed.

		lw ra, 40(sp) # save 'ra' cuz we call other functions.

		addi sp, sp, 44
		jalr zero, ra, 0	# return