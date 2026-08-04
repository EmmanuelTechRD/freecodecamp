# freeCodeCamp challenge: Food Chain
# Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.
# The apex predator is the animal that is never prey to another animal.
# Return the chain as an array of strings.
def get_food_chain(pairs):
    if not pairs:
        return []

    predators = set()
    preys = set()
    predator_map = {}

    for predator, prey in pairs:
        predators.add(predator)
        preys.add(prey)
        predator_map[predator] = prey

    # apex predators cannot be preys
    apex_candidates = predators - preys
    if not apex_candidates:
        return []

    current = apex_candidates.pop()
    chain = [current]

    # finding predators
    while current in predator_map:
        current = predator_map[current]
        chain.append(current)

    return chain