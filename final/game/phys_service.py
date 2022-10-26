import pyray as pr
import random as rnd
import constants

class PhysService():
    """
    Performs the physics emulation. The responsability of the class is to 
    perform all actions regarding physics objects.
    """
    def __init__(self):
        """
        Construct a new PhysService.
        """
        pr.init_physics()
        self._create_plan()
        
    def update(self):
        """
        Update physics system
        """
        pr.update_physics()

    def get_bodies_count(self):
        """
        Get the total number of bodies in the scene.
        """
        self._bodies_count = pr.get_physics_bodies_count()
        return self._bodies_count
    
    def _get_body(self,index):
        """
        Get a physics body of the bodies pool at a specific index.

        Args:
            index(int): index of the body in the bodies pool
        
        Return:
            The physics body data
        """
        self._body = pr.get_physics_body(index)
        return self._body

    def _create_plan(self):
        """
        Create a plan.
        """
        self._plan = pr.create_physics_body_rectangle(pr.Vector2(constants.MAX_X / 2, constants.MAX_Y - 50), constants.MAX_X, 1, constants.BODY_DENSITY)
        self._plan.enabled = False
    
    def create_player(self):
        """
        Create the initial player.
        """
        pr.create_physics_body_circle(pr.Vector2(constants.MAX_X / 2, 0), 20, constants.BODY_DENSITY)

    def move_thing(self, index):
        """
        Move the player.

        Args:
            index of the body in the bodies pool.
        """
        body = pr.get_physics_body(index)
        y_force = int (- body.mass)
        x_force = int (body.mass / 20)
        if pr.is_key_down(pr.KEY_RIGHT):
            pr.physics_add_force(body, pr.Vector2(x_force, 0))
        elif pr.is_key_down(pr.KEY_LEFT):
            pr.physics_add_force(body, pr.Vector2(-x_force, 0))
        elif pr.is_key_pressed(pr.KEY_UP):
            pr.physics_add_force(body, pr.Vector2(0, y_force))

    def create_things(self):
        """
        Create the other bodies.
        """
        if  pr.is_key_pressed(pr.KEY_SPACE):
            shape_position = pr.Vector2(rnd.randint(100, constants.MAX_X - 100), 0)
            shape_selector = rnd.randint(0, 3)
            if shape_selector == 0:
                pr.create_physics_body_polygon(shape_position, rnd.randint(10, 50), rnd.randint(3, 10),  constants.BODY_DENSITY)
            elif shape_selector == 1:
                pr.create_physics_body_rectangle(shape_position, rnd.randint(10, 50), rnd.randint(10, 50),  constants.BODY_DENSITY)
            else:
                pr.create_physics_body_circle(shape_position, rnd.randint(10, 50), constants.BODY_DENSITY)

    def destroy_external_body(self, i):
        """
        Destroy the bodies outside the screen.
        """
        body = self._get_body(i)
        if body and ( body.position.y > constants.MAX_Y or body.position.x > constants.MAX_X) :
            pr.destroy_physics_body(body)