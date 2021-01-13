char_input = input('Enter cells: ')

# table

first_and_last = '---------'
line = char_input[0] + ' ' + char_input[1] + ' ' + char_input[2]
line1 = char_input[3] + ' ' + char_input[4] + ' ' + char_input[5]
line2 = char_input[6] + ' ' + char_input[7] + ' ' + char_input[8]
frame = '|'

win = ((char_input[0] and char_input[1] and char_input[2]) or
       (char_input[3] and char_input[4] and char_input[5]) or
       (char_input[6] and char_input[7] and char_input[8]) or
       (char_input[0] and char_input[3] and char_input[6]) or
       (char_input[1] and char_input[4] and char_input[7]) or
       (char_input[2] and char_input[5] and char_input[8]) or
       (char_input[0] and char_input[4] and char_input[8]) or
       (char_input[2] and char_input[4] and char_input[6]))

print(first_and_last)
print(frame + ' ' + line + ' ' + frame)
print(frame + ' ' + line1 + ' ' + frame)
print(frame + ' ' + line2 + ' ' + frame)
print(first_and_last)


if (('X' == char_input[0] and 'X' == char_input[3] and 'X' == char_input[6]) and
      'O' == char_input[1] and 'O' == char_input[4] and 'O' == char_input[7] or
      ((char_input.count('X') - char_input.count('O')) > 1) or
        (char_input.count('O') - char_input.count('X')) > 1):
    print('Impossible')
elif (('X' == char_input[0] and 'X' == char_input[1] and 'X' == char_input[2]) or
      'X' == char_input[2] and 'X' == char_input[4] and 'X' == char_input[6]):
    print('X wins')
elif ('O' == char_input[2] and 'O' == char_input[5] and 'O' == char_input[8]):
    print('O wins')
elif char_input.count('_') == 0 and win == 'X':
    print('Draw')
else:
    print('Game not finished')
