package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	text := "+++++++++++++++++[>++++>+++++++>+++++++>++>++++>++>++++++>++++++>++++++>++++++>++>++++++>+++++++>+++<<<<<<<<<<<<<<-]>--.>--.>---.>--.>+++++.>--.>++++++.>+++.>+++++.>-.>--.>+++.>---.>-----.>++++++++++++."
	bf := Compile_bf(text)
	fmt.Println(bf)
}

func Compile_bf(code string) string {
	var compiled_result string = ""
	var memory [30000]int
	for i := 0; i < 30000; i++ {
		memory[i] = 0
	}

	ptr := 0
	head := 0
	slicedcode := strings.Split(code, "")
	len := len(slicedcode)
	var count int
	for head < len {

		switch slicedcode[head] {
		case "+":
			memory[ptr]++
		case "-":
			memory[ptr]--
		case "[":
			if memory[ptr] == 0 {
				count = 1
				for count != 0 {
					head++
					if head == len {
						fmt.Print("']' is missing")
						os.Exit(3)
					}
					if slicedcode[head] == "[" {
						count++
					} else if slicedcode[head] == "]" {
						count--
					}
				}
			}
		case "]":
			if memory[ptr] != 0 {
				count = 1
				for count != 0 {
					head--
					if head < 0 {
						print("'[' is missing")
					}
					if slicedcode[head] == "]" {
						count++
					} else if slicedcode[head] == "[" {
						count--
					}
				}
			}
		case ".":
			compiled_result = compiled_result + string(rune(memory[ptr]))
		case ">":
			ptr++
			if ptr > 30000 {
				fmt.Print("overflow!")
				os.Exit(3)
			}
		case "<":
			if ptr == 0 {
				fmt.Print("Can't decrement anymore")
				os.Exit(3)
			}
			ptr--
		default:
		}
		head++

	}
	return compiled_result
}
