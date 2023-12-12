import string


def isUnique(s):
    char_list = {}
    for i in s:
        if i not in char_list:
            char_list[i] = 1
        else:
            return False
    return True

def main():
    word = "asdfghj kl!@#"
    print(isUnique(word))
    exit(0)


if __name__ == "__main__":
    main()