import os
import csv
from collections import Counter

def PyPoll():
    file_read_path = os.path.join('Resources','election_data.csv')
    #Open the file as dict
    reader = csv.DictReader(open(file_read_path))
    #get the list of Candidate by key
    candidate_lst = [c['Candidate'] for c in reader]
    #COUNT votes for each candidate as dict
    candidate_dict = dict(Counter(candidate_lst))
    #count Total Votes
    total_voters = sum(candidate_dict.values())
    #Check for winner with max vote
    winner = max(candidate_dict, key=candidate_dict.get)

    '''Print result in following format
    Election Results
    -------------------------
    Total Votes: 3521001
    -------------------------
    Khan: 63.000% (2218231)
    Correy: 20.000% (704200)
    Li: 14.000% (492940)
    O'Tooley: 3.000% (105630)
    -------------------------
    Winner: Khan
    -------------------------'''
    #Format
    result_str = 'Election Results\n'
    result_str += '-'*30 + '\n'
    result_str +='Total Votes: {}\n'.format(total_voters)
    result_str += '-'*30 + '\n'
    #Print candidate and votes
    for candidate, votes in candidate_dict.items():
        percent_votes = (votes / total_voters) * 100.0
        result_str += "{}:  {:.3f}% ({})\n".format( candidate, percent_votes, votes)
        #print("{}: {0:.3f} ({})".format(candidate, percent_votes, votes))
    result_str += '-'*30 + '\n'
    result_str += "Winner: {}\n".format(winner)
    result_str += '-'*30 + '\n'

    #print the output
    print(result_str)

    #Print it to the file
    file_write_path = os.path.join('Resources','election_result.csv')
    with open(file_write_path, 'w') as f_write:
        print(result_str, file=f_write)

'''-----------------------------------------------------------------------'''
''' Function call '''
PyPoll()
'''-----------------------------------------------------------------------'''
