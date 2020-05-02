## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## hello world path
* hello_world
  - action_hello_world

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## search restaurant path
* search_restaurant
  - action_search_restaurant

## corona tracker path
* corona_state
  - action_corona_tracker

## name path
* greet
  - utter_greet
* name_entry
  - utter_enter_country
* country_entry
  - utter_show_name_country
  - action_name_country
  - utter_show_name_country_custom
  - utter_goodbye
