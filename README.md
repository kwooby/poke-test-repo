# poke-test-repo

Personal Mini Dex

.
06/25/2026

Major:
    -Added enter to search
    -Cleaned abilities code block to include multiple abilities if pokemon has them

Minor:
    -Fixed multiline in search

Need to Fix:
    Major:

    -Evolving through friendship currently only partially works, it returns (friendship #)
    but does not apply to several of the eevee line:
        -Leafeon/Glaceon: Evolve through friendhsip and specific items
        -Umbreon/Espeon: Evolve through friendship and time of day
        -Vaporeon/Flareon/Jolteon: Evolve through evolution stone items(does not show
        in mini dex as of today)
        -Sylveon: Evolves through friendship and move knowledge (this will be difficult
         to fit in the UI lmao)
    -pokesearch of any eeveelution (not eevee) should only result in eevee to one eevee-
    lution, currently returns every single eevee to eeveelution
    -When looking up Eevee in the pokesearch, the eeveelutions should fit rather than
    stack on top of the sprites

    **NIDORAN(MALE AND FEMALE) CANNOT BE SEARCHED IN THE POKESEARCH!!!
    -We will need to add specifications for both eevee and nidoran at the least

    Minor:

    -Method should find the stone or item needed to evolve with an item
    -Pokemon that evolve through trade do not have the items required if they are needed,
    while it's not entirely necessary, it would be nice to add that
    -Pokemon with gender specific evolutions should also be addressed
        -On a similar note, for pokemon that evolve gender-specifically, sprites must
        also show both genders of the pokemon given to the pokesearch

.
06/18/2026

Major:
    -Added levels/methods to evo line

Minor:
    -Bug fixes
    -Code and UI cleanup

Need to Fix:
    -First of all, who would've known that adding the evolution methods would cause so
    many issues holy shit lmao

    **EEVEE IS ROUGH
    -Evolving through friendship currently only partially works, it returns (friendship #)
    but does not apply to several of the eevee line:
        -Leafeon/Glaceon: Evolve through friendhsip and specific items
        -Umbreon/Espeon: Evolve through friendship and time of day
        -Vaporeon/Flareon/Jolteon: Evolve through evolution stone items(does not show
        in mini dex as of today)
        -Sylveon: Evolves through friendship and move knowledge (this will be difficult
         to fit in the UI lmao)
    -pokesearch of any eeveelution (not eevee) should only result in eevee to one eevee-
    lution, currently returns every single eevee to eeveelution
    -When looking up Eevee in the pokesearch, the eeveelutions should fit rather than
    stack on top of the sprites

    **NIDORAN(MALE AND FEMALE) CANNOT BE SEARCHED IN THE POKESEARCH!!!
    -We will need to add specifications for both eevee and nidoran at the least

    -Method should find the stone or item needed to evolve with an item
    -Pokemon that evolve through trade do not have the items required if they are needed,
    while it's not entirely necessary, it would be nice to add that
    -Pokemon with gender specific evolutions should also be addressed
        -On a similar note, for pokemon that evolve gender-specifically, sprites must
        also show both genders of the pokemon given to the pokesearch
    -Still need to add the enter to search on the search page

.
06/16/2026

Major:
    -Added shiny sprites to pokesearch!!!!!
    -Added Evo line text (add levels/evolution type)
    -Added abilities to pokesearch

Minor:
    -Minor cleanup
    -Small bug fixes
    -Moved bst text under rest of stats
    -Fixed sizing on pokename input box and moved button to fit accordingly

Need to Add:
    -Add level requirements/evolution requirements to evo line
    -Add level up algorithm to scale stats by an inputted level

.
06/12/2026:

Major:

    -Added bst(Base Stat Total) to pokesearch
    -Added type lookup

Minor:

    -Minor bugs and fixes
    -Code cleanup
    -Changed pokemon not found text

Need to Add:

    -Evolution Line and level to pokesearch
    -Ability lookup to pokesearch
    -Add level up algorithm to scale stats by an inputted level

.
06/07/2026:

Major:

    -Added Base Stats to sprite finder
    -Added error screen for input that does not exist in pb

Minor:

    -Fixed trim on ends of input to accept names w/ whitespace
    -Changed BoxLayout to FloatLayout, more dynamic
        -Fixed layout issues, pos_hint, and size_hint
    -Put in a try:except for input and sprites
    -Added more defining variables 

Need to Add:

    -Total Base Stat (tbs)
    -Search stats by pokemon AND level?
    -Nature lookup?
