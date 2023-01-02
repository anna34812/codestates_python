import team_information as team_information

def generate_introduce(member):
    if member['소속'] == '나무팀':
        if member['국적'] == '대한민국':
            return('안녕하세요, 저는 파릇파릇한 나무팀의 ' + member['성'] + member['이름'] + '입니다.')
        else: 
            return('안녕하세요, 저는 파릇파릇한 나무팀의 ' + member['이름'] + ' ' + member['성'] + '입니다.')
    elif member['소속'] == '꽃팀':
        if member['국적'] == '대한민국':
            return('안녕하세요, 저는 파릇파릇한 꽃팀의 ' + member['성'] + member['이름'] + '입니다.')
        else: 
            return('안녕하세요, 저는 파릇파릇한 꽃팀의 ' + member['이름'] + ' ' + member['성'] + '입니다.')