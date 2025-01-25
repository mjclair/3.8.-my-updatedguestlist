
guests = ['Socrates', 'Seneca', 'Epictetus']

guests.append('Steve Jobs')
guests.append('Nikola Tesla')
guests.append('Leonardo da Vinci')

print("Good news! I found a bigger dinner table, so now there’s more space for guests!")

guests.insert(0, 'Marcus Aurelius')

guests.insert(len(guests) // 2, 'Albert Einstein')

guests.append('Alan Turing')

guests.sort()

for guest in guests:
    print("Dear " + guest + ", Please join me for an unforgettable evening of food and drinks.")
