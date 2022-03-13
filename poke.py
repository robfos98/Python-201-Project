import requests
def display(mon):
    print('\n' + mon['species']['name'].title())
    print(mon['id'])
    for type in mon['types']:
        print(type['type']['name'].title())
    print('')
    for stat in mon['stats']:
        print(stat['stat']['name'].title() + ': ' + str(stat['base_stat']))
    print('')
    abilities = [ability['ability']['name'] for ability in mon['abilities'] if not ability['is_hidden']]
    if len(abilities) == 2: print('Abilities:')
    else: print('Ability:')
    for ability in abilities: print(ability.title())
    for ability in mon['abilities']:
        if ability['is_hidden']:
            print('Hidden Ability:')
            print(ability['ability']['name'].title())
    print('')

print('\nHello!')
print('This program can tell you about a Pokemon.')
print('Name a Pokemon, or pick a number up to 898; or type quit to leave.')
while True:
    mon = input('Search: ').lower()
    if mon in ['exit', 'leave', 'quit', 'end', 'out', 'over', 'q', 'x']: break
    try: mon = requests.get('https://pokeapi.co/api/v2/pokemon/' + mon).json()
    except:
        print('\nIt doesn\'t look like I can get that for you. Check if you made a typo.')
        continue
    display(mon)
    print('Name another Pokemon, or pick a number up to 898; or type quit to leave.')