def displayFibrosequence(seq):
    start = 0
    start_1 = 1
    default_add = start+start_1
    
    result = [0,1]
    if int(seq):
        for i in range((int(seq) - 2)):
            next_total = result[-1] + result[-2]
            result.append(next_total)
        return result
            
    else:
        return 'cannot solve for characters'
  

def DisplaySequence_is_in(result, request):
    if int(request) in result:
        return True
    else:
        return False

def result_print(arr):
    print(" ".join(map(str, arr)))

def print_is_in(bol,request):
    if bol:
        print(f"{request} is a fibbronicca number")
    else:
        print(f"{request} is NOT a fibbronica number")

print('operations.....................')
print('Asking users number..............')
request = input('Input your fibbronicca number..... ')
result_print(displayFibrosequence(request))
print_is_in(DisplaySequence_is_in(displayFibrosequence((request)),request),request)
