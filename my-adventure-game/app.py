from flask import Flask, render_template, request

app = Flask(__name__)

# Define the story with image paths
story = {
    'start': {
        'text': 'Hetansh starts his adventure with Mama and Papa! Where should they go next? 💫',
        'image': 'mama_papa.png',
        'choices': {
            'Meet Friends': 'meet_friends',
            'Explore Castle': 'explore_castle'
        }
    },
    'meet_friends': {
        'text': 'Hetansh meets Frogie, Drum Box, and Spinner! What should they do together? 🎉',
        'image': 'friends.png',
        'choices': {
            'Play with Lights': 'play_lights',
            'Ride the Carousel': 'ride_carousel',
            'Go Back': 'start'
        }
    },
    'explore_castle': {
        'text': 'Hetansh explores the magical castle and finds a secret path! What should he do? 🏰',
        'image': 'castle.png',
        'choices': {
            'Discover the Treasure': 'find_treasure',
            'Go on an Adventure': 'secret_adventure',
            'Go Back': 'start'
        }
    },
    'play_lights': {
        'text': 'Hetansh and his friends chase magical glowing lights! It’s so much fun! 🌟',
        'image': 'lights.png',
        'choices': {
            'Go Back to Friends': 'meet_friends'
        }
    },
    'ride_carousel': {
        'text': 'Hetansh and his friends ride a magical carousel with unicorns and magical animals! Whee! 🎠',
        'image': 'carousel.png',
        'choices': {
            'Go Back to Friends': 'meet_friends'
        }
    },
    'find_treasure': {
        'text': 'Hetansh finds a hidden treasure chest full of magical toys! 🏆',
        'image': 'treasure.png',
        'choices': {
            'Go Back to Castle': 'explore_castle'
        }
    },
    'secret_adventure': {
        'text': 'Hetansh embarks on a secret adventure in the magical forest! 🌲',
        'image': 'forest_adventure.png',
        'choices': {
            'Go Back to Castle': 'explore_castle'
        }
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Capture the choice value and use it to navigate the story
        choice = request.form.get("choice")
        if choice and choice in story:
            current_story = story[choice]
            print(current_story)
        else:
            current_story = story['start']
    else:
        current_story = story['start']

    return render_template("index.html", story=current_story)

if __name__ == "__main__":
    app.run(debug=True)
