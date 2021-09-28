vowel_list = ['a', 'e', 'o', 'u', 'i']


def vowel_change(txt, vow):
    new_txt = ''
    if check_type(txt):
        if check_vowel_lenght(vow):
            if check_vowel_list(vow):
                for char in txt:
                    if not check_vowel_list(char):
                        new_txt = new_txt + char
                    else:
                        new_txt = new_txt + vow
    return new_txt


def check_type(txt):
    if isinstance(txt, str):
        return True
    return False


def check_vowel_lenght(vow):
    if len(vow) == 1:
        return True
    return False


def check_vowel_list(vow):
    if vow in vowel_list:
        return True
    return False
