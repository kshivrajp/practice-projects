# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
import smtplib


class ActionReceiveUserInterest(Action):

    def name(self) -> Text:
        return "action_receive_user_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_number")

        return [SlotSet("looking_for", tracker.latest_message['text'])]

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_number")

        return [SlotSet("name", tracker.latest_message['text'])]

class ActionReceivePhoneNumber(Action):

    def name(self) -> Text:
        return "action_receive_phone_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_ex_student")

        return [SlotSet("phone_no", tracker.latest_message['text'])]

class ActionReceiveEmailId(Action):

    def name(self) -> Text:
        return "action_receive_email_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(response="utter_ex_student")

        return [SlotSet("email_id", tracker.latest_message['text'])]

class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        return [Restarted()]


# Creating new class to send emails.
class ActionEmail(Action):

    def name(self) -> Text:
        # Name of the action
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Getting the data stored in the
        # slots and storing them in variables.
        user_name = tracker.get_slot("name")
        user_phone_no = tracker.get_slot("phone_no")
        user_email_id = tracker.get_slot("email_id")
        user_looking_for = tracker.get_slot("looking_for")

        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Making connection secured
        s.starttls()

        # Authentication
        s.login("email_id", "password")

        # Message to be sent

        newline = '\n'
        message = f" This is the details of new user.{newline}\n Name: {user_name}, {newline}\n Contact no: {user_phone_no}, {newline}\n Interested in: {user_looking_for}, {newline}\n Email Id: {user_email_id}"

        # Sending the mail
        s.sendmail(from_addr="sender_email_id", to_addrs="receiver_email_id", msg=message)

        # Closing the connection
        s.quit()

        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []
