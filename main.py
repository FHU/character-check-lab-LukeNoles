def check_character(word, index):
   char =  word[index]
   if char.isalpha():
       return "letter"
   if char.isdigit():
       return "digit"
   if char.isspace():
       return "white space"
   else:
       return "unknown"
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
