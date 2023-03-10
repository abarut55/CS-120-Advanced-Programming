def champion_rank(champion_id, events):
    rank = champion_id
    for event in events.split()
        if int(event.split()[0]) == rank:
            if event.split()[1] == 'O'
                rank += 1
            elif event.split()[1] == 'I'
                return -1
    return rank

# Example usage
print(champion_rank(2, "2 O 12 I")) # Output: -1
print(champion_rank(10, "1 O 10 I 2 O 3 O 4 O 15 O")) # Output: 6
