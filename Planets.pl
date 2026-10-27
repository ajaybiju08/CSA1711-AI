% FACTS: planet(Name, Type, Moons, OrderFromSun)
planet(mercury, terrestrial, 0, 1).
planet(venus,   terrestrial, 0, 2).
planet(earth,   terrestrial, 1, 3).
planet(mars,    terrestrial, 2, 4).
planet(jupiter, gas_giant,   95, 5).
planet(saturn,  gas_giant,  146, 6).
planet(uranus,  ice_giant,   28, 7).
planet(neptune, ice_giant,   16, 8).

% RULE: Find planets that have moons
has_moons(Planet) :-
    planet(Planet, _, MoonCount, _),
    MoonCount > 0.

% RULE: Find out if Planet1 is closer to the Sun than Planet2
closer_to_sun(Planet1, Planet2) :-
    planet(Planet1, _, _, Order1),
    planet(Planet2, _, _, Order2),
    Order1 < Order2.
