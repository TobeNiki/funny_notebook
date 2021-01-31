import sys

class Brain:
    def __init__(self):
        self.compiled_result = ""

    def inc(self):
        self.mem[self.ptr] += 1

    def dec(self):
        self.mem[self.ptr] -= 1

    def fore(self):
        self.ptr += 1
        if self.ptr > len(self.mem):
            print("overflow!")
            sys.exit(1)

    def back(self):
        if self.ptr == 0:
            print("Can't decrement anymore")
        self.ptr -= 1

    def putc(self):
        # chr: char -> code point
        #print(chr(self.mem[self.ptr]), end="")  # no line break
        self.compiled_result += chr(self.mem[self.ptr])

    def getc(self):
        # ord: code point -> char
        self.mem[self.ptr] = ord(sys.stdin.buffer.read(1))

    def begin(self):
        if self.mem[self.ptr] == 0:
            nest = 1
            while nest != 0:
                self.head += 1
                if self.head == len(self.code):
                    print("']' is missing")
                    sys.exit(1)
                if self.code[self.head] == '[':
                    nest += 1
                elif self.code[self.head] == ']':
                    nest -= 1

    def end(self):
        if self.mem[self.ptr] != 0:
            nest = 1
            while nest != 0:
                self.head -= 1
                if self.head < 0:
                    print("'[' is missing")
                if self.code[self.head] == ']':
                    nest += 1
                elif self.code[self.head] == '[':
                    nest -= 1

    def nop(self):
        pass  # ignore other symbol

    def fuck(self, code, mem_size=30000):
        operations = {
            "+": self.inc,    # increment the value at the pointer.
            "-": self.dec,    # decrement the value at the pointer.
            ">": self.fore,   # increment the pointer.
            "<": self.back,   # decrement the pointer.
            "[": self.begin,  # if the byte at the pointer is zero, then jump it to the matching ']'
            "]": self.end,    # if the byte at the pointer is nonzero, then jump it buck to the matching '['
            ".": self.putc,   # output the value at the  pointer as utf-8 character.
            ",": self.getc,   # accept one byte of input, storing its value in the mem at the  pointer.
        }
        self.code = code
        self.mem = [0] * mem_size
        self.ptr = 0
        self.head = 0
        while self.head < len(code):
            operations.get(code[self.head], self.nop)()
            self.head += 1
        
        return self.compiled_result.strip()


def sourcecode_compiled(code:str) -> str:
    """
    args = sys.argv
    if len(args) < 2:
        code = sys.stdin.read()
    else:
        path = args[1]
        with open(path) as f:
            code = f.read()
    """
    #code = "+++++++++++++++++[>++++>+++++++>++++++>++++++>++>+++++++>++>++++++>+++++++>++++++>++++++>++++++>++<<<<<<<<<<<<<-]>++.>-----.>-.>++++++++.>+++++.>----.>--.>----.>-----.>-----.>+++.>++++++++.>--.>++++++++++++."
    return Brain().fuck(code)

if __name__ == "__main__":
    pass