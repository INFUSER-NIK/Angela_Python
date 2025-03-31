def explore_galaxy(star_map):
    num_planets = len(star_map)
    num_stars = len(star_map[0]) if num_planets > 0 else 0
    for planet in range(num_planets):
        for star in range(num_stars):
            print(star_map[planet][star], end=" ")
        print()

num_planets = int(input("Enter number of planets: "))
num_stars = int(input("Enter number of stars in each planet's system: "))

universe = []
for planet in range(num_planets):
    star_row = list(map(int, input(f"Enter star brightness levels for planet {planet+1} separated by space: ").split()))
    universe.append(star_row)

explore_galaxy(universe)
