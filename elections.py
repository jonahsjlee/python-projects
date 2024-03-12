'''
Name: Jonah Lee
Computing ID: wkx9ff

dict is country:winner
population is country: population votes
'''

dict = {}

def add_country_winner(name, votes):
    global dict
    most_votes = 0
    for candidate in votes:
        if votes[candidate] > most_votes:
            most_votes = votes[candidate]
            winner = candidate
    #for candidate_name, vote_count in votes.items():
        #if vote_count == most_votes:
            #winner = candidate_name
    dict[name] = winner

def winner(population):
    global dict
    if population == {} or dict == {}:
        return "No Winner"
    scores = {}
    for country in population:
        for country2 in dict:
            if country == country2:
                if scores.get(dict[country]) != None:
                    scores[dict[country]] += population[country]
                else:
                    scores[dict[country]] = population[country]
    #for country, winner in dict.items():
        #if country in population:
            #for country2, pop_votes in population.items():
                #scores[winner] += pop_votes
    highest_score = 0
    for winner, score in scores.items():
        if score > highest_score:
            highest_score = score
    for winner, score in scores.items():
        if highest_score == score:
            return winner

def clear():
    global dict
    dict.clear()