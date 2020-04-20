"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 25
        self.register = [0] * 25
        
        global HLT,PRN,LDI
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        pass

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            LDI, # LDI R0,8
            0b00000000,
            0b00001000,
            PRN, # PRN R0
            0b00000000,
            HLT, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
#         register = [0] * 8   # like variables R0-R7
        pc = 0 # Program Counter, the address of the current instruction
        running = True
#         print("HLT",HLT)
        while running:
            inst = self.ram[pc]

#             if inst == 0b01000111:
#                 print("Beej!")
#                 pc += 1

            if inst == LDI: # Save the register
                reg_num = self.ram[pc + 1]
                value = self.ram[pc + 2]
                self.ram_write(value,reg_num)
                pc += 3

            elif inst == PRN: # Print Register 0
                reg_num = self.ram[pc + 1]
                value = self.ram_read(reg_num)
                print(value)
                pc += 2

            elif inst == HLT: # Halt command
                running = False

            else:
                print("Unknown instruction")
                running = False

    def ram_read(self,reg_num):
        """
        Accept the address to read and return the value stored there.
        """
        value = self.register[reg_num]
        return value
    
    def ram_write(self,value,reg_num):
        """ 
        Accept a value to write, and the address to write it to.
        """
        self.register[reg_num] = value
        
        
        
        