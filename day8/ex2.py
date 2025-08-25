check_1 = ['t', 'r', 'u', 'e']
check_2 = ['l', 'o', 'v', 'e']


def calculate_love_score(name_people_1, name_people_2):
    names = (name_people_1 + name_people_2).lower()
    count_check_1 = sum(ch in check_1 for ch in names)
    count_check_2 = sum(ch in check_2 for ch in names)

    print(f'{count_check_1}{count_check_2}')


calculate_love_score("Kanye West", "Kim Kardashian")