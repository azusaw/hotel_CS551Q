Feature: checking disasters

    Scenario: add a disaster
        Given we want to add a disaster
        When we fill in the form
        Then it succeeds

    Scenario: adding disaster
        Given we have specific disasters to add
        | disasterNo   | year | seq | group  | subgroup | type  | subtype | eventName | country    | iso | region       | continent | location   | startYear | startMonth | startDay | endYear | endMonth |  endDay | totalDeaths | injured | affected | totalAffected | homeless | damageCost |
        | 2020-0055-WEF| 2020 |  15 | Natural|    A     | Flood | subtype | Ada       | Bangladesh | WEF | SouthernAsia | Asia      | Bangladesh | 2020      | 2          | 5        | 2020    | 3        |  1      | 500         | 200     | 90000    | 23456         | 666      | 7876       |
        When we visit the all page
        Then we will find '2020-0055-WEF'

