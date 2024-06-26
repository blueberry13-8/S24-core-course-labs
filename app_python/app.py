from flask import Flask, render_template
from datetime import datetime
import pytz


app = Flask(__name__)


def get_time():
    """
    Get the current time in the Europe/Moscow time zone.

    Returns:
        str: Current time formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    # Get the current time in Moscow
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    # Convert time to string
    str_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return str_time


@app.route('/')
def show_time():
    """
    Route to display the current time on the homepage.

    Returns:
        render_template: Renders the index.html template with the current time.
    """
    return render_template('./index.html', time=get_time())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
