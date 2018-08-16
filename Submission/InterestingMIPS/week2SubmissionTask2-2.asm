####### week 2 homework########
# Author: Shuaishuai Li
# 08 August, 2018
# Tested on MARS MIPS IDE
############################### 

.data 
	MSG2:		.asciiz 	"Success! Location:  "
	MSG4:		.asciiz 	"Fail!"
	newline:	.asciiz  	"\n"
	stringBuffer:	.space 		100
	startSgn:	.asciiz 	"Program is running. \nPlease input a String:"
	exitFlag:	.asciiz 	"?"	
.text 
	# print "Program is running..."
	li		$v0,		4
	la 		$a0,		startSgn
	syscall	
input_string:
	# read string
	li 		$v0, 		8
	la 		$a0,		stringBuffer
	li 		$a1,		100
	syscall	
	li 		$v0,		4
	la 		$a0, 		newline
	syscall	
input_character:
	# read a character
	# print newline
	li 		$v0,		12
	syscall
	move 		$s0, 		$v0
	li 		$v0,		4
	la 		$a0, 		newline
	syscall		
check_character:	
	li 		$s1, 		63
	sub 		$s3,		$s0,	$s1
	beqz 		$s3,		exit 	
	# for each char in the string
	# $t3 --> Location
	la 		$t0, 		stringBuffer
	li 		$t3, 		1
loop_entry:
	lb 		$t1,		0($t0)
	sub 		$t2, 		$t1,		$s0
	beqz 		$t2, 		print_success
	beqz 		$t1, 		print_fail
	addi 		$t3,		$t3,		1
	addi 		$t0,		$t0,		1 
	j 		loop_entry	
print_success:
	# print	"Success! Location:  "
	# print newline
	li 		$v0,		4
	la 		$a0, 		MSG2
	syscall 
	li 		$v0,		1
	move 		$a0, 		$t3
	syscall
	li 		$v0,		4
	la 		$a0, 		newline
	syscall	
	j 		input_character 
print_fail:
	# print "Fail!"
	# print newline
	li 		$v0,		4
	la 		$a0, 		MSG4
	syscall 
	li 		$v0,		4
	la 		$a0, 		newline
	syscall	
	j 		input_character 
exit:
	# terminate program run and exit
	li 		$v0,		10 	
	syscall 
	
