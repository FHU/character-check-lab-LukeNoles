def check_character(word, index):
   char =  word[index]
   if str(char).isalpha():
       return "letter"
   if str(char).isdigit():
       return "digit"
   if str(char).isspace():
       return "whitespace"
   else:
       return "unknown"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))