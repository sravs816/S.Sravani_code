import requests# type: ignore
from rasa_sdk import Action, Tracker# type: ignore
from rasa_sdk.executor import CollectingDispatcher # type: ignore
from rasa_sdk.events import SlotSet # type: ignore

class ActionFetchRiddle(Action):

    def name(self) -> str:
        return "action_fetch_riddle"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Your API key here
        api_key = ''
        api_url = 'https://api.api-ninjas.com/v1/riddles'

        headers = {
            'X-Api-Key': api_key
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            riddle = response.json()[0]
            riddle_question = riddle['question']

            # Send the riddle question to the user
            dispatcher.utter_message(text=f"Here is a riddle for you: {riddle_question}")

        
        else:
            dispatcher.utter_message(text="Sorry, I couldn't fetch a riddle at the moment.")
            return []

class ActionRevealRiddleAnswer(Action):

    def name(self) -> str:
        return "action_reveal_riddle_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        api_key = ''
        api_url = 'https://api.api-ninjas.com/v1/riddles'

        headers = {
            'X-Api-Key': api_key
        }

        response = requests.get(api_url, headers=headers)

        response.status_code == 200
        riddle = response.json()[0]
        riddle_answer = riddle['answer']
            
        dispatcher.utter_message(text=f"The answer to the riddle is: {riddle_answer}")
      
        return []