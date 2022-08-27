# Results and analysis of post-SIGGRAPH COVID poll 2022

At SIGGRAPH/DigiPro 2022, I led a public service / science experiment /
performance art piece involving carrying a CO2 meter and live tweeting
room-by-room CO2 measurements. CO2 concentration goes up with increased
density of exhaling people and decreases with good air circulation/filtration,
and is therefore a proxy for risk of transmission of airborne respiratory
pathogens. I have an [Aranet4](https://aranet.com/products/aranet4/), which is
considered extremely reliable.

Outdoor unpolluted locales should read around 420 ppm of CO2 as I write this
in 2022 (though when I was born, it was around 320 ppm). Anything below 550 or
so is practically like being outdoors and in such an environment, I'm very
comfortable being unmasked for long periods if I'm not too close to strangers.
I believe that in the E.U., indoor air quality standards require 800 ppm or
less, or the venue is considered over-crowded or under-ventilated. Roughly
speaking, under 1000 ppm is probably a reasonably good indoor reading in which
I would be comfortable being in a restaurant unmasked. Much over that, though,
and I stay masked even for short periods. (There's no scientific reason for
those particular numbers, it's just my comfort level. Yours may be different.)

To briefly summarize the results, I found that the hallways at the Vancouver
Convention Centre were an excellent mid-500s or so ppm. The session rooms
ranged from 700 to 1200 most of the time, with some occasionally peaking as
high as 1600. For hundreds of people packed into a room, usually staying under
1200 ppm most of the time is pretty good. Like I said, I would accept that in
a restaurant. But I'm in a restaurant for an hour, maybe a couple times a
week. Spending 40 hours at those levels is a very different risk profile.

Anyway, after the conference was over, I decided to take a poll and try to
figure out how many people got COVID at the conference, and maybe get a few
clues about what activities were more or less risky.

These are the results.


# Executive summary

The main takeaways are:

* Almost 20% of polled conference attendees got COVID-19, confirmed with a
  positive test, and more if you also count people who got sick with
  COVID-like symptoms but either didn't test at all or got a negative test.

* If the 20% rate is representative of all attendees, then we can estimate
  that 2000 or more people caught COVID at SIGGRAPH.

* 15% of polled attendees who were positive for COVID reported that other
  household members who did not attend SIGGRAPH subsequently tested positive
  as well. To the extent that these results are representative of all
  attendees, it is possible that as many as a few hundred non-attending family
  members were infected.

* It didn't seem to make a difference if attendees flew to Vancouver, arrived
  by ground transportation, or lived in Vancouver and didn't travel at all.
  Travel itself, or the mode thereof, did not appear to be a significant
  driver of transmission.

* Surprisingly, whether people individually masked in the conference venues
  did not make any significant difference. (But let's return to the masking
  issue in the detailed discussion at the end.)

* The number of crowded social events did not make any difference if they were
  outdoors or if people were masked indoors. Party outdoors, or wear masks
  indoors, seems to be safe.

* The number of crowded UNMASKED INDOOR social events was important -- those
  who went to 3+ such events got COVID at **twice** the rate of those who did
  not attend any. The difference between these groups is statistically
  significant with p = 0.02.

# Methodology

The original poll can be found [here](https://t.co/aRCvmyub0M). By the time
this report is published, the poll will be closed and not accepting additional
responses.  I spread the word of the poll through public posts on Twitter
(using the [@SIGGRAPHCO2](https://twitter.com/SIGGRAPHCO2) account as well as
retweeted through my personal account), and links to those on my personal
Facebook LinkedIn accounts.

This had nothing to do with my professional responsibilities or my employers
and they were not directly involved in any way. No parties asked me to do this
or have compensated me in any way.

A CSV dump of the complete poll data can be found in
[responses.csv](responses.csv).

The code used to tally and analyze the responses is [analyze.py](analyze.py).
It requires SciPy for the statistical tests.

The raw breakdown is [results.md](results.md) and is simply the output of
running

```sh
python3 analyze.py
```

Those results are reproduced below in the following section, along with
some interpretive commentary.

In the cases where I report statistical significance, I used the Barnard exact
test on a 2x2 contingency table. It's been 35 years since I last took a
university statistics class, so if anybody knows why this is not an
appropriate test, please point out my errors or make a pull request to update
the code!

# Full breakdown

Reading responses...

Read 401 rows, 322 attendees and 79 non-attendees

COVID status of attendees vs non-attendees (control group)
----------------------------------------------------------

Non-attendees:  (total 79)

       3  ( 3.8%) : I got COVID -- tested positive between Aug 7 - Aug 19
       1  ( 1.3%) : I had COVID-like symptoms, but tested negative or did not test
      66  (83.5%) : I had no symptoms and did not test
       9  (11.4%) : I had no symptoms and tested negative after SIGGRAPH

Attendees:  (total 322)

      60  (18.6%) : I got COVID -- tested positive between Aug 7 - Aug 19
      14  ( 4.3%) : I had COVID-like symptoms, but tested negative or did not test
      92  (28.6%) : I had no symptoms and did not test
     156  (48.4%) : I had no symptoms and tested negative after SIGGRAPH

Test positivity for attendees vs non-attendees: p = 0.0032
Test positivity or having symptoms for attendees vs non-attendees: p = 0.0007

Did means of travel make a difference in COVID status of attendees?
-------------------------------------------------------------------

Travel of positive attendees:  (total 60)

      44  (73.3%) : By airplane
       4  ( 6.7%) : By land (car, train, etc.)
      12  (20.0%) : I live in the Vancouver area

Travel of presumed negative attendees:  (total 248)

     160  (64.5%) : By airplane
      16  ( 6.5%) : By land (car, train, etc.)
      72  (29.0%) : I live in the Vancouver area

Air travelers:  (total 212)

      44  (20.8%) : I got COVID -- tested positive between Aug 7 - Aug 19
       8  ( 3.8%) : I had COVID-like symptoms, but tested negative or did not test
      46  (21.7%) : I had no symptoms and did not test
     114  (53.8%) : I had no symptoms and tested negative after SIGGRAPH

Ground travelers:  (total 20)

       4  (20.0%) : I got COVID -- tested positive between Aug 7 - Aug 19
       6  (30.0%) : I had no symptoms and did not test
      10  (50.0%) : I had no symptoms and tested negative after SIGGRAPH

Vancouver residents:  (total 90)

      12  (13.3%) : I got COVID -- tested positive between Aug 7 - Aug 19
       6  ( 6.7%) : I had COVID-like symptoms, but tested negative or did not test
      40  (44.4%) : I had no symptoms and did not test
      32  (35.6%) : I had no symptoms and tested negative after SIGGRAPH

Test positivity for air travelers vs residents: p = 0.4709


Masking habits of attendees in conference venues
------------------------------------------------

Mask habits of positive attendees:  (total 60)

      16  (26.7%) : I rarely or never wore a mask indoors
      16  (26.7%) : I sometimes wore a mask indoors (e.g., depending on crowds, venue, mood, others)
      28  (46.7%) : I usually or always wore a mask indoors

Mask habits of presumed negative attendees:  (total 248)

      80  (32.3%) : I rarely or never wore a mask indoors
      56  (22.6%) : I sometimes wore a mask indoors (e.g., depending on crowds, venue, mood, others)
     112  (45.2%) : I usually or always wore a mask indoors

Rarely/never mask:  (total 103)

      16  (15.5%) : I got COVID -- tested positive between Aug 7 - Aug 19
       7  ( 6.8%) : I had COVID-like symptoms, but tested negative or did not test
      32  (31.1%) : I had no symptoms and did not test
      48  (46.6%) : I had no symptoms and tested negative after SIGGRAPH

Sometimes mask:  (total 74)

      16  (21.6%) : I got COVID -- tested positive between Aug 7 - Aug 19
       2  ( 2.7%) : I had COVID-like symptoms, but tested negative or did not test
      19  (25.7%) : I had no symptoms and did not test
      37  (50.0%) : I had no symptoms and tested negative after SIGGRAPH

Usually/always mask:  (total 145)

      28  (19.3%) : I got COVID -- tested positive between Aug 7 - Aug 19
       5  ( 3.4%) : I had COVID-like symptoms, but tested negative or did not test
      41  (28.3%) : I had no symptoms and did not test
      71  (49.0%) : I had no symptoms and tested negative after SIGGRAPH

COVID positivity of attendees who always/usually masked in conference venues:  (total 145)

      28  (19.3%) : I got COVID -- tested positive between Aug 7 - Aug 19
       5  ( 3.4%) : I had COVID-like symptoms, but tested negative or did not test
      41  (28.3%) : I had no symptoms and did not test
      71  (49.0%) : I had no symptoms and tested negative after SIGGRAPH

COVID positivity of attendees who sometimes masked in conference venues:  (total 74)

      16  (21.6%) : I got COVID -- tested positive between Aug 7 - Aug 19
       2  ( 2.7%) : I had COVID-like symptoms, but tested negative or did not test
      19  (25.7%) : I had no symptoms and did not test
      37  (50.0%) : I had no symptoms and tested negative after SIGGRAPH

COVID positivity of attendees who never/rarely masked in conference venues:  (total 103)

      16  (15.5%) : I got COVID -- tested positive between Aug 7 - Aug 19
       7  ( 6.8%) : I had COVID-like symptoms, but tested negative or did not test
      32  (31.1%) : I had no symptoms and did not test
      48  (46.6%) : I had no symptoms and tested negative after SIGGRAPH

Test positivity + symptoms for usually/always-maskers vs rarely/never-maskers: p = 0.9464


Attendee participation in crowded social events:
------------------------------------------------

Outdoor gatherings of positive attendees:  (total 60)

      18  (30.0%) : 0
      12  (20.0%) : 1
      14  (23.3%) : 2
      16  (26.7%) : 3+

Outdoor gatherings of presumed negative attendees:  (total 248)

      73  (29.4%) : 0
      57  (23.0%) : 1
      46  (18.5%) : 2
      72  (29.0%) : 3+

Masked indoor gatherings of positive attendees:  (total 60)

      25  (41.7%) : 0
      10  (16.7%) : 1
       7  (11.7%) : 2
      18  (30.0%) : 3+

Masked indoor gatherings of presumed negative attendees:  (total 248)

     114  (46.0%) : 0
      42  (16.9%) : 1
      22  ( 8.9%) : 2
      70  (28.2%) : 3+

Unmasked indoor gatherings of positive attendees:  (total 60)

       9  (15.0%) : 0
      13  (21.7%) : 1
      13  (21.7%) : 2
      25  (41.7%) : 3+

Unmasked indoor gatherings of presumed negative attendees:  (total 248)

      73  (29.4%) : 0
      32  (12.9%) : 1
      48  (19.4%) : 2
      95  (38.3%) : 3+

COVID positivity of attendees who never went to crowded indoor gatherings unmasked:  (total 83)

       9  (10.8%) : I got COVID -- tested positive between Aug 7 - Aug 19
       1  ( 1.2%) : I had COVID-like symptoms, but tested negative or did not test
      34  (41.0%) : I had no symptoms and did not test
      39  (47.0%) : I had no symptoms and tested negative after SIGGRAPH

COVID positivity of attendees who went to 3 or more crowded indoor gatherings unmasked:  (total 127)

      25  (19.7%) : I got COVID -- tested positive between Aug 7 - Aug 19
       7  ( 5.5%) : I had COVID-like symptoms, but tested negative or did not test
      26  (20.5%) : I had no symptoms and did not test
      69  (54.3%) : I had no symptoms and tested negative after SIGGRAPH

Test positivity or symptoms for 0 indoor unmasked events vs 3+: p = 0.0206

Test positivity or symptoms for 0 indoor masked events vs 3+: p = 0.9074

Test positivity or symptoms for 0 outdoor events vs 3+: p = 1.0000


Questions about spread
----------------------

Are positive attendees aware of close contact with other positive attendees:  (total 60)

      40  (66.7%) : yes
      20  (33.3%) : no

Are presumed negative attendees aware of close contact with other positive attendees:  (total 248)

     126  (50.8%) : yes
     122  (49.2%) : no

Are positive attendees aware of spread to household members:  (total 60)

       9  (15.0%) : yes
      51  (85.0%) : no

Are presumed negative attendees aware of spread to household members:  (total 248)

       2  ( 0.8%) : yes
     246  (99.2%) : no

Are positive attendees aware of spread to workplace members who did not attend:  (total 60)

      60  (100.0%) : no

Are presumed negative attendees aware of spread to workplace members who did not attend:  (total 248)

       5  ( 2.0%) : yes
     243  (98.0%) : no


# Caveats and potential sources of bias

These results should be taken with some big grains of salt. It's important
to remember that this is a retrospective study, taken voluntarily, self-reported.

The gold standard would be prospective and randomized (assigning some people
to attend SIGGRAPH in person, others to attend virtually, as well as assigning
them particular masking levels and which parties to go to). Obviously not
possible. So, retrospectively, we can describe *what* happened, but we should
not be too confident about saying *why* some people got it and some didn't.

In addition to being retrospective, it is also self-reported and voluntary,
and the respondents were found by being connected somehow to my social network
(either seeing my announcements directly, or being in groups to which it was
forwarded). So, we can see a few ways in which results may not be
representative of all conference attendees:

* Only people reachable on the internet in the 10 days or so after the
  conference could be included. This may exclude people who are extremely sick
  or hospitalized, as well as those who are blissfully on vacation or for
  other benign reasons are not within reach of a computer during the survey
  period.

* The reach of my megaphone (and the places those people in turn forwarded
  the request) may be biased -- for example, industry over academia,
  VFX/animation over other industries, technical attendees over exhibits-only
  attendees.

That said, I have no particular reason to think that these minor sources of
selection bias would substantially change the results. For example, it could
be that I was more likely to reach VFX professionals than university
professors, but I'm not aware of any hypothesis as to why those groups would
behave so differently at SIGGRAPH that they would end up with substantially
different positivity rates.

It's possible that the respondents have biased their own answers. Perhaps the
kind of people who would bother answering is over-representative of those who
got sick. Or maybe under-representative of those who got sick? I tried to
solicit responses both from those who attended and did not get sick, as well
as people who did not attend at all (but presumably mimic the attendee
demographics, if they heard my call), and as you can see from the results, we
did in fact get a lot of answers representing those groups. It's not as good
as polling all attendees for their COVID status (positive or negative), but
it's the best I can do without the full registration list.

And of course, it's possible that the responses are not truthful.  I don't
quite see why that would be the case in great enough numbers to wildly skew
the analysis, but it's worth admitting that I have no way to detect untruthful
survey answers.


# Discussion and uninformed speculation

Almost 20% of polled conference attendees got COVID-19, confirmed with a
positive test. It's over 20% if you count people who got sick with COVID-like
symptoms but either didn't test (we should presume some of those had COVID) or
who tested negatively (noting that some of these could be false negatives).

This is not just "we're in the middle of a COVID wave" background numbers --
respondents who did not attend the conference only had around 5% combined
positivity and sickness for the 2-week period. The statistical significance of
these groups getting COVID at different rates is p = 0.003 for positive tests,
and p = 0.0007 for the combination of those who tested positive and those who
had symptoms. (Clinical trials usually consider statistical significance to be
p < 0.05, or for more rigorous studies, p < 0.01).

If we believe the 20% number is representative of the entire population of
conference attendees, then we can estimate that 2000 or more people caught
COVID at SIGGRAPH.

A shocking 15% of polled attendees who were positive for COVID reported that
other household members who did not attend SIGGRAPH subsequently tested
positive as well. Extrapolating, it is likely that hundreds of non-attending
family members may have been infected after SIGGRAPH.

But on the good news front, none of the positive attendees were aware of any
non-attending coworkers to whom it spread immediately after SIGGRAPH. This
might be because the weekend after SIGGRAPH was enough time for most people to
either develop symptoms or test positive, isolating themselves before they
returned to work. And probably because a lot of them are still working from
home most of the time anyway.

It didn't seem to make much of a difference if attendees flew to Vancouver,
arrived by ground transportation, or lived in Vancouver and didn't travel at
all. Air travelers had a slightly higher positivity rate, but the statistical
significance between air travelers and Vancouver residents was only p = 0.47,
so not a strong result at all. Most likely, only a few people got it while
traveling.

Surprisingly, whether people said they masked in the conference venues did not
make any significant difference. I don't have strong measurements, but by my
recollection, and a quick visual census of some crowd photos at the
conference, only 1/3 - 1/2 of session attendees were masked (roughly matching
the percentage in this poll who responded that they usually wore a mask in
sessions). Furthermore, many of those used cloth masks or the kind of surgical
masks that don't fit tightly -- i.e., the kinds we have been recommended for
some time to "upgrade" to tighter fitting N-95 style respirators.  Remember
that the primary purpose of masking is to ensure that the wearer, if positive,
does not spread it to others, and only secondarily to offer some protection to
a negative wearer. A continued mystery is to what degree *widespread* masking
with *good* masks would have lowered transmission overall at the conference.

I think it's a shame that SIGGRAPH didn't do more to strongly encourage
masking, if not require it. The Vancouver Convention Centre had some strong
recommendations about masks at the entrances. But I didn't see any internal
signage from SIGGRAPH (certainly not anywhere near the session rooms), or
reminder slides in or between presentations. A simple slide between each
presentation saying "Help keep your fellow attendees safe by wearing a mask
any time you are not eating or drinking" could have been a strong nudge in the
right direction.

I also noticed that the chairs in the session rooms were as tightly packed as
in any ordinary year. You'd think that maybe they would have lowered the
seating capacity of the session rooms and spaced out the chairs more widely.
Or had a dense section and also a separate well-spaced section for those who
would prefer not to be so close to others. (Personally, when the room was full
enough that I couldn't find a seat that was away from other people, I just
stood or sat at the back or side walls, as far from others as I could get.)

The number of crowded social events did not make any difference if they were
outdoors or if people were masked indoors. There was no statistical difference
(p > 0.9) in positivity of the people who never went to any of these events
versus those who went to 3 or more, as long as they were either masked our
outdoors.

But the number of crowded UNMASKED INDOOR social events was important -- those
who went to 3+ such events got COVID at **twice** the rate of those who did
not attend any. The difference between these groups is statistically
significant with p = 0.0206.

Attendees who tested positive were somewhat more likely (66%) to know of a
specific person they had close contact with who also was positive, than were
people who did not get COVID (50%). That doesn't necessarily mean they caught
it from that person (or gave it to that person). And note that fully 1/3 of
people who tested positive for COVID are not aware of having been in close
contact with any specific person who had it.

I limited the number of questions in an attempt to get many responses,
figuring that the longer and more detailed the questions, the fewer people
would answer them all and do so carefully. There are some questions that would
have been interesting, but for which we have no data:

* We didn't try to break down who did which kinds of things on different days
  of the conference. We did not ask people when they first noticed symptoms or
  tested positively, which days they attended crowded events, etc.

* We did not ask which particular events people attended -- how many sessions,
  did they go to the electronic theater, did they visit the exhibition and for
  how long, which specific parties they attended.

* We didn't ask to differentiate between PCR lab tests and lateral flow rapid
  antigen tests.
  
* Some people who live in Vancouver, but who were elsewhere immediately before
  the conference, communicated that they were unsure whether to say "flew" or
  "live here." Sorry about that confusion. But I think it was few enough cases
  that it didn't make a difference.

* Regrettably, we combined "symptomatic and never tested" with "symptomatic
  and tested negative." In retrospect, it would have been nice to separate
  those, as well as to try to figure out if the latter group tested negative
  repeatedly, at least 48 hours apart (likely a true negative) or if they
  tested once and assumed negative (but could easily have just been too early
  to get a positive even if they did have COVID).

It is possible that the conclusions of this poll are not truly representative
of the attendee population as a whole. A bit of searching turns up many public
messages about other recent technical conferences having similar infection
rates -- including SIGCHI, DEFCON, and CVPR -- which provides some
corroborating evidence that we are likely in the right ballpark with our
estimates. It would be surprising for SIGGRAPH to have substantially lower
infection rates than those other conferences, in the absence of more stringent
measures to inhibit the spread.

I should note that I myself picked up COVID at the conference -- an *extremely*
mild case (three cheers for being fully vaxed and boosted). But I didn't know
that until after I'd started the process of organizing this poll.


# Feedback, questions, improvements?

If you think there are errors in my analysis, please use the GitHub Issues,
Discussions, or PR (if you have a fix).

