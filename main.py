import src.airmar.airmar_input_thread as airmar
import src.rc_input.rc_input_thread as rc
import src.rudder.rudder_listener as rudder
import src.sail.sail_listener as sail
import src.nav.captain as captain

from src.boat.boat import Boat
from src.world.world import World

from src.logging.logger import Logger

def main():
    """Runs the program."""

    # State objects
    boat = Boat()
    world = World()

    # Threads
#    airmar_thread = airmar.AirmarInputThread()
    logger = Logger()
    rc_thread = rc.RCInputThread()
    Sail = sail.SailListener(boat, world)
    Rudder = rudder.RudderListener()
    captain_thread = captain.Captain(boat, world)

#    airmar_thread.start()
    rc_thread.start()
    captain_thread.start()

    while True:
        print("Waiting for input:\nd: drop mark\ns: start navigation\ne: end navigation\nc: clear course\n^C: exit program")
        cmd = input()
        if cmd == 'd':
            captain_thread.drop_mark()
        elif cmd == 's':
            captain_thread.enable()
        elif cmd == 'e':
            captain_thread.disable()
        elif cmd == 'c':
            captain_thread.clear_course()


if __name__ == "__main__":
    main()
