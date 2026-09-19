def valid_palindrome(s):
    # Assume the default possibility is true
    status = True

    # Amount of letters needed to be removed (can only be 1)
    remove = 0

    # Adjustment to account for "removing" one letter
    f_adjust = 0
    b_adjust = 0

    # Length of s:
    length = len(s)
    for i_char in range((length+1)//2):
        # If not immediately palindrome, try removing either letter
        if s[i_char + f_adjust] != s[length - i_char - 1 - b_adjust]:
            # Check if removing one letter from the front part helps
            if s[i_char + f_adjust + 1] == s[length - i_char - 1 - b_adjust]:
                f_adjust += 1
                remove += 1
            # Check if removing one letter from the back part helps
            elif s[i_char + f_adjust] == s[length - i_char - 2 - b_adjust]:
                b_adjust += 1
                remove += 1
            # If neither helps, than we need to remove at least two letter or it is invalid, but neither aren't allowed to happen
            else:
                status = False  # If my brain hadn't blanked and typed "True" here this code would've been a one-shot :_)
        
    # If it ends up needing more than 1 letter removed (remove>1)
    if remove > 1:
        status = False

    return status
