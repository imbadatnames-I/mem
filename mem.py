import math
import inspect
def decode(input,mode):
    if int(mode)==1:
        if input=="1":
            return "0"
        if input=="2":
            return "1"
        if input=="3":
            return "2"
        if input=="4":
            return "3"
        if input=="5":
            return "4"
        if input=="6":
            return "5"
        if input=="7":
            return "6"
        if input=="8":
            return "7"
        if input=="9":
            return "8"
        if input=="a":
            return "9"
        if input=="b":
            return "a"
        if input=="c":
            return "b"
        if input=="d":
            return "c"
        if input=="e":
            return "d"
        if input=="f":
            return "e"
        if input=="10":
            return "f"
        if input=="11":
            return "g"
        if input=="12":
            return "h"
        if input=="13":
            return "i"
        if input=="14":
            return "j"
        if input=="15":
            return "k"
        if input=="16":
            return "l"
        if input=="17":
            return "m"
        if input=="18":
            return "n"
        if input=="19":
            return "o"
        if input=="1a":
            return "p"
        if input=="1b":
            return "q"
        if input=="1c":
            return "r"
        if input=="1d":
            return "s"
        if input=="1e":
            return "t"
        if input=="1f":
            return "u"
        if input=="20":
            return "v"
        if input=="21":
            return "w"
        if input=="22":
            return "x"
        if input=="23":
            return "y"
        if input=="24":
            return "z"
        if input=="25":
            return "A"
        if input=="26":
            return "B"
        if input=="27":
            return "C"
        if input=="28":
            return "D"
        if input=="29":
            return "E"
        if input=="2a":
            return "F"
        if input=="2b":
            return "G"
        if input=="2c":
            return "H"
        if input=="2d":
            return "I"
        if input=="2e":
            return "J"
        if input=="2f":
            return "K"
        if input=="30":
            return "L"
        if input=="31":
            return "M"
        if input=="32":
            return "N"
        if input=="33":
            return "O"
        if input=="34":
            return "P"
        if input=="35":
            return "Q"
        if input=="36":
            return "R"
        if input=="37":
            return "S"
        if input=="38":
            return "T"
        if input=="39":
            return "U"
        if input=="3a":
            return "V"
        if input=="3b":
            return "W"
        if input=="3c":
            return "X"
        if input=="3d":
            return "Y"
        if input=="3e":
            return "Z"
        if input=="3f":
            return "!"
        if input=="40":
            return '"'
        if input=="41":
            return "#"
        if input=="42":
            return "$"
        if input=="43":
            return "%"
        if input=="44":
            return "&"
        if input=="45":
            return "'"
        if input=="46":
            return "("
        if input=="47":
            return ")"
        if input=="48":
            return "*"
        if input=="49":
            return "+"
        if input=="4a":
            return ""
        if input=="4b":
            return "-"
        if input=="4c":
            return "."
        if input=="4d":
            return "/"
        if input=="4e":
            return ":"
        if input=="4f":
            return ";"
        if input=="50":
            return "<"
        if input=="51":
            return "="
        if input=="52":
            return ">"
        if input=="53":
            return "?"
        if input=="54":
            return "@"
        if input=="55":
            return "["
        if input=="56":
            return "\\"
        if input=="57":
            return "]"
        if input=="58":
            return "^"
        if input=="59":
            return "_"
        if input=="5a":
            return "`"
        if input=="5b":
            return "{"
        if input=="5c":
            return "|"
        if input=="5d":
            return "}"
        if input=="5e":
            return "~"
        if input=="5f":
            return " "
        else:
            return "☒"
    if int(mode)==2:
        input="0x"+input
        input=int(input,16)
        return input
def encode(input,mode):
    if int(mode)==1:
        if input=="0":
            return "1"
        if input=="1":
            return "2"
        if input=="2":
            return "3"
        if input=="3":
            return "4"
        if input=="4":
            return "5"
        if input=="5":
            return "6"
        if input=="6":
            return "7"
        if input=="7":
            return "8"
        if input=="8":
            return "9"
        if input=="9":
            return "a"
        if input=="a":
            return "b"
        if input=="b":
            return "c"
        if input=="c":
            return "d"
        if input=="d":
            return "e"
        if input=="e":
            return "f"
        if input=="f":
            return "10"
        if input=="g":
            return "11"
        if input=="h":
            return "12"
        if input=="i":
            return "13"
        if input=="j":
            return "14"
        if input=="k":
            return "15"
        if input=="l":
            return "16"
        if input=="m":
            return "17"
        if input=="n":
            return "18"
        if input=="o":
            return "19"
        if input=="p":
            return "1a"
        if input=="q":
            return "1b"
        if input=="r":
            return "1c"
        if input=="s":
            return "1d"
        if input=="t":
            return "1e"
        if input=="u":
            return "1f"
        if input=="v":
            return "20"
        if input=="w":
            return "21"
        if input=="x":
            return "22"
        if input=="y":
            return "23"
        if input=="z":
            return "24"
        if input=="A":
            return "25"
        if input=="B":
            return "26"
        if input=="C":
            return "27"
        if input=="D":
            return "28"
        if input=="E":
            return "29"
        if input=="F":
            return "2a"
        if input=="G":
            return "2b"
        if input=="H":
            return "2c"
        if input=="I":
            return "2d"
        if input=="J":
            return "2e"
        if input=="K":
            return "2f"
        if input=="L":
            return "30"
        if input=="M":
            return "31"
        if input=="N":
            return "32"
        if input=="O":
            return "33"
        if input=="P":
            return "34"
        if input=="Q":
            return "35"
        if input=="R":
            return "36"
        if input=="S":
            return "37"
        if input=="T":
            return "38"
        if input=="U":
            return "39"
        if input=="V":
            return "3a"
        if input=="W":
            return "3b"
        if input=="X":
            return "3c"
        if input=="Y":
            return "3d"
        if input=="Z":
            return "3e"
        if input=="!":
            return "3f"
        if input=='"':
            return "40"
        if input=="#":
            return "41"
        if input=="$":
            return "42"
        if input=="%":
            return "43"
        if input=="&":
            return "44"
        if input=="'":
            return "45"
        if input=="(":
            return "46"
        if input==")":
            return "47"
        if input=="*":
            return "48"
        if input=="+":
            return "49"
        if input=="":
            return "4a"
        if input=="-":
            return "4b"
        if input==".":
            return "4c"
        if input=="/":
            return "4d"
        if input==":":
            return "4e"
        if input==";":
            return "4f"
        if input=="<":
            return "50"
        if input=="=":
            return "51"
        if input==">":
            return "52"
        if input=="?":
            return "53"
        if input=="@":
            return "54"
        if input=="[":
            return "55"
        if input=="\\":
            return "56"
        if input=="]":
            return "57"
        if input=="^":
            return "58"
        if input=="_":
            return "59"
        if input=="`":
            return "5a"
        if input=="{":
            return "5b"
        if input=="|":
            return "5c"
        if input=="}":
            return "5d"
        if input=="~":
            return "5e"
        else:
            return "5f"
    if int(mode)==2:
        input=hex(input).split("x")
        return input[1]
def de_adr(adr):
    adr=adr.split("x")
    return f"{adr[0]}",f"{adr[1]}"
def read_mem(address,decode_mode):
    adr_line,adr=de_adr(address)
    with open("memory","r") as file:
        mem=file.readlines()
    adr_line=int(adr_line,16)
    adr=int(adr,16)
    try:
        mem_line=mem[adr_line-1] # sets the list with all 8 items of a line value adr_line-1 in the memory file
    except:
        frame = inspect.currentframe().f_back
        lineno = frame.f_lineno
        print(f"error in line {lineno}\nerror: the adr {address} doesn't exist try make sure the memory file exists and the line of memory exists as well.\nexiting...")
        exit()
    mems=mem_line.split("  ")
    memr=[]
    i=1
    try:
        while i<=16:
            memr.append(mems[0][i-1])
            i+=1
        while memr[len(memr)-1]=="0":
            memr.pop(len(memr)-1)
        while len(memr)>1:
            memr[0]=memr[0]+memr[1]
            memr.pop(1)
        return decode(memr[0],decode_mode)
    except:
        frame = inspect.currentframe().f_back
        lineno = frame.f_lineno
        print(f"error in line {lineno}\nerror: the adr {address} doesn't exist try make sure the memory file exists and the line of memory exists as well.\nreading address: {hex(adr_line)},{hex(adr-8*math.trunc(adr/8))}")
        return mems[adr-1-8*math.trunc(adr/8)]
def write_mem(address,write,decode_mode):
    adr_line,adr=de_adr(address)
    write=encode(write,decode_mode)
    while len(str(write))<16:
        write=str(write)+"0"
    with open("memory","r") as file:
        mem=file.readlines()
    try:
        mem_line=mem[int(adr_line)-1] # sets the list with all 8 items of a line value adr_line-1 in the memory file
    except:
        frame = inspect.currentframe().f_back
        lineno = frame.f_lineno
        print(f"error in line {lineno}\nerror: the adr {address} doesn't exist try make sure the memory file exists and the line of memory exists as well.\nexiting...")
        exit()
    mems=mem_line.split("  ")
    mems[int(adr)-1]=write
    while len(mems)>1:
                mems[0]=str(mems[0])+"  "+str(mems[1])
                mems.pop(1)
    mems=mems[0]
    mem[int(adr_line)-1]=mems
    try:
        mems=mem_line.split("  ")
        mems[int(adr)-1]=write
        while len(mems)>1:
                mems[0]=str(mems[0])+"  "+str(mems[1])
                mems.pop(1)
        mems=mems[0]
        mem[int(adr_line)-1]=mems
        while len(mem)>1:
                    mem[0]=mem[0]+mem[1]     
                    mem.pop(1)
                    with open("memory","w") as file:
                        file.write((mem[0]))
    except:
        frame = inspect.currentframe().f_back
        lineno = frame.f_lineno
        print(f"error in line {lineno}\nerror: the adr {address} doesn't exist try make sure the memory file exists and the line of memory exists as well.\nexiting....")
        exit()
def extend_mem(eleng):
    try:
        with open("memory","r") as file:
            mem=file.readlines()
        if len(mem)>1:
            while eleng>0:
                with open("memory","a") as file:
                    file.write("\n0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000")
                eleng-=1
        else:
            with open("memory","a") as file:
                file.write("0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000")
                while eleng>1:
                    file.write("\n0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000")
                    eleng-=1
    except:
        frame = inspect.currentframe().f_back
        lineno = frame.f_lineno
        print(f"error in line {lineno}\nerror: the memory file doesn't exist.\nexiting...")
        exit()
def clear_mem(mem_len):
        with open("memory","w") as file:
            file.write("0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000")
            while mem_len>1:
                file.write("\n0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000  0000000000000000")
                mem_len-=1
def alu(inpt,inpt2,op):
    if op=="+":
        return int(inpt)+int(inpt2)
    if op=="-":
        return int(inpt)-int(inpt2)
    if op=="*":
        return int(inpt)*int(inpt2)
    if op=="/":
        return int(inpt)/int(inpt2)
__doc__="""not done"""