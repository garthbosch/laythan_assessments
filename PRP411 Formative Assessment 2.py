events = {}

# Add Event
def add_event():
    event_id = input("Enter the event ID: ")
    event_name = input("Enter the event name: ")
    max_attendees = int(input("Enter the maximum number of attendees: "))

    if event_id not in events:
        events[event_id] = {
            'name': event_name,
            'max_attendees': max_attendees,
            'attendees': []
        }
        print(f"Event '{event_name}' added successfully.")
    else:
        print(f"Event ID '{event_id}' already exists.")

# Register for event
def register_for_event(event_id, attendee_name):
    if event_id in events:
        event = events[event_id]
        if len(event['attendees']) < event['max_attendees']:
            event['attendees'].append(attendee_name)
            print(f"{attendee_name} successfully registered for event '{event['name']}'.")
        else:
            print(f"Event '{event['name']}' is full.")
    else:
        print(f"Event with ID '{event_id}' not found.")


# Search Event

# List All Events

# View Event Registrations


add_event()
add_event()
register_for_event('1', 'Laythan')
register_for_event('1', 'McKenzie')
register_for_event('2', 'Garth')
