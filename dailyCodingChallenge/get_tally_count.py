# freeCodeCamp challenge: Given a string of tally marks, return the total count represented.
# Each pipe "|" represents one count.
# Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
# Groups are separated by a space.
def get_tally_count(s):

    return s.count('|') + s.count('/')