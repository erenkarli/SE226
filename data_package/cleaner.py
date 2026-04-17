def remove_duplicates(data_list):
    result = []
    for x in data_list:
        if x not in result:
            result.append(x)
    return result

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]