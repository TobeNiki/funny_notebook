package bfCompiler

import (
	"bufio"
	"os"
	"strings"
)

type brainfuckResource struct {
	memory  [30000]int
	address int
}

type codeInfomation struct {
	head        int
	splitCode   []string
	length      int
	count       int
	errorMsg    string
	errorStatus int
}

type compiled struct {
	result string
}

func resoucrceInit(bf *brainfuckResource) {
	bf.address = 0
	for i := 0; i < 30000; i++ {
		bf.memory[i] = 0
	}
}

func infomationInit(code *codeInfomation, text string) {
	code.head = 0
	code.splitCode = strings.Split(text, "")
	code.length = len(code.splitCode)
	code.errorMsg = ""
	code.errorStatus = 0
}

func inc(bf *brainfuckResource) {
	bf.memory[bf.address]++
}

func dec(bf *brainfuckResource) {
	bf.memory[bf.address]--
}

func fore(bf *brainfuckResource, code *codeInfomation) {
	bf.address++
	if bf.address > 30000 {
		code.errorMsg = "overflow!"
		code.errorStatus = 1
	}
}

func back(bf *brainfuckResource, code *codeInfomation) {
	if bf.address == 0 {
		code.errorMsg = "Can't decrement anymore"
		code.errorStatus = 2
	}
	bf.address--
}

func begin(bf *brainfuckResource, code *codeInfomation) {
	if bf.memory[bf.address] == 0 {
		code.count = 1
		for code.count != 0 {
			code.head++
			if code.head == code.length {
				code.errorMsg = "']' is missing"
				code.errorStatus = 3
				break
			}
			if code.splitCode[code.head] == "[" {
				code.count++
			} else if code.splitCode[code.head] == "]" {
				code.count--
			}
		}
	}
}

func end(bf *brainfuckResource, code *codeInfomation) {
	if bf.memory[bf.address] != 0 {
		code.count = 1
		for code.count != 0 {
			code.head--
			if code.head < 0 {
				code.errorMsg = "'[' is missing"
				code.errorStatus = 4
				break
			}
			if code.splitCode[code.head] == "]" {
				code.count++
			} else if code.splitCode[code.head] == "[" {
				code.count--
			}
		}
	}
}

func putchar(bf *brainfuckResource, compiled *compiled) {
	compiled.result = compiled.result + string(rune(bf.memory[bf.address]))
}

func getchar(bf *brainfuckResource) {
	stdin := bufio.NewScanner(os.Stdin)
	stdin.Scan()
	text := stdin.Text()
	bf.memory[bf.address] = int(text[0])
}

// Compile param text(bfcode) return compiledText
func Compile(text string) string {
	var result string
	var bf brainfuckResource
	var code codeInfomation
	var compiled compiled
	compiled.result = ""
	resoucrceInit(&bf)
	infomationInit(&code, text)
	for code.head < code.length {

		switch code.splitCode[code.head] {
		case "+":
			inc(&bf)
		case "-":
			dec(&bf)
		case "[":
			begin(&bf, &code)
		case "]":
			end(&bf, &code)
		case ".":
			putchar(&bf, &compiled)
		case ",":
			getchar(&bf)
		case ">":
			fore(&bf, &code)
		case "<":
			back(&bf, &code)
		default:
		}
		code.head++

		if code.errorStatus != 0 {
			break
		}
	}
	if code.errorStatus == 0 {
		result = compiled.result
	} else {
		result = code.errorMsg
	}
	return result
}

/*
func main() {
	text := ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<+++++>-]<.>++++++++[<+++>-]<.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]++++++++++."
	result := Compile(text)
	fmt.Printf("%s\n", result)
	text = "+++++++++>++++++++>+++++++++++>+++>+<<<<-]>.>++.+++++++..+++.>+++++.<<+++++++++++++++.>.+++.------.--------.>+.>+."
	result = Compile(text)
	fmt.Printf("%s\n", result)
}
*/
