import random

  
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)
  

uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))  

lowercaseLetter1=chr(random.randint(65,90))
lowercaseLetter2=chr(random.randint(65,90))
random_digit = (random.randint(0,9))
rndom_digit = (random.randint(0,9))
punctuation = chr(random.randint(33,47))
punctuation2 = chr(random.randint(33,47)) 
password = str(uppercaseLetter1) + str(uppercaseLetter2) + str(lowercaseLetter1.lower()) + str(lowercaseLetter2.lower())+ str(random_digit) + str(rndom_digit) + str(punctuation) + str(punctuation2)
password = shuffle(password) 
    

def main():
  welcome = input('Would you like a random password? (yes or no)')
  if welcome == ('yes'):
    print (password)
  else:
    print ('Maybe some other time!')
  def second():
    repeat = input('Would you like the characters from the password to be shuffled? (yes or no)')
    if repeat == 'yes':
      print (shuffle(password))
      second()
    else:
      exit()
  second()

main()

