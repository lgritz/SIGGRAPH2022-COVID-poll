#!/usr/bin/env python3

import csv
import numpy
import scipy.stats


answer_sets = {}

# Aliases for the question field names and answers. I didn't expect the google
# forms to make these fully verbose. But whatever, that's what computers are
# for.
Q_travel = 'How did you travel to Vancouver?'
A_air = 'By airplane'
A_land = 'By land (car, train, etc.)'
A_vancouver = 'I live in the Vancouver area'
A_none = 'I did not attend in person'
answer_sets[Q_travel] = [A_air, A_land, A_vancouver, A_none]

Q_mask = 'While indoors at conference venues (sessions, hallways, exhibition, etc.)'
A_rarely = 'I rarely or never wore a mask indoors'
A_sometimes = "I sometimes wore a mask indoors (e.g., depending on crowds, venue, mood, others)"
A_usually = 'I usually or always wore a mask indoors'
# A_none is also valid here
answer_sets[Q_mask] = [A_rarely, A_sometimes, A_usually, A_none]

Q_n_outdoor = 'Number of large or crowded social gatherings OUTDOORS'
Q_n_indoor_masked = 'Number of large or crowded social gatherings INDOORS, mostly MASKED'
Q_n_indoor_unmasked = 'Number of large or crowded social gatherings INDOORS, mostly UNMASKED'
# Each of the above can have the answer '0', '1', '2', '3+'
answer_sets[Q_n_outdoor] = ['0', '1', '2', '3+']
answer_sets[Q_n_indoor_masked] = ['0', '1', '2', '3+']
answer_sets[Q_n_indoor_unmasked] = ['0', '1', '2', '3+']

Q_covid = 'My COVID status'
A_nosym_notest = 'I had no symptoms and did not test'
A_nosym_negative = 'I had no symptoms and tested negative after SIGGRAPH'
A_covid = 'I got COVID -- tested positive between Aug 7 - Aug 19'
A_sick = 'I had COVID-like symptoms, but tested negative or did not test'
answer_sets[Q_covid] = [A_covid, A_sick, A_nosym_notest, A_nosym_negative]

Q_spread = 'Spread vectors (check all that apply)\n\nLet\'s consider "close contact" to mean: within 6 feet for 15 minutes or more'
# This one is a comma-separated list, and more than one of the following can
# be present::
A_contact = "I'm sure I was in close contact at SIGGRAPH/DigiPro with someone who tested positive"
A_nocontact = 'I am not aware of any specific person I was close to who tested positive'
A_household = 'Others in my household tested positive or got sick after I returned from SIGGRAPH'
A_workplace = 'Others in my workplace -- who did not themselves go to SIGGRAPH -- tested positive or got sick right after SIGGRAPH'
# reformulate into new questions:
Q_contact = A_contact
Q_household = A_household
Q_workplace = A_workplace


# List of responses, each entry is a dictionary for one row of the csv. The
# main list is for people who attended in person, a separate one for the
# control group of remote attendees (or those who did not attend).
responses = []
responses_remote = []


def read_responses():
    global responses
    global responses_remote
    print("Reading responses...")
    csvreader = csv.DictReader(open('responses.csv', 'rt'))
    total = 0
    for row in csvreader:
        # Do some cleanup on the ambiguous spread field
        spread = row[Q_spread].split(", ")
        row[Q_contact] = 'yes' if A_contact in spread else 'no'
        row[Q_household] = 'yes' if A_household in spread else 'no'
        row[Q_workplace] = 'yes' if A_workplace in spread else 'no'
        # Separate attendees from non-attendees
        if row[Q_travel] == A_none or row[Q_mask] == A_none:
            responses_remote.append(row)
        else:
            responses.append(row)
        # print (row)
        total += 1
    print('\nRead {} rows, {} attendees and {} non-attendees\n'.format(
        total, len(responses), len(responses_remote)))


def count(responses, field, values, cond=None, condset=None) -> (int, int):
    """" From the given set of responses, count the number of times the named
    field had a value in the set `value`. If `cond` is not None, then restrict
    the count only to responses where the value of field `cond` was in the set
    `condset`. Return a tuple where the first element is the count of matches,
    and the second is the total number of rows that qualified (were in the
    responses and, if applicable, satisfied the `cond` test).
    """
    qualified = 0
    total = 0
    for row in responses:
        if cond is None or row[cond] in condset:
            qualified += 1
            if row[field] in values:
                total += 1
    return (total, qualified)


def breakdown(label: str, responses, field, cond=None, condset=None,
              answers=None):
    """
    From the given set of responses, tally all the answers for the given
    `field`, and print the totals. If `cond` is not None, then restrict the
    tally only to responses where the value of field `cond` was in the set
    `condset`. If `answers` is not None, then only tally those answers that
    take on one of the values in the list `answers`.
    """
    totalnum = 0  # Number of responses in this set
    totals = {}  # Totals for each possible answer of field for this set
    for row in responses:
        A = row[field]  # Answer for field's row of this response
        # If a constraining condition was given, skip this response if
        # it doesn't meet the condition.
        if cond is None or row[cond] in condset:
            if A in totals:
                totals[A] += 1
            else:
                totals[A] = 1
            totalnum += 1
    print("\n{}:  (total {})\n".format(label, totalnum))
    # print(totals)
    for i in (answer_sets[field] if answers is None else answers):
        if i in totals:
            print('    {:4}  ({:4.1f}%) : {}'.format(
                totals[i], totals[i] * 100.0 / totalnum, i))


def filter(responses, field, values):
    """
    Return the subset of `responses` where the given `field` has a value in
    the set `values`.
    """
    return [row for row in responses if row[field] in values]


def significance(set1, set2, field, values1, values2, cond=None, condset=None) -> float:
    """"
    Considering cases where respondents in set1 had `field` in the set
    `values1`, compared to cases where respondents in set2 had `field` in the
    set `values2`, (and in both cases, if `cond` is not none, restrict to
    responses where field `cond` is in the set `condset`), find the
    statistical significance (p-value) of their being different.
    """
    attendees = count(set1, field, values1, cond, condset)
    control = count(set2, field, values2, cond, condset)
    table = [ [attendees[0], control[0] ],
              [attendees[1] - attendees[0], control[1] - control[0]] ]
    # print(table)
    return scipy.stats.barnard_exact(table).pvalue
    # return scipy.stats.fisher_exact(table)



def main():
    read_responses()

    print("COVID status of attendees vs non-attendees (control group)")
    print("----------------------------------------------------------")
    breakdown("Non-attendees", responses_remote, field=Q_covid)
    breakdown("Attendees", responses, field=Q_covid)
    print("\nTest positivity for attendees vs non-attendees: p = {:.4f}".format(
        significance(responses, responses_remote, Q_covid, [A_covid], [A_covid])))
    print("Test positivity or having symptoms for attendees vs non-attendees: p = {:.4f}".format(
        significance(responses, responses_remote, Q_covid, [A_covid, A_sick], [A_covid, A_sick])))
    print("")

    # breakdown("Travel of positive attendees", responses, field=Q_travel,
    #           cond=Q_covid, condset=[A_covid])
    print("Did means of travel make a difference in COVID status of attendees?")
    print("-------------------------------------------------------------------")
    breakdown("Travel of positive attendees",
              filter(responses, Q_covid, [A_covid]),
              field=Q_travel)
    # print("checking total pos attendees by air = ",
    #       count(responses, cond=Q_covid, condset=[A_covid], field=Q_travel, values=[A_air]))
    breakdown("Travel of presumed negative attendees", responses, field=Q_travel,
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])

    breakdown("Air travelers", responses, Q_covid, cond=Q_travel, condset=[A_air])
    breakdown("Ground travelers", responses, Q_covid, cond=Q_travel, condset=[A_land])
    breakdown("Vancouver residents", responses, Q_covid, cond=Q_travel, condset=[A_vancouver])
    print("\nTest positivity for air travelers vs residents: p = {:.4f}".format(
        significance(filter(responses, Q_travel, [A_air]),
                     filter(responses, Q_travel, [A_vancouver]),
                     Q_covid, [A_covid, A_sick], [A_covid, A_sick])))
    print("\n")


    print("Masking habits of attendees in conference venues")
    print("------------------------------------------------")
    breakdown("Mask habits of positive attendees", responses, field=Q_mask,
              cond=Q_covid, condset=[A_covid])
    breakdown("Mask habits of presumed negative attendees", responses, field=Q_mask,
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])
    breakdown("Rarely/never mask", responses, Q_covid, cond=Q_mask, condset=[A_rarely])
    breakdown("Sometimes mask", responses, Q_covid, cond=Q_mask, condset=[A_sometimes])
    breakdown("Usually/always mask", responses, Q_covid, cond=Q_mask, condset=[A_usually])

    breakdown("COVID positivity of attendees who always/usually masked in conference venues",
              responses, field=Q_covid,
              cond=Q_mask, condset=[A_usually])
    breakdown("COVID positivity of attendees who sometimes masked in conference venues",
              responses, field=Q_covid,
              cond=Q_mask, condset=[A_sometimes])
    breakdown("COVID positivity of attendees who never/rarely masked in conference venues",
              responses, field=Q_covid,
              cond=Q_mask, condset=[A_rarely])

    print("\nTest positivity + symptoms for usually/always-maskers vs rarely/never-maskers: p = {:.4f}".format(
        significance(filter(responses, Q_mask, [A_usually]),
                     filter(responses, Q_mask, [A_rarely]),
                     Q_covid, [A_covid, A_sick], [A_covid, A_sick])))
    print("\n")


    print("Attendee participation in crowded social events:")
    print("------------------------------------------------")
    breakdown("Outdoor gatherings of positive attendees", responses, field=Q_n_outdoor,
              cond=Q_covid, condset=[A_covid])
    breakdown("Outdoor gatherings of presumed negative attendees", responses, field=Q_n_outdoor,
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])
    breakdown("Masked indoor gatherings of positive attendees", responses, field=Q_n_indoor_masked,
              cond=Q_covid, condset=[A_covid])
    breakdown("Masked indoor gatherings of presumed negative attendees", responses, field=Q_n_indoor_masked,
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])
    breakdown("Unmasked indoor gatherings of positive attendees", responses, field=Q_n_indoor_unmasked,
              cond=Q_covid, condset=[A_covid])
    breakdown("Unmasked indoor gatherings of presumed negative attendees", responses, field=Q_n_indoor_unmasked,
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])

    breakdown("COVID positivity of attendees who never went to crowded indoor gatherings unmasked",
              responses, field=Q_covid,
              cond=Q_n_indoor_unmasked, condset=['0'])
    breakdown("COVID positivity of attendees who went to 3 or more crowded indoor gatherings unmasked",
              responses, field=Q_covid,
              cond=Q_n_indoor_unmasked, condset=['3+'])

    print("\nTest positivity or symptoms for 0 indoor unmasked events vs 3+: p = {:.4f}".format(
        significance(filter(responses, Q_n_indoor_unmasked, ['0']),
                     filter(responses, Q_n_indoor_unmasked, ['3+']),
                     Q_covid, [A_covid, A_sick], [A_covid, A_sick])))
    print("\nTest positivity or symptoms for 0 indoor masked events vs 3+: p = {:.4f}".format(
        significance(filter(responses, Q_n_indoor_masked, ['0']),
                     filter(responses, Q_n_indoor_masked, ['3+']),
                     Q_covid, [A_covid, A_sick], [A_covid, A_sick])))
    print("\nTest positivity or symptoms for 0 outdoor events vs 3+: p = {:.4f}".format(
        significance(filter(responses, Q_n_outdoor, ['0']),
                     filter(responses, Q_n_outdoor, ['3+']),
                     Q_covid, [A_covid, A_sick], [A_covid, A_sick])))
    print("\n")


    print("Questions about spread")
    print("----------------------")
    breakdown("Are positive attendees aware of close contact with other positive attendees",
              responses, field=Q_contact, answers=['yes', 'no'],
              cond=Q_covid, condset=[A_covid])
    breakdown("Are presumed negative attendees aware of close contact with other positive attendees",
              responses, field=Q_contact, answers=['yes', 'no'],
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])

    breakdown("Are positive attendees aware of spread to household members",
              responses, field=Q_household, answers=['yes', 'no'],
              cond=Q_covid, condset=[A_covid])
    breakdown("Are presumed negative attendees aware of spread to household members",
              responses, field=Q_household, answers=['yes', 'no'],
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])

    breakdown("Are positive attendees aware of spread to workplace members who did not attend",
              responses, field=Q_workplace, answers=['yes', 'no'],
              cond=Q_covid, condset=[A_covid])
    breakdown("Are presumed negative attendees aware of spread to workplace members who did not attend",
              responses, field=Q_workplace, answers=['yes', 'no'],
              cond=Q_covid, condset=[A_nosym_negative, A_nosym_notest])


if __name__ == "__main__":
    main()
    # print (responses)
