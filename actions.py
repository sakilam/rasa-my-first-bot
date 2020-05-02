# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World from the action!")

         return []

class ActionSearchRestaurant(Action):

     def name(self) -> Text:
         return "action_search_restaurant"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']

         print(entities)

         for e in entities:
             if e['entity'] == "hotel":
                 name = e['value']
             if name == "indian":
                 message = "Indian1, Indian2, Indian3, Indian4, Indian5"
             if name == "chinese":
                 message = "Chinese1, Chinese2, Chinese3, Chinese4, Chinese5"
             if name == "thai":
                 message = "Thai1, Thai2, Thai3, Thai4, Thai5"
             if name == "italian":
                 message = "Italian1, Italian2, Italian3, Italian4, Italian5"

         dispatcher.utter_message(text=message)

         return []

class ActionCoronaTracker(Action):

     def name(self) -> Text:
         return "action_corona_tracker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         response = requests.get("https://api.covid19india.org/data.json").json()

         entities = tracker.latest_message['entities']
         print("Last Message Now", entities)
         state = None

         for e in entities:
             if e['entity'] == "state":
                 state = e['value']

         message = "Please enter the correct state name"
         for data in response["statewise"]:
             if data["state"] == state.title():
                 print(data)
                 message = "Active: " + data["active"] + " Confirmed: " + data["confirmed"] + " Recovered: " + data["recovered"] + " Last Updated Time: " + data["lastupdatedtime"]
                 
         dispatcher.utter_message(text=message)

         return []

class ActionNameCountry(Action):

     def name(self) -> Text:
         return "action_name_country"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         name = tracker.get_slot("name")
         country = tracker.get_slot("country")
         leader_name = "{} & {}".format(name, country)

         message = "Your name is {} and belongs to {}. This message is from custom actions.".format(name, country)

         dispatcher.utter_message(text=message)

         return [SlotSet("leader", leader_name)]
