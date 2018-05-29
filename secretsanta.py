#!/usr/bin/env python3
# Michael Wood
# probably will work with python2

import random
import smtplib
################

people = {
    # 'name' : 'email address'
    'cat' : 'email@example.com',
    'dog' : 'email@example.com',
    'cheese' : 'email@example.com',
    'michael' : 'email@example.com',
}

from_address = 'santa@example.com'
independent_adjudicator = 'mainman@example.com'


#################

def mailer(to, msg):
    mail = ("From: %s\r\nTo: %s\r\nSubject: Secret Santa\r\n\r\n %s"
            % (from_address, to, msg))

    mail_server = smtplib.SMTP('localhost')
    mail_server.sendmail(from_address, [to, independent_adjudicator], mail)
    mail_server.quit()


all_valid = False

while all_valid is False:
    people_in_hat = people.copy()
    buying_for = {}
    all_valid = True

    for person in people:

        valid_choice = False
        while valid_choice is not True:

            # Person is making the choice
            choice = random.choice(list(people_in_hat.keys()))
            # Check that the person picked isn't the picker
            if person in choice:
                # People left in the hat is the chooser! oh nooo fail start
                # again
                if len(people_in_hat) <= 1:
                    all_valid = False
                    break

                continue

            # Store the winning combination for later
            buying_for[person] = choice
            # get rid of that choice from the hat
            people_in_hat.pop(choice)
            valid_choice = True

    if all_valid == True:
        for buyer in buying_for:
            mailer(people[buyer],
                   "%s is buying gift for %s" % (buyer, buying_for[buyer]))