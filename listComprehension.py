sq = []
for i in range(1, 101):
    sq.append(i**2)
print(sq)


sq2 = [i**2 for i in range(1, 101)]
print(sq2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)


remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

movies = ['Star War', 'Gandhi', 'Casablanca', 'Shawshank Redemption', 'Toy Story', 'Gone With The Wind', 'Citizen Kane', 'It\'s A Wonderful Life', 'The Wizard of Oz', 'Gattaca',
          'Rear Window', 'Ghostbusters', 'To Kill A Mockingbird', 'Good Will Hunting', '2001: A Space Odyssey', 'Raiders of the Lost Ark', 'Groundhog Day', 'Close Encounters of the Third Kind']

gmovies = []
for title in movies:
    if title.startswith('G'):
        gmovies.append(title)
print(gmovies)

gmovies = [title for title in movies if title.startswith('G')]
print(gmovies)

movies = [('Citizen Kane', 1941), ('Spirited Away', 2001), ('It\'s A Wonderful Life', 1946), ('Gattaca', 1997), ('No Country For Old Men', 2007), ('Rear Window',
                                                                                                                                                   1954), ('The Lord of The Rings: The Fellowship of the Ring', 1977), ('The Royal Tenenbaums', 2001), ('The Aviator', 2004), ('Raider of the Lost Ark', 1981)]

pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)

v = [2, -3, 1]
#w = 4*v

w = [4 * x for x in v]
print(w)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_prod = [(a, b) for a in A for b in B]
print(cartesian_prod)
