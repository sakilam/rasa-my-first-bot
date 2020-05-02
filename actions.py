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
