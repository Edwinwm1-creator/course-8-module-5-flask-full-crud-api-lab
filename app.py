from flask import Flask, jsonify, request

app = Flask(__name__)

class Event:
   def __init__(self, id, title):
       self.id = id
       self.title = title

   def to_dict(self):
       return {"id": self.id, "title": self.title}

events = [
   Event(1, "Tech Meetup"),
   Event(2, "Python Workshop")
]

@app.route('/', methods=['GET'])
def welcome():
   return jsonify({"message": "Welcome!"}), 200

@app.route('/events', methods=['GET'])
def get_all_events():

   # Loops through our objects and turn them into plain text dictionaries
   results = []
   for event in events:
       results.append(event.to_dict())
   return jsonify(results), 200
# TODO: POST /events - Create a new event from JSON input
@app.route('/events', methods=['POST'])
def create_event():
   data = request.get_json()
  
   # title data
   event_title = data['title']
  
   # counts no of events and adds 1 to create a new id
   new_id = len(events) + 1
  
   # Creates the new Event object and add it to our list
   new_event = Event(new_id, event_title)
   events.append(new_event)
  
   # Returns the new event data and a 201 status code
   return jsonify(new_event.to_dict()), 201

# TODO: PATCH /events/<id> - Update the title of an event
@app.route('/events/<int:id>', methods=['PATCH'])
def update_event(id):
   data = request.get_json()
   new_title = data['title']
  
   # Looks through every event to find the one with the matching ID
   for event in events:
       if event.id == id:
           event.title = new_title  # Change the title
           return jsonify(event.to_dict()), 200
          
   return jsonify({"error": "Event not found"}), 404

# TODO: DELETE /events/<id> - Remove an event from the list
@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
   # Searchs the list for the matching event
   for event in events:
       if event.id == id:
           events.remove(event)  # Delete it from the list
           return jsonify({"message": "Deleted successfully"}), 200
          
   return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
   app.run(debug=True)



