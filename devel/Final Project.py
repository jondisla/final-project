##PRESS F5 TO RUN THE PROGRAM IN THE PYTHON SHELL##

print("Hello! Welcome to the personality test!")
print("")
print('============')
print('INSTRUCTIONS')
print('============')
print('')
print('Answer these questions about yourself and then compare with friends')
print('You will learn more about yourself and your friends!')
print('')

while True:
    print("Are you ready to begin? Enter Y or N")
    startGame = input()
    if startGame.upper() != 'Y':
        continue
    else:
        print("Let's begin!")
        break

while True:
    print('''What's your name? ''')
    name = input()
    if name == (''):
        continue
    else:
        print ("Okay " + name + " here we go!")
        print('Multiple choice, type A or B then press ENTER')
        print('')
        break

def questions():
    answers = []

    while True:

        print('a. Interact with many, including strangers \nb. Interact with a few, known to you')
        q1 = input('1.    At a party do you: \n')


        if q1.upper() == 'A' or q1.upper() == 'B':
            break
                
        else:
            print('***TRY AGAIN***')

    answers = answers + [q1]
    print('')
    print('Answers so far : ')
    for q1 in answers:
        print('' + q1)
        
    while True:
    
        print("")
        print('a. Realistic than speculative \nb. Speculative than realistic\n')
        q2 = input('2.    Are    you    more: \n')

        if q2.upper() == 'A' or q2.upper() == 'B':
            break
                    
        else:
            print('***TRY AGAIN***')

    answers = answers + [q2]
    print('Answers so far : ')
    for q2 in answers:
            print('' + q2)

    while True:
    
            print("")
            print('a. Have your “head in the clouds"\nb. Be “in a rut” \n')
            q3 = input('3.  Is it worse to: ')

            if q3.upper() == 'A' or q3.upper() == 'B':
                break
                    
            else:
                print('***TRY AGAIN***')

    answers = answers + [q3]
    print('Answers so far : ')
    for q3 in answers:
                print('' + q3)

    while True:
           
                print("")
                print('a. Principles\nb. Emotions\n ')
                q4 = input('4.  Are you more impressed by: ')

                if q4.upper() == 'A' or q4.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q4]
    print('Answers so far : ')
    for q4 in answers:
                print('' + q4)

    while True:
            
                print("")
                print('a. Convincing \nb. Touching \n')
                q5 = input('5.  Are more drawn toward the: ')

                if q5.upper() == 'A' or q5.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q5]
    print('Answers so far : ')
    for q5 in answers:
                print('' + q5)
                
    while True:
            
                print("")
                print('a. To deadlines \nb. Just “whenever”  \n')
                q6 = input('6. Do you prefer to work: ')

                if q6.upper() == 'A' or q6.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q6]
    print('Answers so far : ')
    for q6 in answers:
                print('' + q6)

    while True:            
            
                print("")
                print('a. Rather carefully \nb. Somewhat impulsively  \n')
                q7 = input('7. Do you tend to choose: ')

                if q7.upper() == 'A' or q7.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    

    answers = answers + [q7]
    print('Answers so far : ')
    for q7 in answers:
                print('' + q7)

    while True:
            
                print("")
                print('a. re-negotiable\nb. random and circumstantial  \n')
                q8 = input('8.  In relationships should most things be: ')

                if q8.upper() == 'A' or q8.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q8]
    print('Answers so far : ')
    for q8 in answers:
                print('' + q8)

    while True:
            
                print("")
                print('a. hard-headed\nb. soft-hearted  \n')
                q9 = input('9.  Do you see yourself as basically: ')

                if q9.upper() == 'A' or q9.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q9]
    print('Answers so far : ')
    for q9 in answers:
                print('' + q9)
                
    while True:
            
                print("")
                print('a. easy to approach\nb. somewhat reserved  \n')
                q10 = input('10.  Are you more inclined to be: ')

                if q10.upper() == 'A' or q10.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q10]
    print('Answers so far : ')
    for q10 in answers:
                print('' + q10)
                
    while True:
                print("")
                print('a. make sure things are arranged\nb. just let things happen  \n')
                q11 = input('11.  Is it preferable mostly to: ')

                if q11.upper() == 'A' or q11.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q11]
    print('Answers so far : ')
    for q11 in answers:
                print('' + q11)

    while True:
            
                print("")
                print('a. your head\nb. your heart  \n')
                q12 = input('12.  Which rules you more: ')

                if q12.upper() == 'A' or q12.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q12]
    print('Answers so far : ')
    for q12 in answers:
                print('' + q12)
                
    while True:
            
                print("")
                print('a. initiate conversation\nb. wait to be approached  \n')
                q13 = input('13. In company do you: ')

                if q13.upper() == 'A' or q13.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q13]
    print('Answers so far : ')
    for q13 in answers:
                print('' + q13)
                    
    while True:
            
                print("")
                print('a. planned event\nb. unplanned event  \n')
                q14 = input('14.  Do you prefer the: ')

                if q14.upper() == 'A' or q14.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q14]
    print('Answers so far : ')
    for q14 in answers:
                print('' + q14)

    while True:
            
                print("")
                print('a. Stay late, with increasing energy\nb. Leave early with\bdecreased energy  \n')
                q15 = input('15. At parties do you: ')

                if q15.upper() == 'A' or q15.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q15]
    print('Answers so far : ')
    for q15 in answers:
                print('' + q15)

    while True:
               
                print("")
                print('a. speak easily and at length with strangers\nb. find little to say to strangers ')
                q16 = input('16.  Do you: ')

                if q16.upper() == 'A' or q16.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q16]
    print('Answers so far : ')
    for q16 in answers:
                print('' + q16)
                
    while True:
                print("")
                print('a. a practical sort of person\nb. a fanciful sort of person  \n')
                q17 = input('17.  Are you more frequently: ')

                if q17.upper() == 'A' or q17.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')
                    
    answers = answers + [q17]
    print('Answers so far : ')
    for q17 in answers:
                print('' + q17)
                
    while True:
                
                print("")
                print('a. experience\nb. hunch  \n')
                q18 = input('18.  Are you more likely to trust your: ')

                if q18.upper() == 'A' or q18.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q18]
    print('Answers so far : ')
    for q18 in answers:
                print('' + q18)

    while True:
                print("")
                print('a. Punctual\nb. Leisurely  \n')
                q19 = input('19.  Are you more: ')

                if q19.upper() == 'A' or q19.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q19]
    print('Answers so far : ')
    for q19 in answers:
                print('' + q19)
                
    while True:
                print("")
                print('a. Serious and determined\nb. Easy-going  \n')
                q20 = input('20. Would you say you are more: ')

                if q20.upper() == 'A' or q20.upper() == 'B':
                    break
                        
                else:
                    print('***TRY AGAIN***')

    answers = answers + [q20]
    print('Answers so far: ')
    for q20 in answers:
                print('' + q20)

questions()

print("That's all the questions for now,  working on recording your answers soon!")
input('Thanks for taking the test! Press ENTER to exit')
