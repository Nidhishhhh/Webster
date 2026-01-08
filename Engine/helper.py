import re


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'  #here play is a constant term, (.+?) is a dynamic term and on youtube is again a constant term.
    match = re.search(pattern, command, re.IGNORECASE) #here we have imported re(REGULAR EXPRESSION) module to pass the qury. re.IGNORECASE is used to ignore the capital and small letters.
    return match.group(1) if match else None #match.group is used to search the dynamic term in the query. If no match is found, it returns None.