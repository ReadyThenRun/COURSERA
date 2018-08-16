####### week 2 homework########
# Author: Shuaishuai Li
# 08 August, 2018
# Tested on MARS MIPS IDE
############################### 

.data
	AZ:			.asciiz 		"Alpha ","Bravo ","Charlie ","Delta ","Echo ","Foxtrot ","Golf ","Hotel ","India ","Juliet ","Kilo ","Lima ","Mike ","November ","Oscar ","Papa ","Quebec ","Romeo ","Sierra ","Tango ","Uniform ","Victor ","Whisky ","X-ray ","Yankee ","Zulu ","\0"
	az:			.asciiz 		"alpha ","bravo ","charlie ","delta ","echo ","foxtrot ","golf ","hotel ","india ","juliet ","kilo ","lima ","mike ","november ","oscar ","papa ","quebec ","romeo ","sierra ","tango ","uniform ","victor ","whisky ","x-ray ","yankee ","zulu ","\0"
	azShift:	.word			0,7,14,23,30,36,45,51,58,65,73,79,85,91,101,108,114,122,129,137,144,153,161,169,176,184,189
	number:		.asciiz			"zero ", "First ", "Second ", "Third ", "Fourth ", "Fifth ", "Sixth ", "Seventh ","Eighth ","Nine ","\0"
	numShift:	.word 			0,6,13,21,28,36,43,50,59,67,73
	startSgn:	.asciiz 		"Program is running."
	exitSgn:	.word  			'?'
	newline:	.asciiz 		"\n"
.text
.globl main
main:
	# print "Program is running."
	li		$v0,		4
	la 		$a0,		startSgn
	syscall
	# print newline
	li		$v0,		4
	la 		$a0,		newline
	syscall
loop_detect_input:
	# clear $s0 , prepare for store input character
	# receive a input character and store it in Register $s0
	# detect if input is '?'
	move 	$s0,		$zero	
	li 		$v0,		12
	syscall
	############## logic selection ##########################
	# {$s0=='?'} ? --> exit : --> continue
	# {$s0 in {[0,9]or[A,Z]or[a,z]} ? -->'*' : --> loop_print} 
	move 	$s0,		$v0		
	li 		$s1, 		63
	sub 	$s3,		$s0,	$s1
	beqz 	$s3,		exit 	
	li 		$s1, 		123
	sub 	$s3,		$s0,	$s1
	bgez 	$s3,		print_asterisk 
	li 		$s1, 		97
	sub 	$s3,		$s0,	$s1
	bgez 	$s3,		branch_az	
	li 		$s1, 		91
	sub 	$s3,		$s0,	$s1
	bgez 	$s3,		print_asterisk	
	li 		$s1, 		65
	sub 	$s3,		$s0,	$s1
	bgez 	$s3,		branch_AZ	
	li 		$s1, 		58
	sub 	$s3,		$s0,	$s1
	bgez 	$s3,		print_asterisk		
	li 		$s1, 		48
	sub 	$s3,		$s0,	$s1
	bgez 	$s3,		branch_number	
	j print_asterisk
branch_AZ:
	li 		$s3,		65
	sub 	$s1,		$s0,		$s3
	j 		loop_AZ	
branch_az:
	li 		$s3,		97
	sub 	$s1,		$s0,		$s3
	j 		loop_az
branch_number:
	li 		$s3,		48
	sub 	$s1,		$s0,		$s3
	j 		loop_number	
loop_AZ:
	# $t0 --> loop times counter
	move 	$t0,		$s1
	la	 	$t1,		AZ
	move 	$t4, 		$zero
	la		$t2,		azShift	
	j 		loop_entry
loop_az:
	# $t0 --> loop times counter
	# $t3 --> AZ print index start point(absolute address)
	# $t4 --> AZ print index end point(absolute address)
	move 	$t0,		$s1	
	la	 	$t1,		az
	move 	$t4, 		$zero
	la		$t2,		azShift	
	j 		loop_entry
loop_number:
	# $t0 --> loop times counter
	# $t3 --> AZ print index start point(absolute address)
	# $t4 --> AZ print index end point(absolute address)
	move 	$t0,		$s1	
	la	 	$t1,		number	
	move 	$t4, 		$zero
	la		$t2,		numShift	
	j 		loop_entry	
loop_entry:	
	# $t1 <-- address of AZ | az | number
	# $t5 <-- shift value based on $t1 
	# $t3 <-- $t1 + $t5   		print start
	# $t4 <-- $t1 + $t5[next]	print end
	lw		$t5,		0($t2)	
	add 	$t3,		$t1,		$t5		
	addi	$t2,		$t2,		4	
	lw		$t6,		0($t2)
	add 	$t4,		$t1,		$t6
	beq 	$t0, 		$zero,		loop_print_head
	subi	$t0,		$t0,		1
	j 		loop_entry	
loop_print_head:
	li		$v0,		4
	la 		$a0,		newline
	syscall
loop_print:
	# print $a0 character
	# $t3 ++
	lb		$a0,		0($t3)
	beq 	$t4, 		$t3,		loop_print_outlet
	li 		$v0, 		11
	syscall		
	addi 	$t3,		$t3,		1		
	j 		loop_print
loop_print_outlet:
	li 		$v0,		4
	la 		$a0, 		newline
	syscall 
	j 		loop_detect_input
exit:	
	# terminate program run and exit
	li 		$v0,		10 	
	syscall 
print_asterisk:
	# print newline
	# print '*'
	li		$v0,		4
	la 		$a0,		newline
	syscall
	li 		$v0,		11
	li 		$a0, 		42
	syscall 
	j 		loop_print_outlet	
