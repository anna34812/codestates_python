def compare_age(standard_member, member_to_compare):
    if standard_member['나이'] > member_to_compare['나이']:
        return(standard_member['이름']+'사원은 '+member_to_compare['이름']+'보다 나이가 많습니다.')
    elif standard_member['나이'] < member_to_compare['나이']:
        return(standard_member['이름']+'사원은 '+member_to_compare['이름']+'보다 나이가 적습니다.')
    else:
        return(standard_member['이름']+'사원은 '+member_to_compare['이름']+'과 나이가 같습니다.')