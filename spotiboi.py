import pulsectl
from pydbus import SessionBus
from gi.repository import GLib

# A random string can be used in place of 'spotiboi' to evade detection, I think.
pulse=pulsectl.Pulse('spotiboi')

def handler(*args):
    trackid=args[1]['Metadata']['mpris:trackid']
    
    # TODO: compress if-else branching
    if ':ad:' in trackid:
        for app in pulse.sink_input_list():
            if 'Spotify' == app.name:
                pulse.sink_input_mute(app.index, 1)
    else:
        for app in pulse.sink_input_list():
            if 'Spotify' == app.name:
                pulse.sink_input_mute(app.index, 0)
    
SessionBus().get('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2').onPropertiesChanged = handler
GLib.MainLoop().run()
