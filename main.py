def parser(sentence):
  tokens = sentence.lower().split()
  tokens.append("EOS")

  # symbols definiton
  non_terminals = ["S", "NN", "VB"]
  terminals = ['ahu','nasida','tahuluk','hami','huting','hoda','lomo','manuhor','mida']

  # parse table definition
  parse_table = {}

  # S
  parse_table[("S", "ahu")] = ["NN", "VB", "NN"]
  parse_table[("S", "nasida")] = ["NN", "VB", "NN"]
  parse_table[("S", "tahuluk")] = ["NN", "VB", "NN"]
  parse_table[("S", "hami")] = ["NN", "VB", "NN"]
  parse_table[("S", "huting")] = ["NN", "VB", "NN"]
  parse_table[("S", "hoda")] = ["NN", "VB", "NN"]
  parse_table[("S", "lomo")] = ["NN", "VB", "NN"]
  parse_table[("S", "manuhor")] = ["error"]
  parse_table[("S", "mida")] = ["error"]
  parse_table[("S", "EOS")] = ["error"]


  # NN
  parse_table[("NN", "ahu")] = ["ahu"]
  parse_table[("NN", "nasida")] = ["nasida"]
  parse_table[("NN", "tahuluk")] = ["tahuluk"]
  parse_table[("NN", "hami")] = ["hami"]
  parse_table[("NN", "huting")] = ["huting"]
  parse_table[("NN", "hoda")] = ["hoda"]
  parse_table[("NN", "lomo")] = ["lomo"]
  parse_table[("NN", "manuhor")] = ["error"]
  parse_table[("NN", "mida")] = ["error"]
  parse_table[("NN", "EOS")] = ["error"]


  # VB
  parse_table[("VB", "ahu")] = ["error"]
  parse_table[("VB", "nasida")] =["error"]
  parse_table[("VB", "tahuluk")] = ["error"]
  parse_table[("VB", "hami")] = ["error"]
  parse_table[("VB", "huting")] = ["error"]
  parse_table[("VB", "hoda")] = ["error"]
  parse_table[("VB", "lomo")] = ["lomo"]
  parse_table[("VB", "manuhor")] = ["manuhor"]
  parse_table[("VB", "mida")] = ["mida "]
  parse_table[("VB", "EOS")] = ["error"]


  # stack initialization
  stack = []
  stack.append("#")
  stack.append("S")

  # input reading initialization
  idx_token = 0
  symbol = tokens[idx_token]

  # parsing process
  while len(stack) > 0:
      top = stack[len(stack) - 1]
      print("top = ", top)
      print("symbol = ", symbol)
      if top in terminals:
          print("top adalah simbol terminal")
          if top == symbol:
              stack.pop()
              idx_token = idx_token + 1
              symbol = tokens[idx_token]
              if symbol == "EOS":
                  print("ini stack: ", stack)
                  stack.pop()
          else:
              print("error")
              break
      elif top in non_terminals:
          print("top adalah simbol non-terminal")
          if parse_table[(top, symbol)][0] != "error":
              stack.pop()
              symbols_to_be_pushed = parse_table[(top, symbol)]
              for i in range(len(symbols_to_be_pushed) - 1, -1, -1):
                  stack.append(symbols_to_be_pushed[i])
          else:
              print("error")
              break
      else:
          print("error")
          break
      print("isi stack:", stack)
      print()

  # conclusion
  print()
  if symbol == "EOS" and len(stack) == 0:
      print("input string ", sentence, " diterima, sesuai Grammar")
  else:
      print("Error input string: ", sentence, " tidak diterima, tidak sesuai Grammar")

def lexicalAnalyzer(kataInput):
  import string

  input_string = kataInput.lower() + "#"

  # initialization
  alphabet_list = list(string.ascii_lowercase)
  state_list = [
      "q0",
      "q1",
      "q2",
      "q3",
      "q4",
      "q5",
      "q6",
      "q7",
      "q8",
      "q9",
      "q10",
      "q11",
      "q12",
      "q13",
      "q14",
      "q15",
      "q16",
      "q17",
      "q18",
      "q19",
      "q20",
      "q21",
      "q22",
      "q23",
      "q24",
      "q26",
      "q27",
      "a1",
      "a2",
      "a3",
      "a4",
      "a5",
      "a6",
      "a7",
      "a8",
      "a9",
      "a10",
      "a11",
      "a12",
      "a13",
      "a14",
  ]

  transition_table = {}

  for i in state_list:
      for alphabet in alphabet_list:
          transition_table[(i, alphabet)] = "ERROR"
      transition_table[(i, "#")] = "ERROR"
      transition_table[(i, " ")] = "ERROR"

  # Finish state
  transition_table[("q27","#")] = "ACCEPT"
  transition_table[("q27"," ")] = "q27"
  transition_table[('q27','a')]= 'q26'
  transition_table[('q27','t')]= 'q4'
  transition_table[('q27','h')]= 'q11'
  transition_table[('q27','n')]= 'q20'
  transition_table[('q27','l')]= 'a1'
  transition_table[('q27','m')]= 'a5'

  #  ahu
  transition_table[("q0","a")] = "q26"
  transition_table[('q26','h')]= 'q1'
  transition_table[('q1','u')]= 'q2'
  transition_table[('q2','#')]= 'ACCEPT'
  transition_table[('q2',' ')]= 'q27'


  # string "nasida"
  transition_table[("q0","n")] = "q20"
  transition_table[('q20','a')]= 'q21'
  transition_table[('q21','s')]= 'q22'
  transition_table[('q22','i')]= 'q23'
  transition_table[('q23','d')]= 'q24'
  transition_table[('q24','a')]= 'q25'
  transition_table[('q25','#')]= 'ACCEPT'
  transition_table[('q25',' ')]= 'q27'


  # string "tahuluk"
  transition_table[("q0","t")] = "q4"
  transition_table[('q4','a')]= 'q5'
  transition_table[('q5','h')]= 'q6'
  transition_table[('q6','u')]= 'q7'
  transition_table[('q7','l')]= 'q8'
  transition_table[('q8','u')]= 'q9'
  transition_table[('q9','k')]= 'q10'
  transition_table[('q10','#')]= 'ACCEPT'
  transition_table[('q10',' ')]= 'q27'

  # string "hami"
  transition_table[("q0","h")] = "q11"
  transition_table[('q11','a')]= 'q12'
  transition_table[('q12','m')]= 'q13'
  transition_table[('q13','i')]= 'q14'
  transition_table[('q14','#')]= 'ACCEPT'
  transition_table[('q14',' ')]= 'q27'

  # string "huting"
  transition_table[("q0","h")] = "q11"
  transition_table[('q11','u')]= 'q15'
  transition_table[('q15','t')]= 'q16'
  transition_table[('q16','i')]= 'q17'
  transition_table[('q17','n')]= 'q18'
  transition_table[('q18','g')]= 'q19'
  transition_table[('q19','#')]= 'ACCEPT'
  transition_table[('q19',' ')]= 'q27'


  # string "Hoda"
  transition_table[("q0","h")] = "q11"
  transition_table[('q11','o')]= 'q23'
  transition_table[('q23','d')]= 'q24'
  transition_table[('q24','a')]= 'q25'
  transition_table[('q25','#')]= 'ACCEPT'
  transition_table[('q25',' ')]= 'q27'

  # string "Lomo"
  transition_table[("q0", "l")] = "a1"
  transition_table[('a1','o')]= 'a2'
  transition_table[('a2','m')]= 'a3'
  transition_table[('a3','o')]= 'a4'
  transition_table[('a4','#')]= 'ACCEPT'
  transition_table[('a4',' ')]= 'q27'



  # string "Manuhor"
  transition_table[("q0", "m")] = "a5"
  transition_table[('a5','a')]= 'a6'
  transition_table[('a6','n')]= 'a7'
  transition_table[('a7','u')]= 'a8'
  transition_table[('a8','h')]='a9'
  transition_table[('a9','o')]= 'a10'
  transition_table[("a10", "r")] = "a11"
  transition_table[('a11','#')]='ACCEPT'
  transition_table[('a11',' ')]= 'q27'




  # string "Mida"
  transition_table[("q0","m")] = "a5"
  transition_table[("a5", "i")] = "a12"
  transition_table[('a12','d')]= 'a13'
  transition_table[('a13','a')]= 'a14'
  transition_table[('a14','#')]= 'ACCEPT'
  transition_table[('a14',' ')]= 'q27'


  # lexical Analysis
  idx_char = 0
  state = "q0"
  current_token = ""
  while state != "ACCEPT":
      current_char = input_string[idx_char]
      current_token += current_char
      print(state, current_char)
      state = transition_table[(state, current_char)]
      if state == "q27":
          print("current token: {} is valid".format(current_token))
          current_token = ""
      if state == "ERROR":
          print("error")
          break
      idx_char += 1

  # Conclusion
  if state == "ACCEPT":
      parser(kataInput)


# Main Program
print("Nama Anggota :")
print("Fendi Irfan Amorokhman (1301191447) \nChristina Natalia (1301180131) \nMoh Adi Ikfini M (13011944160)")
print("==================================")
print("Code based from Ade Romadhony, School of Computing - Telkom University")
print("==================================")

sentence = input("Masukkan kata yang ingin diperiksa: ")
lexicalAnalyzer(sentence)

import time
time.sleep(20)