# key란 본인 commit message의 식별자, 미리 지정
def getKey():
    users_key = {'keunhak':'lkh', 'keunhyeok':'me', 'ksbyun':'bks'}
    return users_key

# commit 메시지 파싱, key란 본인 이름의 축약어
def messageParsing(message, key):
    res = []
    temp = message
    while True:
        text = ''
        # key가 없다면 종료
        if temp.find(key) == -1:
            return res
        else:
            text += key
            firstIndex = temp.find('-')
            secondIndex = temp[firstIndex + 1:].find('-') + firstIndex + 1
            text += temp[firstIndex : secondIndex + 2]
            res.append(text)
            temp = temp[secondIndex + 2:]
            continue
    return res

# commit이 중복되는지 체크
def checkCommit(user, commit):
    temp = list(user.keys())
    # key 리스트에 있다면 True, 없으면 False
    if commit in temp:
        return True
    else:
        return False