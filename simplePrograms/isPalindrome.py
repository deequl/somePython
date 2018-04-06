#Long solution
def is_palindrome_old(word):
    word = list(word)
    while word:
        if word.pop(-1)==word.pop(0):
            if len(word)==1:
                return True
            elif len(word)==2:
                return word.pop(-1)==word.pop(0)
        else :
            return False

#Short solution
def is_palindrome(word):
    return word == word[::-1]

#improved version (replace() spaces(" "))
def is_palindrome_noSpaces(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]