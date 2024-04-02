import string


letters_punctuation = list(string.ascii_letters) + list(string.punctuation) + list(string.digits)

flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"


#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


answer = []


for count in range(len(flag)):
    answer.append("a")
    answer.append("a")
    
    for first_char in letters_punctuation:
        answer[count * 2] = first_char

        for second_char in letters_punctuation:
            answer[count * 2 + 1] = second_char

            if (ord(answer[count * 2]) << 8) + ord(answer[count*2 + 1]) == ord(flag[count]):
                print(f'{answer[-2]}{answer[-1]}', end="")
                #print(f'{"".join(answer)}')
                break


        if (ord(answer[count * 2]) << 8) + ord(answer[count*2 + 1]) == ord(flag[count]):
            break
