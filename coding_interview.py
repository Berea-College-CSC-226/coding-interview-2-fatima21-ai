
def balanced_parentheses(text):


    text_len = len (text)%2
    if text_len == 0:
        return True
    else:
        text_len = 1
        return False



def main():
    text= input ("Enter text with parentheses:")
    result = balanced_parentheses (text)
    print (result)

if __name__ == "__main__":
    main()