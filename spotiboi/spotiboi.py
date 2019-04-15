from gi.repository import GLib
import pydbus
import pulsectl
import sys


def mute(status=True):
    """Set Spotify's mute status.

    This requires directly manipulating the pulseaudio sink
    as the client does not respond to setting volume via mpris.Player interface.
    """
    with pulsectl.Pulse("spotiboi") as pulse:
        for app in pulse.sink_input_list():
            if app.name == "Spotify":
                pulse.sink_input_mute(app.index, status)


def analyze(*arg):
    """Function called when interface properties change.

    Checks for ad signature in current track's id then mutes/unmutes Spotify.
    """
    metadata = arg[1]["Metadata"]
    if "spotify:ad" in metadata["mpris:trackid"]:
        print(metadata)
        mute(True)
    elif "spotify:track" in metadata["mpris:trackid"]:
        print(metadata)
        mute(False)
    else:
        print(metadata)


def main():
    bus = pydbus.SessionBus()
    try:
        mpris = bus.get("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    except Exception as e:
        sys.exit(e)

    mpris.onPropertiesChanged = analyze

    GLib.MainLoop().run()
